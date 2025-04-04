from rest_framework import generics
from .models import Conversation
from .serializers import ConversationSerializer
from rest_framework.permissions import IsAuthenticated

# Vue pour gérer les conversations
class ConversationListCreate(generics.ListCreateAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]  # Seulement les utilisateurs authentifiés peuvent accéder

    def perform_create(self, serializer):
        # Associe la conversation à l'utilisateur connecté
        serializer.save(user=self.request.user)

