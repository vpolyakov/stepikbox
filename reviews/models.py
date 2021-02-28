from django.db import models
from django.conf import settings
from django.utils import timezone


class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(default=timezone.now, null=True)
    status = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.text[:50]}...'
