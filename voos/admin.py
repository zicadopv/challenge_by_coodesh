from django.contrib import admin

from voos.models import Voo


@admin.register(Voo)
class VoosAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'key',
        'title',
        'url',
        'image_url',
        'news_site',
        'summary',
        'featured'
    ]
