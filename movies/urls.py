from django.urls import path

from . import views

urlpatterns = [
    # Genre URLs
    path('genres/', views.GenreListView.as_view(), name='genre-list'),
    path('genres/create/', views.GenreCreateView.as_view(), name='genre-create'),
    path('genres/<int:pk>/', views.GenreDetailView.as_view(), name='genre-detail'),
    path('genres/<int:pk>/update/', views.GenreUpdateView.as_view(), name='genre-update'),
    path('genres/<int:pk>/edit/', views.GenrePartialUpdateView.as_view(), name='genre-edit'),
    path('genres/<int:pk>/delete/', views.GenreDeleteView.as_view(), name='genre-delete'),
    
    # Production Companies URLs
    path('production-companies/', views.ProductionCompanyListView.as_view(), name='productioncompany-list'),
    path('production-companies/create/', views.ProductionCompanyCreateView.as_view(), name='productioncompany-create'),
    path('production-companies/<int:pk>/', views.ProductionCompanyDetailView.as_view(), name='productioncompany-detail'),
    path('production-companies/<int:pk>/update/', views.ProductionCompanyUpdateView.as_view(), name='productioncompany-update'),
    path('production-companies/<int:pk>/edit/', views.ProductionCompanyPartialUpdateView.as_view(), name='productioncompany-edit'),
    path('production-companies/<int:pk>/delete/', views.ProductionCompanyDeleteView.as_view(), name='productioncompany-delete'),
    
    # Collection URLs
    path('collections/', views.CollectionListView.as_view(), name='collection-list'),
    path('collections/create/', views.CollectionCreateView.as_view(), name='collection-create'),
    path('collections/<int:pk>/', views.CollectionDetailView.as_view(), name='collection-detail'),
    path('collections/<int:pk>/update/', views.CollectionUpdateView.as_view(), name='collection-update'),
    path('collections/<int:pk>/edit/', views.CollectionPartialUpdateView.as_view(), name='collection-edit'),
    path('collections/<int:pk>/delete/', views.CollectionDeleteView.as_view(), name='collection-delete'),

    # Movie URLs
    path('movies/', views.MovieListView.as_view(), name='movie-list'),
    path('movies/create/', views.MovieCreateView.as_view(), name='movie-create'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('movies/<int:pk>/update/', views.MovieUpdateView.as_view(), name='movie-update'),
    path('movies/<int:pk>/edit/', views.MoviePartialUpdateView.as_view(), name='movie-edit'),
    path('movies/<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movie-delete'),

    # CrewMember URLs
    path('crew-members/', views.CrewMemberListView.as_view(), name='crew-member-list'),
    path('crew-members/create/', views.CrewMemberCreateView.as_view(), name='crew-member-create'),
    path('crew-members/<int:pk>/', views.CrewMemberDetailView.as_view(), name='crew-member-detail'),
    path('crew-members/<int:pk>/update/', views.CrewMemberUpdateView.as_view(), name='crew-member-update'),
    path('crew-members/<int:pk>/partial-update/', views.CrewMemberPartialUpdateView.as_view(), name='crew-member-partial-update'),
    path('crew-members/<int:pk>/delete/', views.CrewMemberDeleteView.as_view(), name='crew-member-delete'),

    # CastMember URLs
    path('cast-members/', views.CastMemberListView.as_view(), name='cast-member-list'),
    path('cast-members/create/', views.CastMemberCreateView.as_view(), name='cast-member-create'),
    path('cast-members/<int:pk>/', views.CastMemberDetailView.as_view(), name='cast-member-detail'),
    path('cast-members/<int:pk>/update/', views.CastMemberUpdateView.as_view(), name='cast-member-update'),
    path('cast-members/<int:pk>/partial-update/', views.CastMemberPartialUpdateView.as_view(), name='cast-member-partial-update'),
    path('cast-members/<int:pk>/delete/', views.CastMemberDeleteView.as_view(), name='cast-member-delete'),

    # Review URLs
    path('reviews/', views.ReviewListView.as_view(), name='review-list'),
    path('reviews/create/', views.ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/<int:pk>/update/', views.ReviewUpdateView.as_view(), name='review-update'),
    path('reviews/<int:pk>/partial-update/', views.ReviewPartialUpdateView.as_view(), name='review-partial-update'),
    path('reviews/<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='review-delete'),

    # Comment URLs
    path('comments/', views.CommentListView.as_view(), name='comment-list'),
    path('comments/create/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
    path('comments/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/partial-update/', views.CommentPartialUpdateView.as_view(), name='comment-partial-update'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),

    # WatchedMovie URLs
    path('watched-movies/', views.WatchedMovieListView.as_view(), name='watched-movie-list'),
    path('watched-movies/create/', views.WatchedMovieCreateView.as_view(), name='watched-movie-create'),
    path('watched-movies/<int:pk>/', views.WatchedMovieDetailView.as_view(), name='watched-movie-detail'),
    path('watched-movies/<int:pk>/update/', views.WatchedMovieUpdateView.as_view(), name='watched-movie-update'),
    path('watched-movies/<int:pk>/partial-update/', views.WatchedMoviePartialUpdateView.as_view(), name='watched-movie-partial-update'),
    path('watched-movies/<int:pk>/delete/', views.WatchedMovieDeleteView.as_view(), name='watched-movie-delete'),

    # Watchlist URLs
    path('watchlists/', views.WatchlistListView.as_view(), name='watchlist-list'),
    path('watchlists/create/', views.WatchlistCreateView.as_view(), name='watchlist-create'),
    path('watchlists/<int:pk>/', views.WatchlistDetailView.as_view(), name='watchlist-detail'),
    path('watchlists/<int:pk>/update/', views.WatchlistUpdateView.as_view(), name='watchlist-update'),
    path('watchlists/<int:pk>/partial-update/', views.WatchlistPartialUpdateView.as_view(), name='watchlist-partial-update'),
    path('watchlists/<int:pk>/delete/', views.WatchlistDeleteView.as_view(), name='watchlist-delete'),

    # Notification URLs
    path('notifications/', views.NotificationListView.as_view(), name='notification-list'),
    path('notifications/create/', views.NotificationCreateView.as_view(), name='notification-create'),
    path('notifications/<int:pk>/', views.NotificationDetailView.as_view(), name='notification-detail'),
    path('notifications/<int:pk>/update/', views.NotificationUpdateView.as_view(), name='notification-update'),
    path('notifications/<int:pk>/partial-update/', views.NotificationPartialUpdateView.as_view(), name='notification-partial-update'),
    path('notifications/<int:pk>/delete/', views.NotificationDeleteView.as_view(), name='notification-delete'),
]
