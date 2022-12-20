from django.contrib import admin
from .models import UserRating, UserReview


class UserRatingAdmin(admin.ModelAdmin):
    pass


class UserReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserRating, UserRatingAdmin)
admin.site.register(UserReview, UserReviewAdmin)
