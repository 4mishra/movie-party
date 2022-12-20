import factory
import random
from datetime import date


class ResponseDataFactory(factory.Factory):
    tmdb_id = factory.Sequence(lambda u: u)
    title = factory.Sequence(lambda u: "title_%d" % u)
    overview = factory.Sequence(lambda u: "overview_%d" % u)
    vote_count = factory.Sequence(lambda u: u + 1000)
    vote_average = random.randint(1, 10)
    poster_path = factory.Sequence(lambda u: "url_%d" % u)
    release_date = date.today().isoformat()
