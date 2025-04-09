from django.urls import path
from .views import ConversationViewSet

urlpatterns = [
    path('', ConversationViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', ConversationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
