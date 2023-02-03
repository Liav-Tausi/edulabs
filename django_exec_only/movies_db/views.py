from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies_app.models import *
from movies_app.serializers import *


# Create your views here.
# @api_view(['GET'])
# def movies_list(request):
#     movies = Movie.objects.all()
#     result = []
#     for i in movies:
#         result.append({'name': i.name, 'description': i.description})
#     return Response(result)


# serializer is like a str for object, many=True if more than one
@api_view(['GET'])
def movies_list(request) -> Response:
    movies = Movie.objects.all()
    if 'name' in request.query_params:
        movies = movies.filter(name__iexact=request.query_params['name'])
    if not movies:
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# def movies_details(request, movie_id: int):
#     try:
#         movie = Movie.objects.filter(id=movie_id)
#         serializer = MovieDetailsSerializer(instance=movie, many=False)
#     except Movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     return Response(serializer.data)


@api_view(['GET', 'PATCH'])
def movies_details(request, movie_id: int):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'GET':
        serializer = MovieDetailsSerializer(instance=movie, many=False)
        return Response(serializer.data)

    if request.method == 'PATCH':
        serializer = MovieDetailsSerializer(instance=movie, data=request.data, many=False, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)




@api_view(['GET', 'PATCH', 'REMOVE'])
def actor_details(request, actor_id):
    actor = get_object_or_404(Actor, id=actor_id)

    if request.method == 'GET':
        serializer = GetActorSerializer(instance=actor, many=False)
        return Response(serializer.data)

    if request.method == 'PATCH':
        serializer = AddActorSerializer(instance=actor_id, data=request.data, many=False, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)

    if request.method == 'REMOVE':
        DeleteActorSerializer.delete(instance=actor_id)
        return Response(status=status.HTTP_200_OK)




@api_view(['POST'])
def post_actor(request):
    if request.method == 'POST':
        serializer = AddActorSerializer(data=request.data, many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response(status=status.HTTP_200_OK)





def get_rating_details(request):
    rating = Rating.objects.all()
    if 'date' in request.query_params:
        rating = Rating.objects.filter(rating_date=request.query_params['date'])
    if ('date_from' and 'date_to') in request.query_params:
        rating = Rating.objects.filter(
            rating_date__range=[request.query_params['date_from'], request.query_params['date_to']])
    if 'rating' in request.query_params:
        rating = Rating.objects.filter(rating=request.query_params['rating'])
    if ('rating_from' and 'rating_to') in request.query_params:
        rating = Rating.objects.filter(
            rating__range=[request.query_params['rating_from'], request.query_params['rating_to']])

    serializer = RatingsSerializer(instance=rating, many=True)
    return Response(serializer.data)



@api_view(['GET', 'POST'])
def rating_details(request):
    if request.method == 'GET':
        return get_rating_details(request)

    elif request.method == 'POST':
        serializer = RatingsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def delete_rating(request, movie_id, rating_id):
    get_object_or_404(Movie, movie_id)
    get_object_or_404(Rating, rating_id)

    if request.method == 'DELETE':
        DeleteActorSerializer.delete(instance=rating_id)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET', 'POST'])
def movie_actors_details(request, movie_id):
    movie_actor = get_object_or_404(MovieActor, id=movie_id)
    if request.method == 'GET':
        movie_actors = MovieActor.objects.filter(movie_id=movie_actor)
        serializer = MovieActorSerializer(instance=movie_actors, many=True)
        return Response(serializer.data)

    elif request.method == ['POST']:
        get_object_or_404(Movie, id=movie_id)
        serializer = AddMovieActorSerializer(data=request.data, context={'movie_id': movie_id, 'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)



