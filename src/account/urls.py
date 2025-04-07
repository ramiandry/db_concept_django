from django.urls import path
from .views import RegisterView, EmailAuthTokenView, current_user

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', EmailAuthTokenView.as_view(), name='login'),
    path('me/', current_user, name='current-user'),
]
