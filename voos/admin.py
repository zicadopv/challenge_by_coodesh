from django.contrib import admin

from voos.models import Voo, Launch, Events


@admin.register(Voo)
class VoosAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'key',
        'title',
        'url',
        'imageUrl',
        'newsSite',
        'summary',
        'featured'
    ]


@admin.register(Launch)
class LaunchAdmin(admin.ModelAdmin):
    pass


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    pass
