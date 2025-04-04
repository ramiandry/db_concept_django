# message/views.py
from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer
from rest_framework.permissions import IsAuthenticated
from conversation.models import Conversation

class MessageListCreate(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Récupère la conversation de l'URL
        conversation = Conversation.objects.get(id=self.kwargs['conversation_id'])
        serializer.save(conversation=conversation, sender="user")
