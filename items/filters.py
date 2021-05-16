import django_filters

from items.models import Item


class ItemFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Item
        fields = {
            'title': ['icontains'],
            'price': ['gt', 'gte', 'lt', 'lte'],
        }
