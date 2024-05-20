from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegistrationSerializer, SendEmailVerificationSerializer, ConfirmEmailVerificationSerializer

class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    # def perform_create(self, serializer):
    #      return super().perform_create(serializer)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'User registered successfully. Please check your email for verification.'}, status=status.HTTP_201_CREATED)

class SendEmailVerificationView(generics.GenericAPIView):
    serializer_class = SendEmailVerificationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Verification email sent successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConfirmEmailVerificationView(generics.GenericAPIView):
    serializer_class = ConfirmEmailVerificationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Email verified successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)