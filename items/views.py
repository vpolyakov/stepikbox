from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from items.models import Item


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
