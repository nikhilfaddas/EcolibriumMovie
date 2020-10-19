from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from movie_app.models import Movies
from movie_app.serializers import MovieSerializer
from rest_framework.decorators import action


# Create your views here
# ViewSets define the view behavior


class MoviesViewSet(ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]

    @action(detail=False, methods=["get"], serializer_class=MovieSerializer, authentication_classes=[TokenAuthentication], permission_classes=[IsAuthenticated])
    def list_movies(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)