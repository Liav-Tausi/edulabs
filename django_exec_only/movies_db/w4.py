import os

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"

import django

django.setup()

from movies_app.models import *
from datetime import datetime


# Get all the actors in the db who are younger than 50 years old
query1 = Actor.objects.filter(birth_year__gte=datetime.now().year - 50)
# print(query1)


# Get movies that last less than 2.5 hours and were released after 2005
query2 = Movie.objects.filter(duration_in_min__lte=150, release_year__gte=2005)
# print(query2)


# Get all the movies that contain a word “criminal”, “mob” or “cop” in their description
from django.db.models import Q, Count, Min, Avg, Max

query3 = Movie.objects.filter(
    Q(description__contains='criminal') |
    Q(description__contains='mob') |
    Q(description__contains='cop')
).values('name', 'description')

# print(query3)


# Like previous, but get only movies that were released before 2010
query4 = Movie.objects.filter(
    Q(description__contains='criminal') |
    Q(description__contains='mob') |
    Q(description__contains='cop')
).values('name', 'description').filter(release_year__lte=2010)

# print(query4)


# Get list of actors, and add amount of movies they played in (for each one)
query5 = Actor.objects.annotate(num_movies=Count('movie'))
# for actor in query5:
#     print(f"Actor: {actor.name}, {actor.id}, Movies: {actor.num_movies}")


# Get average, min, and max rating in the system
query6 = Rating.objects.aggregate(Avg('rating'), Min('rating'), Max('rating'))
# print(query6)


# Get Movies with their avg ratings
query7 = Movie.objects.annotate(average_rating=Avg('rating__rating'))
# for movie in query7:
#     print(f"Movie: {movie.name}, Average Rating: {movie.average_rating}")


# Get ratings that were created in 2023
query8 = Rating.objects.filter(rating_date__year=2023)
# print(query8)


# Get all the actors in the system with min and max rating of the movies they played in
query9 = Actor.objects.annotate(min_rating=Min('movieactor__movie__rating'), max_rating=Max('movieactor__movie__rating'))
# for actor in query9:
#     print(actor.name, actor.min_rating, actor.max_rating)


# Get movies with average salary for actors in each one
query10 = Movie.objects.annotate(avg_salary=Avg('movieactor__salary'))
# for movie in query10:
#     print(movie.name, movie.avg_salary)


# Get actors with their average salaries
query11 = Actor.objects.annotate(avg_salary=Avg('movieactor__salary'))
# for actor in query11:
#     print(actor.name, actor.avg_salary)


# Get actors who played main roles at least once
query12 = Actor.objects.filter(movieactor__main_role=True).annotate(
    main_roles_count=Count('movieactor')
).filter(main_roles_count__gt=0)
# print(query12)


# Get movies and amount of actors who played main roles
query13 = MovieActor.objects.filter(main_role=True).values('movie_id').annotate(main_actors=Count('movie_id'))
for role in query13:
    movie = Movie.objects.get(id=role['movie_id'])
    print(f"Movie: {movie.name}, Main actors: {role['main_actors']}")

