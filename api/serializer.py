from rest_framework import serializers

from voos.models import Voo


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voo
        fields = "__all__"
        # fields = (
        #     'id',
        #     'key',
        #     'title',
        #     'url',
        #     'image_url',
        #     'news_site',
        #     'summary',
        #     'featured',
        #     'launches',
        #     'events'
        # )
