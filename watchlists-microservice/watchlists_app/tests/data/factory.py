import factory
from ...models import UserVO, Watchlist, WatchlistItem
from movies_app.tests.data.factory import MovieFactory
from datetime import datetime
from .base_user_data import base_username, base_email
import random


class UserVOFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserVO

    username = factory.Sequence(lambda u: f"{base_username}%d" % u)
    email = factory.Sequence(lambda u: f"{base_username}%d{base_email}" % u)


class WatchlistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Watchlist

    name = factory.Sequence(lambda u: "watchlist_%d" % u)
    description = factory.Sequence(lambda u: "description_%d" % u)
    date_created = datetime.now()
    date_updated = datetime.now()

    @factory.post_generation
    def owners(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for owner in extracted:
                self.owners.add(owner)


class WatchlistItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WatchlistItem

    movie = factory.SubFactory(MovieFactory)
    interest = random.randint(1, 3)
    watchlist = factory.SubFactory(WatchlistFactory)
    date_added = datetime.now()
    watched = False if random.randint(1, 2) % 2 == 0 else True
