from django.db import models

class Genre(models.Model):
    """Модель для жанра"""
    name = models.CharField(
        max_length=50,
        unique=True, # во-избежании дубликатов
        help_text="Напишите название жанра",
        verbose_name="genre_name"
    )
    def __str__(self):
        return self.name