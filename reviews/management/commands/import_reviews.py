from datetime import datetime
import requests
from django.core.management import BaseCommand
from reviews.models import Reviews

REVIEW_URL = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/reviews.json'


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get(url=REVIEW_URL).json()

        for review in response:
            Reviews.objects.get_or_create(
                id=review['id'],
                defaults={
                    'author_id': review['author'],
                    'text': review['content'],
                    'created_at': datetime.strptime(review['created_at'], '%Y-%m-%d'),
                    'published_at': (datetime.strptime(review['published_at'], '%Y-%m-%d')
                                     if review['published_at'] else None),
                    'status': review['status'],
                },
            )

        return
