from .models import Genre, Movie
from rest_framework import serializers

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'