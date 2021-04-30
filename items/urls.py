from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, ItemRetrieveView, ItemListAPIView, ItemReadOnlyViewSet

item_router = DefaultRouter()
item_router.register(r'', ItemReadOnlyViewSet, basename='item')
urlpatterns = item_router.urls

# urlpatterns = [
#     # path('<int:pk>', get_item_view),
#     path('', ItemListAPIView.as_view(), ),
#     path('<int:pk>', ItemRetrieveView.as_view(), ),
# ]
