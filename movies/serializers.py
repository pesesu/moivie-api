from rest_framework import serializers

from .models import (
    Genre,
    ProductionCompany,
    Collection,
    Movie,
    CrewMember,
    CastMember,
    Review,
    Comment,
    WatchedMovie,
    Watchlist,
    Notification,
)

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']


class ProductionCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionCompany
        fields = ['id', 'name', 'logo_url', 'description', 'country']
        read_only_fields = ['id']


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name', 'description', 'poster_url', 'backdrop_url', 'movies']
        read_only_fields = ['id']

class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())
    production_companies = serializers.PrimaryKeyRelatedField(many=True, queryset=ProductionCompany.objects.all())

    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'original_title', 'release_date', 'runtime', 'synopsis', 'tagline', 'language', 
            'budget', 'revenue', 'rating', 'poster_url', 'backdrop_url', 'trailer_url', 'homepage_url', 
            'genres', 'production_companies', 'spoken_languages', 'status'
        ]
        read_only_fields = ['id']

class CrewMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrewMember
        fields = ['id', 'movie', 'name', 'role']
        read_only_fields = ['id']

class CastMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CastMember
        fields = ['id', 'movie', 'actor_name', 'character_name']
        read_only_fields = ['id']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'movie', 'rating', 'review_text', 'review_date', 'likes', 'dislikes']
        read_only_fields = ['id']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'review', 'user', 'comment_text', 'comment_date', 'likes', 'dislikes']
        read_only_fields = ['id']

class WatchedMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchedMovie
        fields = ['id', 'user', 'movie', 'watch_date']
        read_only_fields = ['id']

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = ['id', 'user', 'name', 'description', 'movies', 'created_date', 'updated_date']
        read_only_fields = ['id']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'notification_type', 'read_status', 'date']
        read_only_fields = ['id']