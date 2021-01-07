from django.urls import path,include
from . import views


app_name = 'movies'

urlpatterns = [
    path('',views.add_data,name='home'),
    # path('new/',views.new_show.as_view(),name='show')
    path('imdb_movies/',views.movieList.as_view(),name='addData')

]

