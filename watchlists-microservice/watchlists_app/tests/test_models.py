from django.test import TestCase
from ..models import UserVO, Watchlist, WatchlistItem
from .data.factory import UserVOFactory, WatchlistFactory, WatchlistItemFactory
from datetime import datetime
from movies_app.tests.data.factory import MovieFactory
from movies_app.models import Movie
import random


class TestWatchlistModel(TestCase):
    def setUp(self) -> None:
        for i in range(3):
            WatchlistFactory()

    def test_create(self) -> None:
        watchlist = Watchlist.objects.create(
            name="Watchlist 1",
            description="Description 1",
            date_created=datetime.now(),
            date_updated=datetime.now(),
        )
        watchlist.owners.add(UserVOFactory())
        self.assertIsInstance(watchlist, Watchlist)
        self.assertIsNotNone(watchlist.id)
        self.assertIsNotNone(watchlist.name)
        self.assertIsInstance(watchlist.owners.all()[0], UserVO)

    def test_add_owners(self) -> None:
        watchlist = WatchlistFactory()
        owner1 = UserVOFactory()
        owner2 = UserVOFactory()
        watchlist.owners.add(owner1, owner2)
        self.assertEqual(len(watchlist.owners.all()), 2)

    def test_remove_owner(self) -> None:
        owner1 = UserVOFactory()
        owner2 = UserVOFactory()
        watchlist = WatchlistFactory.create(owners=[owner1, owner2])
        self.assertEqual(len(watchlist.owners.all()), 2)
        watchlist.owners.remove(owner2)
        self.assertEqual(len(watchlist.owners.all()), 1)

    def test_str_method(self) -> None:
        watchlist = WatchlistFactory()
        self.assertTrue("watchlist" in watchlist.__str__())

    def test_date_updated(self) -> None:
        owner = UserVOFactory()
        watchlist = WatchlistFactory.create(owners=[owner])
        old_date = watchlist.date_updated
        watchlist.date_updated = datetime.now()
        watchlist.save()
        new_date = watchlist.date_updated
        self.assertNotEqual(old_date, new_date)


class TestWatchlistItemModel(TestCase):
    def setUp(self) -> None:
        for i in range(3):
            WatchlistItemFactory()

    def test_create_instance(self) -> None:
        movie = MovieFactory()
        watchlist = WatchlistFactory()
        interest = random.randint(1, 3)
        date_added = datetime.now()

        watchlist_item = WatchlistItem.objects.create(
            movie=movie, watchlist=watchlist, interest=interest, date_added=date_added
        )
        self.assertIsInstance(watchlist_item, WatchlistItem)
        self.assertTrue(watchlist_item.watched is False)
        self.assertIsInstance(watchlist_item.movie, Movie)
        self.assertIsInstance(watchlist_item.watchlist, Watchlist)

    def test_update_watched(self) -> None:
        watchlist_item = WatchlistItemFactory(watched=False)
        watched_status = watchlist_item.watched
        watchlist_item.watched = True
        watchlist_item.save()
        self.assertTrue(watched_status != watchlist_item.watched)

    def test_str_method(self) -> None:
        movie = MovieFactory()
        watchlist = WatchlistFactory()
        interest = random.randint(1, 3)
        date_added = datetime.now()

        watchlist_item = WatchlistItem.objects.create(
            movie=movie, watchlist=watchlist, interest=interest, date_added=date_added
        )
        self.assertEqual(watchlist_item.__str__(), f"{watchlist.name}: {movie.title}")


class TestUserVOModel(TestCase):
    def test_create_instance(self) -> None:
        username = "jinspins"
        email = "jp@watchparty.com"
        user = UserVO.objects.create(username=username, email=email)
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertIsNotNone(user.id)
        UserVO.objects.filter(username=username).delete()

    def test_str_method(self) -> None:
        username = "pinsjins"
        email = "pj@watchparty.com"
        user = UserVO.objects.create(username=username, email=email)
        self.assertEqual(user.__str__(), "pinsjins")
        UserVO.objects.filter(username=username).delete()

    def test_field_labels(self) -> None:
        user = UserVOFactory()
        username_label = user._meta.get_field("username").verbose_name
        email_label = user._meta.get_field("email").verbose_name

        self.assertEqual(username_label, "username")
        self.assertEqual(email_label, "email")
