from django.core.management import BaseCommand
from items.models import Item
from django.core.files.base import ContentFile

from utils.getting_jsons import update_or_create_elements, get_use_content


ITEMS_URL = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json'


def get_save_json_image(response, obj, element_id):
    """
    Сохраняет картинку в хранилище
    """
    image_content = response.content
    obj.image.save(f'food{element_id}.jpg', ContentFile(image_content))


def process_item(element, obj):
    """
    Создает или обновляет элемент в БД, соответсвующий элементу из json
    """
    item_tuple = obj.objects.update_or_create(
        id=element['id'],
        defaults={
            'title': element['title'],
            'description': element['description'],
            'weight': element['weight_grams'],
            'price': float(element['price']),
        },
    )
    if item_tuple[1] and element['image']:
        # Если элемент удачно создан, и если есть адрес откуда брать картинку, делает get запрос картинки
        get_use_content(element['image'], get_save_json_image, item_tuple[0], element["id"])


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_use_content(ITEMS_URL, update_or_create_elements, process_item, Item)
