from django.db import models


class Launch(models.Model):
    key = models.CharField(
        max_length=100,
        unique=True
    )
    provider = models.CharField(
        max_length=30
    )

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = 'Launch'
        verbose_name_plural = 'Launchs'


class Events(models.Model):
    key = models.CharField(
        max_length=100,
        unique=True
    )
    provider = models.CharField(
        max_length=30
    )

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'


class Voo(models.Model):
    key = models.IntegerField(
        unique=True,
        null=True
    )
    title = models.CharField(
        max_length=200
    )
    url = models.URLField(
        max_length=200
    )
    imageUrl = models.URLField(
        max_length=200
    )
    newsSite = models.CharField(
        max_length=30
    )
    summary = models.CharField(
        max_length=255
    )
    publishedAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    featured = models.BooleanField()
    launches = models.ForeignKey(
        Launch,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    events = models.ForeignKey(
        Events,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title
