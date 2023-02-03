from abc import ABC

from rest_framework import serializers
from rest_framework.serializers import Serializer

from movies_app.models import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ['id', 'name', 'release_year']
        # exclude = ['actors', 'descriptions'] if i want to import all and then exclude only need this!
        # depth = 1 the depth the query goes, for this, it will return every actor for movie
        depth = 1


class MovieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ['actors']


class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


# class ActorNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Actor
#         fields = ['name']
#
#
# class MovieActorSerializer(serializers.ModelSerializer):
#
#     actor = ActorNameSerializer(many=False)
#
#     class Meta:
#         model = MovieActor
#         exclude = ['movie']
#         depth = 1


class MovieActorSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField(many=False)

    class Meta:
        model = MovieActor
        exclude = ['movie']
        depth = 1


# class MyActorSerializer(Serializer):
#
#     id = serializers.IntegerField(read_only=True)
#
#     name = serializers.CharField(max_length=256, min_length=None,
#                                  allow_blank=False, trim_whitespace=True)
#
#     birth_year = serializers.DateField(max_value=2020, min_value=1900)
#
#     def update(self, instance, validated_data):
#         pass
#
#     def create(self, validated_data):
#         return Actor.objects.create(**validated_data)


## Not Goood!! doesnt know what model
# class AddMovieActorSerializer(serializers.ModelSerializer):
#
#     actor_id = serializers.PrimaryKeyRelatedField(many=False, read_only=False)
#
#     class Meta:
#         model = MovieActor

# not good return object actor
# class AddMovieActorSerializer(serializers.ModelSerializer):
#
#     actor_id = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Actor.objects.all())
#
#     class Meta:
#         model = MovieActor

# overwrite function to return id or pk of object actor
class WriteableMovieActorSerializer(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Actor.objects.all()

    def to_internal_value(self, data):
        val = super().to_internal_value(data)
        return val.id


class AddMovieActorSerializer(serializers.Serializer):
    actor_id = WriteableMovieActorSerializer(
        read_only=False, many=False
    )
    salary = serializers.IntegerField(min_value=0)
    main_role = serializers.BooleanField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        MovieActor.objects.create(movie_id=self.context['movie_id'], **validated_data)


class GetActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
        depth = 1


class AddActorSerializer(serializers.Serializer):
    class Meta:
        model = Actor
        fields = '__all__'
        depth = 1

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        Actor.objects.create(**validated_data)


class DeleteActorSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    @staticmethod
    def delete(instance):
        instance.delete()


class DeleteMovieRatingSerializer(serializers.Serializer):

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    @staticmethod
    def delete(instance):
        instance.delete()
