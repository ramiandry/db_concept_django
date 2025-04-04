from django.urls import path
from .views import MessageListCreate

urlpatterns = [
    path('<int:conversation_id>/messages/', MessageListCreate.as_view(), name='message-list-create'),
]
