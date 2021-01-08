from django.urls import path,include
from . import views


app_name = 'movies'

urlpatterns = [
    path('',views.add_data,name='home'),
    # path('new/',views.new_show.as_view(),name='show')
    path('imdb_movies/title/',views.movieTitle.as_view(),name='title'),
    path('imdb_movies/rating/',views.movieReateing.as_view(),name='title'),
    path('imdb_movies/release/',views.movieRelease.as_view(),name='title'),
    path('imdb_movies/duration/',views.movieDuration.as_view(),name='title'),
    path('imdb_movies/description/',views.movieDescription.as_view(),name='title'),
    path('imdb_movies/',views.movieList.as_view(),name='addData')
]

