from django.contrib.auth.models import User
from django.db import models


class Car(models.Model):
    make = models.CharField("Марка автомобиля", max_length=50)
    model = models.CharField("Модель автомобиля", max_length=50)
    year = models.IntegerField("Год выпуска", null=True, blank=True)
    description = models.TextField("Описание автомобиля", null=True, blank=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)
    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.make}: {self.model}"


class Comment(models.Model):
    content = models.TextField("Содержание комментария")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    car = models.ForeignKey(
        Car,
        verbose_name="Автомобиль",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.content[:20]
