from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings

from helpers.email_sender import Mail
from helpers.email_model import EmailVerificationHelper
from helpers.token import Token
from .models import EmailVerification


User = get_user_model()

def send_verification_email(user):
    template_path ='email_verification.html' # modify template path
    subject = 'Email Verification'
    from_email = settings.EMAIL_HOST_USER  
    to_email = user.email
    token = Token.generate_token()
    EmailVerificationHelper.save_token(user.email, token)
    context = {
        'user': user.email,
        'token': token,
    }
    try:
        Mail.send_template_mail(template_path, context, subject, from_email, to_email)
    except Exception as e:
        return Response(e)
    

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_verification_email(user)
        return user
    

class SendEmailVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField(required=False, write_only=True)

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
            if user.is_active:
                raise serializers.ValidationError("User is already active.")
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")
        return value

    def save(self, **kwargs):
        email = self.validated_data['email']
        user = User.objects.get(email=email)
        send_verification_email(user)
        return user
    

class ConfirmEmailVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        token = data.get('token')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")

        try:
            verification = EmailVerification.objects.get(user=user, token=token)
        except EmailVerification.DoesNotExist:
            raise serializers.ValidationError("Invalid or expired token.")

        if (timezone.now() - verification.created_at).days > 1:
            raise serializers.ValidationError("Token has expired.")
        
        return data

    def save(self, **kwargs):
        email = self.validated_data['email']
        token = self.validated_data['token']
        verification = EmailVerificationHelper.verify_email(email, token)
        if verification:
            return Response({'success': True}, status=status.HTTP_302_FOUND)
        return Response({'success': False}, status=status.HTTP_404_NOT_FOUND)
