import requests
from django.core.management import BaseCommand
from items.models import Item
from django.core.files.base import ContentFile


ITEMS_URL = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json'


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get(url=ITEMS_URL).json()
        if response:
            for item in response:
                item_tuple = Item.objects.update_or_create(
                        id=item['id'],
                        defaults={
                            'title': item['title'],
                            'description': item['description'],
                            'weight': item['weight_grams'],
                            'price': float(item['price']),
                        },
                    )

                if item_tuple[1] and item['image']:
                    image_response = requests.get(item['image'])
                    if image_response:
                        image_content = image_response.content
                        item_tuple[0].image.save(f'food{item["id"]}.jpg', ContentFile(image_content))
                    else:
                        print(f'Импорт картинки {item["title"]} завершился ошибкой: {response.status_code}.')

            print('Импорт данных завершен.')
            return

        else:
            print(f'Импорт данных завершился ошибкой: {response.status_code}.')
            return
