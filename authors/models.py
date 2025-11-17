from django.contrib.auth.models import User
from django.db import models

class Authors(models.Model):
    """Модель для авторов"""
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="выберите пользователя",
        verbose_name="authors_owner"
    )
    name = models.CharField(
        max_length=100,
        verbose_name="authors_name"
    )

    def __str__(self):
        return self.name
