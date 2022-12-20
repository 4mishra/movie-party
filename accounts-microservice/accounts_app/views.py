from rest_framework.views import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer, ErrorSerializer, DeletedSerializer
import json


def prepare_json_response(status_code, data, serializer, many=True):
    if 200 <= status_code < 300:
        serialized_data = serializer(data, many=many)
        return Response(serialized_data.data, status=status_code)
    else:
        serialized_error = ErrorSerializer({"message": data})
        return Response(serialized_error.data, status=status_code)


@api_view(["GET", "POST"])
def list_users(request):
    if request.method == "GET":
        users = User.objects.all()
        serialized_users = UserSerializer(users, many=True)
        data = {"users": serialized_users.data}
        return Response(data, status=200)
    else:
        try:
            fields = ["username", "email", "password"]
            data = json.loads(request.body)
            for field in fields:
                if field not in data:
                    message = f"KeyError at list_users. Missing '{field}' key."
                    return prepare_json_response(500, message, ErrorSerializer)

            if data.get("test"):
                del data["test"]
                user = User.objects.create_user(**data)
            else:
                user = User.objects.create_user_and_publish(**data)
            serialized_user = UserSerializer(user, many=False)
            return Response(serialized_user.data, status=201)
        except KeyError:
            message = "KeyError at list_users POST"
            return prepare_json_response(500, message, ErrorSerializer)
        except TypeError:
            message = "TypeError at list_users POST"
            return prepare_json_response(500, message, ErrorSerializer)


@api_view(["GET", "PUT", "DELETE"])
def get_user(request, username, publish=User.objects.publish, data={}):
    if request.body:
        data = json.loads(request.body)
        if data.get("test"):
            publish = lambda *args, **kwargs: None
            del data["test"]

    if request.method == "GET":
        try:
            user = User.objects.get(username=username)
            return prepare_json_response(200, user, UserSerializer, many=False)
        except User.DoesNotExist:
            message = f"User.DoesNotExist Error with username: '{username}'."
            return prepare_json_response(500, message, ErrorSerializer)

    elif request.method == "PUT":
        message = None
        try:
            valid_fields = ["username", "email"]
            for key in data:
                if key not in valid_fields:
                    raise KeyError
                if type(data[key]) != str:
                    raise TypeError
            count = User.objects.filter(username=username).update(**data)
            if count < 1:
                raise TypeError if not data else User.DoesNotExist
            user = User.objects.get(username=data.get("username", username))
            publish(
                username=user.username,
                email=user.email,
                exchange="users",
                old_username=username,
            )
            return prepare_json_response(200, user, UserSerializer, many=False)
        except KeyError:
            message = "KeyError: Invalid key."
        except User.DoesNotExist:
            message = f"User.DoesNotExist Error with username: '{username}'."
        except TypeError:
            message = "TypeError: No JSON or invalid value type. (strings required)."
        return prepare_json_response(500, message, ErrorSerializer)

    else:
        count, _ = User.objects.filter(username=username).delete()
        if count > 0:
            publish(username=username, email=None, exchange="users", delete=True)
        return prepare_json_response(
            202, {"deleted": count > 0}, DeletedSerializer, many=False
        )
