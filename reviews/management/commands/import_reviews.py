from datetime import datetime

from django.core.management import BaseCommand

from reviews.models import Reviews
from utils.getting_jsons import update_or_create_elements, get_use_content

REVIEW_URL = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/reviews.json'


def assign_status(element, obj):
    if element['status'] == 'published':
        return obj.PUBLISHED
    elif element['status'] == 'hidden':
        return obj.REJECTED
    elif element['status'] == 'new':
        return obj.ON_MODERATION
    else:
        return


def process_review(element, obj):
    status = assign_status(element, obj)

    if status:
        published_at = datetime.strptime(element['published_at'], '%Y-%m-%d') if element['published_at'] else None

        obj.objects.update_or_create(
            id=element['id'],
            defaults={
                'author_id': element['author'],
                'text': element['content'],
                'created_at': datetime.strptime(element['created_at'], '%Y-%m-%d'),
                'published_at': published_at,
                'status': status,
            },
        )


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_use_content(REVIEW_URL, update_or_create_elements, process_review, Reviews)
