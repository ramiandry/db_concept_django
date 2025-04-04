from django.db import models
from conversation.models import Conversation



# Modèle Message pour enregistrer chaque message
class Message(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    sender = models.CharField(max_length=50)  # peut être "user" ou "ai"
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.text[:50]}..."  # Affiche les premiers 50 caractères du message
