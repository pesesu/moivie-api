from rest_framework import generics
from .models import (
    Genre, ProductionCompany, Collection, Movie,
    CrewMember, CastMember, Review, Comment, WatchedMovie, 
    Watchlist, Notification
)
from .serializers import (
    GenreSerializer, ProductionCompanySerializer, CollectionSerializer, MovieSerializer,
    CrewMemberSerializer, CastMemberSerializer, ReviewSerializer, CommentSerializer,
    WatchedMovieSerializer, WatchlistSerializer, NotificationSerializer
)

# Create a new genre
class GenreCreateView(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# List all genres
class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# Detail view of a genre
class GenreDetailView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'pk'

# Update an existing genre (full update)
class GenreUpdateView(generics.UpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'pk'

# Edit an existing genre (partial update)
class GenrePartialUpdateView(generics.UpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    http_method_names = ['patch']
    lookup_field = 'pk'

# Delete a genre
class GenreDeleteView(generics.DestroyAPIView):
    queryset = Genre.objects.all()
    lookup_field = 'pk'

# Create a new production company
class ProductionCompanyCreateView(generics.CreateAPIView):
    queryset = ProductionCompany.objects.all()
    serializer_class = ProductionCompanySerializer

# List all production companies
class ProductionCompanyListView(generics.ListAPIView):
    queryset = ProductionCompany.objects.all()
    serializer_class = ProductionCompanySerializer

# Detail view of a production company
class ProductionCompanyDetailView(generics.RetrieveAPIView):
    queryset = ProductionCompany.objects.all()
    serializer_class = ProductionCompanySerializer
    lookup_field = 'pk'

# Update an existing production company (full update)
class ProductionCompanyUpdateView(generics.UpdateAPIView):
    queryset = ProductionCompany.objects.all()
    serializer_class = ProductionCompanySerializer
    lookup_field = 'pk'

# Edit an existing production company (partial update)
class ProductionCompanyPartialUpdateView(generics.UpdateAPIView):
    queryset = ProductionCompany.objects.all()
    serializer_class = ProductionCompanySerializer
    http_method_names = ['patch']
    lookup_field = 'pk'

# Delete a production company
class ProductionCompanyDeleteView(generics.DestroyAPIView):
    queryset = ProductionCompany.objects.all()
    serializer_class = ProductionCompanySerializer
    lookup_field = 'pk'

# Collection Views
class CollectionCreateView(generics.CreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class CollectionListView(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class CollectionDetailView(generics.RetrieveAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    lookup_field = 'pk'


class CollectionUpdateView(generics.UpdateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    lookup_field = 'pk'


class CollectionPartialUpdateView(generics.UpdateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    http_method_names = ['patch']
    lookup_field = 'pk'


class CollectionDeleteView(generics.DestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    lookup_field = 'pk'

# Create a new movie
class MovieCreateView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# List all movies
class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Detail view of a movie
class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'pk'

# Update an existing movie (full update)
class MovieUpdateView(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'pk'

# Edit an existing movie (partial update)
class MoviePartialUpdateView(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    http_method_names = ['patch']
    lookup_field = 'pk'

# Delete a movie
class MovieDeleteView(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'pk'

class CrewMemberCreateView(generics.CreateAPIView):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer

class CrewMemberListView(generics.ListAPIView):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer

class CrewMemberDetailView(generics.RetrieveAPIView):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer

class CrewMemberUpdateView(generics.UpdateAPIView):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer

class CrewMemberPartialUpdateView(generics.UpdateAPIView):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer
    http_method_names = ['patch']

class CrewMemberDeleteView(generics.DestroyAPIView):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer

# CastMember Views
class CastMemberCreateView(generics.CreateAPIView):
    queryset = CastMember.objects.all()
    serializer_class = CastMemberSerializer

class CastMemberListView(generics.ListAPIView):
    queryset = CastMember.objects.all()
    serializer_class = CastMemberSerializer

class CastMemberDetailView(generics.RetrieveAPIView):
    queryset = CastMember.objects.all()
    serializer_class = CastMemberSerializer

class CastMemberUpdateView(generics.UpdateAPIView):
    queryset = CastMember.objects.all()
    serializer_class = CastMemberSerializer

class CastMemberPartialUpdateView(generics.UpdateAPIView):
    queryset = CastMember.objects.all()
    serializer_class = CastMemberSerializer
    http_method_names = ['patch']

class CastMemberDeleteView(generics.DestroyAPIView):
    queryset = CastMember.objects.all()
    serializer_class = CastMemberSerializer

# Review Views
class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewUpdateView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewPartialUpdateView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    http_method_names = ['patch']

class ReviewDeleteView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Comment Views
class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentPartialUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['patch']

class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# WatchedMovie Views
class WatchedMovieCreateView(generics.CreateAPIView):
    queryset = WatchedMovie.objects.all()
    serializer_class = WatchedMovieSerializer

class WatchedMovieListView(generics.ListAPIView):
    queryset = WatchedMovie.objects.all()
    serializer_class = WatchedMovieSerializer

class WatchedMovieDetailView(generics.RetrieveAPIView):
    queryset = WatchedMovie.objects.all()
    serializer_class = WatchedMovieSerializer

class WatchedMovieUpdateView(generics.UpdateAPIView):
    queryset = WatchedMovie.objects.all()
    serializer_class = WatchedMovieSerializer

class WatchedMoviePartialUpdateView(generics.UpdateAPIView):
    queryset = WatchedMovie.objects.all()
    serializer_class = WatchedMovieSerializer
    http_method_names = ['patch']

class WatchedMovieDeleteView(generics.DestroyAPIView):
    queryset = WatchedMovie.objects.all()
    serializer_class = WatchedMovieSerializer

# Watchlist Views
class WatchlistCreateView(generics.CreateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer

class WatchlistListView(generics.ListAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer

class WatchlistDetailView(generics.RetrieveAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer

class WatchlistUpdateView(generics.UpdateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer

class WatchlistPartialUpdateView(generics.UpdateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    http_method_names = ['patch']

class WatchlistDeleteView(generics.DestroyAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer

# Notification Views
class NotificationCreateView(generics.CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationDetailView(generics.RetrieveAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationUpdateView(generics.UpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationPartialUpdateView(generics.UpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    http_method_names = ['patch']

class NotificationDeleteView(generics.DestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

