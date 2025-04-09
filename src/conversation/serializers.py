from rest_framework import serializers
from .models import Conversation
from message.serializers import MessageSerializer  # Importation du sérialiseur MessageSerializer
from django.contrib.auth.models import User



class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)  # ← ici, c’est juste pour affichage

    class Meta:
        model = Conversation
        fields = ['id', 'titre', 'created_at', 'updated_at', 'messages', 'user']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Sérialiser tous les champs du modèle User
