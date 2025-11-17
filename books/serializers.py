from rest_framework import serializers

from books.models import Books


class BooksSerializer(serializers.ModelSerializer):
    """Сериализатор для модели `Books`"""

    class Meta:
        model = Books
        fields = ['id', 'name', 'genre', 'date_pub']