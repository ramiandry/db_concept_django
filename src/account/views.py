from rest_framework.permissions import AllowAny
from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  # ← IMPORTANT
