from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

from spots.models.spot import Spot

User = get_user_model()


FREE = "Free"
LOCK = "Lock"
RESERVATION_STATUS_CHOICES = [
    (FREE, "Free"),
    (LOCK, "Lock")
]


class Order(models.Model):
    """Класс заказа"""
    spot = models.ForeignKey(
        Spot,
        verbose_name="Коворкинг",
        on_delete=models.CASCADE,
        related_name="order"
    )
    user = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE,
        related_name="order"
    )
    status = models.TextField(
        max_length=10,
        choices=RESERVATION_STATUS_CHOICES,
        default=FREE,
    )
    start_date = models.DateTimeField(
        verbose_name="Начало брони",
    )
    end_date = models.DateTimeField(
        verbose_name="Конец брони",
    )
    bill = models.TextField()

    class Meta:
        """Класс Meta для Order описание метаданных."""
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ('start_date',)

    def __str__(self) -> str:
        return f'{self.user} {self.spot}'

    def validate_unique(self, *args, **kwargs):
        super(Order, self).validate_unique(*args, **kwargs)
        if not (
            isinstance(self.start_date, datetime)
            and isinstance(self.end_date, datetime)
        ):
            raise ValidationError("")
        if self.end_date < self.start_date:
            raise ValidationError(
                {'start_date': "Начало брони не может быть меньше конца"})
        qs = self.__class__._default_manager.filter(
            coworking=self.coworking,
            start_date__lt=self.end_date,
            end_date__gt=self.start_date
        )
        if qs.exists():
            raise ValidationError({
                NON_FIELD_ERRORS: ['Данный коворкинг уже забронирован', ],
            })
