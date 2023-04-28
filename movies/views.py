from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_POST
from .models import Movie, Genre
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieSerializer, GenreSerializer
from django.http import JsonResponse


# Create your views here.
@require_safe
def index(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return render(request, 'movies/index.html', {'movies':serializer.data})


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return render(request, 'movies/detail.html', {'movie':serializer.data})


@require_safe
def recommended(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            genres = get_list_or_404(Genre)
            serializer = GenreSerializer(genres, many=True)
            return render(request, 'movies/recommended.html', {'genres':serializer.data})
    return redirect('accounts:login')


@require_POST
def recommendation(request, genre_name):
    if request.method == 'POST':
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        context = {
            'movies': serializer.data,
            'genre_name': genre_name,
        }
        return render(request, 'movies/recommendation.html', context)