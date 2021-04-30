from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand

from users.models import User
from utils.getting_jsons import update_or_create_elements, get_use_content

USERS_URL = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/recipients.json'


def process_user(element, obj):
    obj.objects.update_or_create(
        id=element['id'],
        defaults={
            'email': element['email'],
            'username': element['email'].split("@")[0],
            'password': make_password(element['password']),
            'first_name': element['info']['name'],
            'last_name': element['info']['surname'],
            'middle_name': element['info']['patronymic'],
            'phone': element['contacts']["phoneNumber"],
            'address': element['city_kladr'],
        },
    )


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_use_content(USERS_URL, update_or_create_elements, process_user, User)
