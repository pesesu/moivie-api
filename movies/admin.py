from django.contrib import admin
from .models import Genre, ProductionCompany, Collection, Movie, CrewMember, CastMember, Review, Comment, WatchedMovie, Watchlist, Notification

admin.site.register(Genre)
admin.site.register(ProductionCompany)
admin.site.register(Collection)
admin.site.register(Movie)
admin.site.register(CrewMember)
admin.site.register(CastMember)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(WatchedMovie)
admin.site.register(Watchlist)
admin.site.register(Notification)
