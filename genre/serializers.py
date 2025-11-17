from rest_framework import serializers

from genre.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для модели `Genre`"""

    class Meta:
        model = Genre
        fields = ['id', 'name']