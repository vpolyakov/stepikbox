import requests
from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand
from users.models import User

USERS_URL = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/recipients.json'


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get(url=USERS_URL).json()

        if response:
            for user in response:
                User.objects.update_or_create(
                    id=user['id'],
                    defaults={
                        'email': user['email'],
                        'username': user['email'].split("@")[0],
                        'password': make_password(user['password']),
                        'first_name': user['info']['name'],
                        'last_name': user['info']['surname'],
                        'middle_name': user['info']['patronymic'],
                        'phone': user['contacts']["phoneNumber"],
                        'address': user['city_kladr'],
                    },
                )

            print('Импорт данных завершен.')
            return

        else:
            print(f'Импорт данных завершился ошибкой {response.status_code}.')
            return
