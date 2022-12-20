import factory
from ...models import UserReview, UserRating
from watchlists_app.tests.data.factory import UserVOFactory
from movies_app.tests.data.factory import MovieFactory
from datetime import datetime
import random


class UserReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserReview

    date_created = datetime.now()
    date_updated = datetime.now()
    title = factory.Sequence(lambda u: "review_title_%d" % u)
    content = factory.Sequence(lambda u: "review_content_%d" % u)
    user = factory.SubFactory(UserVOFactory)
    movie = factory.SubFactory(MovieFactory)


class UserRatingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserRating

    date = datetime.now()
    score = random.randint(1, 10)
    user = factory.SubFactory(UserVOFactory)
    movie = factory.SubFactory(MovieFactory)
