from django.contrib.auth.models import UserManager
import pika
import json


class CustomUserManager(UserManager):
    def create_user_and_publish(
        self, username, email=None, password=None, **extra_fields
    ):
        user = self.create_user(username, email, password, **extra_fields)
        self.publish(user.username, user.email, "users")
        return user

    def create_superuser_and_publish(
        self, username, email=None, password=None, **extra_fields
    ):
        superuser = self.create_superuser(username, email, password, **extra_fields)
        self.publish(superuser.username, superuser.email, "users")
        return superuser

    def publish(
        self, username, email, exchange, delete=False, old_username=None
    ) -> None:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host="rabbitmq")
            )
            channel = connection.channel()
            channel.exchange_declare(exchange=exchange, exchange_type="fanout")
            message = {
                "old_username": old_username,
                "username": username,
                "email": email,
                "delete": delete,
            }
            channel.basic_publish(
                exchange=exchange, routing_key="", body=json.dumps(message)
            )
            print(" [x] Sent %r" % message)
            connection.close()
        # Don't recover if connection was closed by broker
        except pika.exceptions.ConnectionClosedByBroker:
            print("Connection closed by broker")
        # Don't recover on channel errors
        except pika.exceptions.AMQPChannelError:
            print("AMQPChannelError")
        except Exception as e:
            print("publish user ERROR: ", e, message)
