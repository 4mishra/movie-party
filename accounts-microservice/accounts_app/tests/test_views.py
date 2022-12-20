from django.test import TestCase
from .data.factory import UserFactory
from django.urls import reverse
import json
from ..models import User


class TestListUserView(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_users = 3
        for i in range(number_of_users):
            user = UserFactory()
            user.save()

    def test_list_users_url_exists_at_expected_location(self):
        response = self.client.get(path="/api/users/")
        self.assertEqual(response.status_code, 200)

    def test_list_users_url_accessible_by_name(self):
        response = self.client.get(reverse("list_users_url"))
        self.assertEqual(response.status_code, 200)

    def test_list_users_returns_json_dict(self):
        response = self.client.get(reverse("list_users_url"))
        content = json.loads(response.content)
        self.assertEqual(type(content), dict)
        self.assertIsNotNone(content["users"])

    def test_list_users_returns_at_least_one_user(self):
        response = self.client.get(reverse("list_users_url"))
        content = json.loads(response.content)
        users = content["users"]
        self.assertGreater(len(users), 0)

    def test_list_users_post_returns_user(self):
        user_in = {
            "username": "cool_username",
            "email": "cool_email@watchparty.com",
            "password": "coolpassword",
            "test": True,
        }
        response = self.client.post(
            reverse("list_users_url"),
            data=json.dumps(user_in),
            content_type="application/json",
        )
        user_out = json.loads(response.content)
        self.assertIsNotNone(user_out)
        self.assertEqual(type(user_out), dict)
        self.assertEqual(user_out["username"], user_in["username"])
        self.assertEqual(user_out["email"], user_in["email"])
        self.assertIsNone(user_out.get("password"))

    def test_list_users_post_missing_data(self):
        user_in = {
            "username": "cool_username2",
            "email": "cool_email2@watchparty.com",
            "password": "coolpassword2",
        }
        for key in user_in:
            response = self.client.post(
                reverse("list_users_url"),
                data=json.dumps(user_in[key]),
                content_type="application/json",
            )
            content = json.loads(response.content)
            self.assertIsNotNone(content["message"])
            self.assertTrue("KeyError" in content["message"])
            self.assertEqual(response.status_code, 500)

    def test_list_users_post_handles_keyerror(self):
        incorrect_data = json.dumps([1, 2, 3])
        response = self.client.post(
            reverse("list_users_url"),
            data=json.dumps(incorrect_data),
            content_type="application/json",
        )
        content = json.loads(response.content)
        self.assertTrue("KeyError" in content["message"])
        self.assertEqual(response.status_code, 500)


class TestGetUserView(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_users = 3
        for i in range(number_of_users):
            user = UserFactory()
            user.save()

    def test_url_exists_at_expected_location(self):
        username = User.objects.all()[0].username
        response = self.client.get(path=f"/api/users/{username}/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        username = User.objects.all()[0].username
        response = self.client.get(
            reverse("get_user_url", kwargs={"username": f"{username}"})
        )
        content = json.loads(response.content)
        self.assertEqual(content["username"], username)
        self.assertEqual(response.status_code, 200)

    def test_get_method_returns_200(self):
        username = User.objects.all()[0].username
        response = self.client.get(path=f"/api/users/{username}/")
        self.assertEqual(response.status_code, 200)

    def test_get_method_json_has_has_content(self):
        username = User.objects.all()[0].username
        response = self.client.get(path=f"/api/users/{username}/")
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(content)
        self.assertEqual(content["username"], username)

    def test_get_method_handles_keyerror(self):
        response = self.client.get(path="/api/users/user_1000/")
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 500)
        self.assertTrue("User.DoesNotExist" in content["message"])


class TestPutUserView(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_users = 1
        for i in range(number_of_users):
            user = UserFactory()
            user.save()

    def test_update_with_correct_data(self):
        old_username = User.objects.all()[0].username
        new_username = "new_user_1"
        new_email = "new_email_1@watchparty.com"
        response = self.client.put(
            path=f"/api/users/{old_username}/",
            data=json.dumps(
                {"username": new_username, "email": new_email, "test": True}
            ),
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content["username"], new_username)
        self.assertEqual(content["email"], new_email)

    def test_update_with_invalid_data_types(self):
        user = User.objects.all()[0].username
        invalid_types = [False, [], {}]
        for username in invalid_types:
            response = self.client.put(
                path=f"/api/users/{user}/",
                data=json.dumps({"username": username, "test": True}),
            )
            content = json.loads(response.content)
            self.assertEqual(response.status_code, 500)
            self.assertTrue("TypeError" in content["message"])

        for email in invalid_types:
            response = self.client.put(
                path=f"/api/users/{user}/",
                data=json.dumps({"email": email, "test": True}),
            )
            content = json.loads(response.content)
            self.assertEqual(response.status_code, 500)
            self.assertTrue("TypeError" in content["message"])

    def test_update_with_invalid_keys(self):
        user = User.objects.all()[0].username
        response = self.client.put(
            path=f"/api/users/{user}/", data=json.dumps({"whoops": "invalid"})
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 500)
        self.assertTrue("TypeError", content["message"])

    def test_update_with_no_data(self):
        user = User.objects.all()[0].username
        response = self.client.put(path=f"/api/users/{user}/")
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 500)
        self.assertTrue("TypeError", content["message"])


class TestDeleteUserView(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_users = 5
        for i in range(number_of_users):
            user = UserFactory()
            user.save()

    def test_delete_successful_and_cannot_redelete(self):
        username = User.objects.all()[0].username
        response = self.client.delete(
            path=f"/api/users/{username}/", data=json.dumps({"test": True})
        )
        content = json.loads(response.content)
        self.assertTrue(content["deleted"])
        self.assertEqual(response.status_code, 202)

        # attemt to re-delete same user
        response = self.client.delete(
            path=f"/api/users/{username}/", data=json.dumps({"test": True})
        )
        content = json.loads(response.content)
        self.assertFalse(content["deleted"])
        self.assertEqual(response.status_code, 202)
