from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# Modèle Conversation pour l'historique des conversations
class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # l'utilisateur associé à la conversation
    created_at = models.DateTimeField(auto_now_add=True)  # date de création de la conversation
    updated_at = models.DateTimeField(auto_now=True)  # date de la dernière mise à jour de la conversation

    def __str__(self):
        return f"Conversation with {self.user.username} - {self.created_at}"