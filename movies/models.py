from django.db import models
from django.contrib.auth import get_user_model

from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class ProductionCompany(models.Model):
    name = models.CharField(max_length=255)
    logo_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Collection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    poster_url = models.URLField(blank=True, null=True)
    backdrop_url = models.URLField(blank=True, null=True)
    movies = models.ManyToManyField('Movie', related_name='collections')

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.DateField()
    runtime = models.PositiveIntegerField()
    synopsis = models.TextField(blank=True, null=True)
    tagline = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=50)
    budget = models.BigIntegerField(blank=True, null=True)
    revenue = models.BigIntegerField(blank=True, null=True)
    rating = models.CharField(max_length=10, blank=True, null=True)
    poster_url = models.URLField(blank=True, null=True)
    backdrop_url = models.URLField(blank=True, null=True)
    trailer_url = models.URLField(blank=True, null=True)
    homepage_url = models.URLField(blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    production_companies = models.ManyToManyField(ProductionCompany, related_name='movies')
    spoken_languages = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

class CrewMember(models.Model):
    movie = models.ForeignKey(Movie, related_name='crew_members', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} ({self.role})'

class CastMember(models.Model):
    movie = models.ForeignKey(Movie, related_name='cast_members', on_delete=models.CASCADE)
    actor_name = models.CharField(max_length=255)
    character_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.actor_name} as {self.character_name}'

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    review_text = models.TextField(blank=True, null=True)
    review_date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Review by {self.user.username} for {self.movie.title}'

class Comment(models.Model):
    review = models.ForeignKey(Review, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Comment by {self.user.username}'

class WatchedMovie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watch_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} watched {self.movie.title}'

class Watchlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_watchlists', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    movies = models.ManyToManyField(Movie, related_name='watchlists')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} by {self.user.username}'

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notifications', on_delete=models.CASCADE)
    message = models.TextField()
    notification_type = models.CharField(max_length=50)
    read_status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification for {self.user.username}'

