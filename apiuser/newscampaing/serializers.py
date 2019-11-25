from rest_framework import serializers
from core.models import News


class NewsSerializer(serializers.ModelSerializer):
    """serializer for news objects"""

    class Meta:
        model = News
        fields = (
                'id',
                'title',
                'description',
        )
        read_only_fields = ('id',)
