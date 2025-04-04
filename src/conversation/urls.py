from django.urls import path
from .views import ConversationListCreate

urlpatterns = [
    path('', ConversationListCreate.as_view(), name='conversation-list-create'),
]
