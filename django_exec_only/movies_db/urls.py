from django.urls import path

# from this package
from . import views

urlpatterns = [
    path('api/v1/movie', views.movies_list),
    path('api/v1/movie/<int:movie_id>', views.movies_details),
    path('api/v1/movie/<int:movie_id>/actors', views.movie_actors_details),
    path('api/v1/actor/', views.post_actor),
    path('api/v1/actor/<int:actor_id>', views.actor_details),
    path('api/v1/movie/rating/', views.rating_details),
    path('api/v1/movie/<int:movie_id>/<int:rating_id>')
]