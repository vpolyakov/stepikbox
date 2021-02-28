import requests
from django.core.management import BaseCommand
from items.models import Item
from django.core.files.base import ContentFile


ITEMS_URL = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json'


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get(url=ITEMS_URL).json()

        for item in response:
            itm = Item.objects.get_or_create(
                    id=item['id'],
                    defaults={
                        'title': item['title'],
                        'description': item['description'],
                        'weight': item['weight_grams'],
                        'price': float(item['price']),
                    },
                )
            if itm[1] and item['image']:
                cnt = requests.get(item['image']).content
                itm[0].image.save(f'food{item["id"]}.jpg', ContentFile(cnt))

        return
