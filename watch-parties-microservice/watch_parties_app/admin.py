from django.contrib import admin
from .models import UserVO


class UserVOAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserVO, UserVOAdmin)
