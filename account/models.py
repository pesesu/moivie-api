from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import MyUserManager
from movies.models import Movie, WatchedMovie


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=50, unique=True)
    profile_picture = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    join_date = models.DateTimeField(auto_now_add=True)
    favorite_movies = models.ManyToManyField(Movie, related_name='favorited_by', blank=True)
    watchlist = models.ManyToManyField(Movie, related_name='in_watchlists', blank=True)
    watched_movies = models.ManyToManyField(Movie, through=WatchedMovie, related_name='watched_by', blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class EmailVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Email verification for {self.user.email}"