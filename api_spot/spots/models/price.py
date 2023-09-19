from django.core.validators import MinValueValidator
from django.db import models

from spots.constants import (
    DISCOUNT_NEGATIVE_MESSAGE,
    PRICE_NEGATIVE_OR_ZERO_MESSAGE,
    MIN_VALUE,
    ZERO,
)


class Price(models.Model):
    # spot = models.ForeignKey(
    #     'spots.Spot',
    #     on_delete=models.CASCADE,
    #     related_name='prices',
    #     verbose_name='Место',
    # )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
        validators=[
            MinValueValidator(
                limit_value=MIN_VALUE,
                message=PRICE_NEGATIVE_OR_ZERO_MESSAGE,
            )
        ],
    )
    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        verbose_name='Скидка',
        validators=[
            MinValueValidator(
                limit_value=ZERO,
                message=DISCOUNT_NEGATIVE_MESSAGE,
            )
        ],
    )
    description = models.TextField(
        max_length=500,
        blank=True,
        verbose_name='Описание',
    )

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return str(self.price)
