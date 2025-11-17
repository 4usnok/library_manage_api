from rest_framework import serializers

from authors.models import Authors


class AuthorsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели `Authors`"""

    class Meta:
        model = Authors
        fields = ['id', 'name']