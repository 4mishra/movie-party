from django.contrib import admin
from .models import UserVO, Watchlist, WatchlistItem


class UserVOAdmin(admin.ModelAdmin):
    pass


class WatchlistAdmin(admin.ModelAdmin):
    pass


class WatchlistItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserVO, UserVOAdmin)
admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(WatchlistItem, WatchlistItemAdmin)
