from django.shortcuts import render, redirect
from . models import Movie
from . forms import MovieForm
# Create your views here.


def index(request):
    movie = Movie.objects.all()
    context = {
        'movielist': movie
    }
    return render(request, 'index.html', context)


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "details.html", {'movie': movie})


def update(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "edit.html", {'form':form,'movie': movie})


def delete(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return redirect('/')
    return render(request, "delete.html")