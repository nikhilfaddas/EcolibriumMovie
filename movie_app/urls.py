from rest_framework.routers import SimpleRouter
from movie_app.views import MoviesViewSet

# describe app level urls

simpleRouter = SimpleRouter()
simpleRouter.register('list_movies',MoviesViewSet)

urlpatterns = simpleRouter.urls