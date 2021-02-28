from django.urls import path
from .views import get_item_view

urlpatterns = [
    path('<int:pk>', get_item_view),
]
