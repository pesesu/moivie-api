from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.RegistrationAPIView.as_view(), name='register'),
    path('send-verification-email/', views.SendEmailVerificationView.as_view(), name='send-verification-email'),
    path('confirm-email-verification/', views.ConfirmEmailVerificationView.as_view(), name='confirm-email-verification'),
]