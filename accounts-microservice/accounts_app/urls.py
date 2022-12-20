from django.urls import path
from .views import list_users, get_user

urlpatterns = [
    path("", list_users, name="list_users_url"),
    path("<str:username>/", get_user, name="get_user_url"),
]
