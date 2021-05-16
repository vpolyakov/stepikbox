from django.core.management import BaseCommand
from rest_framework.authtoken.models import Token

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        token = Token.objects.create(user=User.objects.get(id=1))
        print(token.key)
