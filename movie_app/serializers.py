from movie_app.models import Movies
from rest_framework.serializers import ModelSerializer

# Serializers define the API representation

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'