import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

from spots.models.spot import Spot
import spots.constants as constants

User = get_user_model()


class Order(models.Model):
    """Класс заказа"""
    spot = models.ForeignKey(
        Spot,
        verbose_name='Коворкинг',
        on_delete=models.CASCADE,
        related_name='orders'
    )
    user = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='orders'
    )
    status = models.CharField(
        max_length=constants.MAX_LENGTH_STATUS,
        choices=constants.ORDER_STATUS_CHOICES,
        default=constants.WAIT_PAY,
    )
    date = models.DateField(
        verbose_name='Дата заказа'
    )
    start_time = models.TimeField(
        verbose_name='Время начала брони'
    )
    end_time = models.TimeField(
        verbose_name='Время конца брони'
    )
    bill = models.IntegerField(
        'итоговый счет'
    )

    def validate_unique(self, *args, **kwargs):
        super(Order, self).validate_unique(*args, **kwargs)
        if not (
            isinstance(self.start_time, datetime.time)
            and isinstance(self.end_time, datetime.time)
        ):
            raise ValidationError("")
        qs = self.__class__._default_manager.filter(
            spot=self.spot,
            date=self.date,
            start_time__lte=self.end_time,
            end_time__gte=self.start_time
        )
        if qs.exists():
            raise ValidationError({
                NON_FIELD_ERRORS: 'Данный коворкинг уже забронирован',
            })

    def clean(self):
        if self.end_time < self.start_time:
            raise ValidationError({
                'end_time': 'Конец брони должен быть позже начала'
            })
        return super().clean()

    class Meta:
        """Класс Meta для Order описание метаданных."""
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('start_time',)

    def __str__(self) -> str:
        return f'{self.user} {self.spot}'
