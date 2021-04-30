from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from items.filters import ItemFilter
from items.models import Item
from items.paginators import ItemPaginator
from items.serializers import ItemSerializer


# Если пишешь кастомное и легаси API, то с ViewSet это будет сложно
# Если пишешь с нуля, то пару строк и получаешь полноценное API
class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = ItemPaginator
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = ItemFilter
    ordering = ['price', 'title']
    ordering_fields = ['price', 'title']


class ItemReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = ItemPaginator
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = ItemFilter
    ordering = ['price', 'title']
    ordering_fields = ['price', 'title', 'weight']


# class ItemRetrieveView(RetrieveAPIView):  # Просмотр элемента гетом
# class ItemRetrieveView(RetrieveUpdateAPIView):  # Просмотр с апдейтом постом
class ItemRetrieveView(RetrieveUpdateDestroyAPIView):  # Просмотр гетом, апдейт постом и удаление delete'ом
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


# class ItemListAPIView(ListAPIView):  # Просто список элементов гетом
class ItemListAPIView(ListCreateAPIView):  # Список елементов гетом, плюс создать элемент постом
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    pagination_class = ItemPaginator
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = ItemFilter


@api_view(http_method_names=['GET'])
def get_item_view(request, pk, *args, **kwargs):
    try:
        item = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response({
        'id': item.id,
        'title': item.title,
        'description': item.description,
        'image': request.build_absolute_uri(item.image.url),
        'weight': item.weight,
        'price': f'{item.price:.2f}',
    })
