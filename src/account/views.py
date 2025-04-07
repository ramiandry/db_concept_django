from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from .serializers import RegisterSerializer, EmailAuthTokenSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
import rest_framework.authtoken.models as drf_models
from rest_framework.decorators import api_view, permission_classes

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class EmailAuthTokenView(ObtainAuthToken):
    serializer_class = EmailAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = drf_models.Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id,
            'email': user.email
        })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = request.user
    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email
    })
