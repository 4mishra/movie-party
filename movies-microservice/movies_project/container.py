from dependency_injector import containers, providers
from movies_app import acls


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    movie_search = providers.Factory(acls.MovieRequests)
