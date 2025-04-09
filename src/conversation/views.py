from rest_framework import viewsets, permissions
from .models import Conversation
from .serializers import ConversationSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Renvoyer seulement les conversations de l'utilisateur connecté
        return Conversation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Associer la conversation à l'utilisateur connecté
        serializer.save(user=self.request.user)
