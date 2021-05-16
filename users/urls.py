from django.urls import path
from rest_framework.authtoken import views

from .views import CurrentUserAPIView, RegisterUserViewSet


urlpatterns = [
    path('auth/login', views.obtain_auth_token),
    path('auth/register', RegisterUserViewSet.as_view()),
    path('current/', CurrentUserAPIView.as_view()),
]
