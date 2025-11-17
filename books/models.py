from django.db import models

from authors.models import Authors
from genre.models import Genre


class Books(models.Model):
    """Модель для книг"""
    owner = models.ForeignKey(
        Authors,
        on_delete=models.CASCADE,
        help_text="Выберите автора",
        verbose_name="books_owner"
    )
    name = models.CharField(
        max_length=100,
        help_text="Напишите название книги",
        verbose_name="books_name"
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        help_text="Выберите название жанра",
        verbose_name="books_genre"
    )
    date_pub = models.DateTimeField(
        help_text="Укажите дату и время публикации",
        verbose_name="books_date_pub",
        auto_now_add=True
    )

    def __str__(self):
        return self.name
