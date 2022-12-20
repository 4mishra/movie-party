from django.contrib.auth import get_user_model
from django.test import TestCase
from accounts_app.tests.data.factory import UserFactory
from .data.base_user_data import base_user


class UserModelTests(TestCase):
    def test_create_multiple_users(self):
        for i in range(3):
            user = UserFactory()
            self.assertIn(base_user["email"], user.email)
            self.assertIn(base_user["username"], user.email)
            self.assertIn(base_user["username"], user.username)
            self.assertIsNotNone(user.password)
            self.assertTrue(user.is_active)
            self.assertFalse(user.is_staff)
            self.assertFalse(user.is_superuser)
            try:
                self.assertIsNone(user.boring)
            except AttributeError:
                pass

    def test_incorrect_user_data(self):
        User = get_user_model()
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(ValueError):
            User.objects.create_user(username="", email="", password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="siegfried", email="siegfried@watchparty.com", password="password"
        )
        self.assertEqual(admin_user.email, "siegfried@watchparty.com")
        self.assertEqual(admin_user.username, "siegfried")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username="beren",
                email="beren@watchparty.com",
                password="foo",
                is_superuser=False,
            )
