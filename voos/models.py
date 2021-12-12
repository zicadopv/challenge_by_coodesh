from django.db import models


class Voo(models.Model):
    key = models.IntegerField(
        unique=True,
        null=True
    )
    title = models.CharField(
        max_length=255
    )
    url = models.URLField(
        max_length=255
    )
    image_url = models.URLField(
        max_length=255
    )
    news_site = models.CharField(
        max_length=100
    )
    summary = models.TextField()
    published_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    featured = models.BooleanField()
    launches = models.JSONField(
        blank=True,
        default=list
    )
    events = models.JSONField(
        blank=True,
        default=list
    )

    def __str__(self):
        return self.title
