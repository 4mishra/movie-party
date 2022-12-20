import factory
from ... import models
from .base_user_data import base_user


class UserFactory(factory.Factory):
    class Meta:
        model = models.User

    username = factory.Sequence(lambda u: f"{base_user['username']}%d" % u)
    first_name = factory.Sequence(lambda u: f"{base_user['first_name']}%d" % u)
    last_name = factory.Sequence(lambda u: f"{base_user['last_name']}%d" % u)
    email = factory.LazyAttribute(lambda obj: f"%s{base_user['email']}" % obj.username)
    password = factory.Sequence(lambda u: f"{base_user['password']}%d" % u)
    is_active = True


class AdminFactory(UserFactory):
    is_superuser = True
    is_admin = True
