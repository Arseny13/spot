# Generated by Django 4.2.5 on 2023-09-22 18:18

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Категория"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=500, verbose_name="Описание"
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Equipment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, verbose_name="Название оборудования"
                    ),
                ),
                (
                    "description",
                    models.TextField(max_length=500, verbose_name="Описание"),
                ),
            ],
            options={
                "verbose_name": "Оборудование",
                "verbose_name_plural": "Оборудования",
            },
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=64, unique=True, verbose_name="Название"
                    ),
                ),
                ("street", models.CharField(max_length=100, verbose_name="Улица")),
                (
                    "house_number",
                    models.CharField(max_length=10, verbose_name="Номер дома"),
                ),
                (
                    "apartment_number",
                    models.CharField(
                        blank=True, max_length=10, verbose_name="Номер квартиры"
                    ),
                ),
                (
                    "latitude",
                    models.DecimalField(
                        decimal_places=6,
                        max_digits=9,
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=-90,
                                message="Широта должна быть в диапазоне от -90 до 90",
                            ),
                            django.core.validators.MaxValueValidator(
                                limit_value=90,
                                message="Широта должна быть в диапазоне от -90 до 90",
                            ),
                        ],
                        verbose_name="Широта",
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        decimal_places=6,
                        max_digits=9,
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=-180,
                                message="Долгота должна быть в диапазоне от -180 до 180",
                            ),
                            django.core.validators.MaxValueValidator(
                                limit_value=180,
                                message="Долгота должна быть в диапазоне от -180 до 180",
                            ),
                        ],
                        verbose_name="Долгота",
                    ),
                ),
                (
                    "plan_photo",
                    models.ImageField(
                        blank=True,
                        help_text="План коворкинга",
                        upload_to="images/plans/",
                        verbose_name="План",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=500, verbose_name="Описание"
                    ),
                ),
            ],
            options={
                "verbose_name": "Локация",
                "verbose_name_plural": "Локации",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Ожидается оплата", "Ожидается оплата"),
                            ("Оплачено", "Оплачено"),
                            ("Забранировано", "Забранировано"),
                            ("Не оплачено", "Не оплачено"),
                        ],
                        default="Ожидается оплата",
                        max_length=16,
                    ),
                ),
                ("date", models.DateField(verbose_name="Дата заказа")),
                (
                    "start_time",
                    models.TimeField(
                        choices=[
                            (datetime.time(8, 0), "08:00"),
                            (datetime.time(9, 0), "09:00"),
                            (datetime.time(10, 0), "10:00"),
                            (datetime.time(11, 0), "11:00"),
                            (datetime.time(12, 0), "12:00"),
                            (datetime.time(13, 0), "13:00"),
                            (datetime.time(14, 0), "14:00"),
                            (datetime.time(15, 0), "15:00"),
                            (datetime.time(16, 0), "16:00"),
                            (datetime.time(17, 0), "17:00"),
                            (datetime.time(18, 0), "18:00"),
                            (datetime.time(19, 0), "19:00"),
                            (datetime.time(20, 0), "20:00"),
                        ],
                        default=datetime.time(8, 0),
                        verbose_name="Время начала брони",
                    ),
                ),
                (
                    "end_time",
                    models.TimeField(
                        choices=[
                            (datetime.time(9, 0), "09:00"),
                            (datetime.time(10, 0), "10:00"),
                            (datetime.time(11, 0), "11:00"),
                            (datetime.time(12, 0), "12:00"),
                            (datetime.time(13, 0), "13:00"),
                            (datetime.time(14, 0), "14:00"),
                            (datetime.time(15, 0), "15:00"),
                            (datetime.time(16, 0), "16:00"),
                            (datetime.time(17, 0), "17:00"),
                            (datetime.time(18, 0), "18:00"),
                            (datetime.time(19, 0), "19:00"),
                            (datetime.time(20, 0), "20:00"),
                            (datetime.time(21, 0), "21:00"),
                        ],
                        default=datetime.time(9, 0),
                        verbose_name="Время конца брони",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заказ",
                "verbose_name_plural": "Заказы",
                "ordering": ("date", "start_time"),
            },
        ),
        migrations.CreateModel(
            name="Price",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=1,
                                message="Цена не может быть меньше или равна нулю.",
                            )
                        ],
                        verbose_name="Цена",
                    ),
                ),
                (
                    "discount",
                    models.PositiveSmallIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MaxValueValidator(
                                limit_value=100,
                                message="Скидка не может превышать 100%",
                            )
                        ],
                        verbose_name="Скидка",
                    ),
                ),
                (
                    "total_price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=1,
                                message="Цена не может быть меньше или равна нулю.",
                            )
                        ],
                        verbose_name="Итоговая стоимость",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=500, verbose_name="Описание"
                    ),
                ),
            ],
            options={
                "verbose_name": "Цена",
                "verbose_name_plural": "Цены",
            },
        ),
        migrations.CreateModel(
            name="Spot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, verbose_name="Название рабочего места"
                    ),
                ),
                (
                    "description",
                    models.TextField(max_length=500, verbose_name="Описание"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="spots",
                        to="spots.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Место",
                "verbose_name_plural": "Места",
                "ordering": ("location", "category"),
            },
        ),
        migrations.CreateModel(
            name="SpotEquipment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "equipment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="spot_equipment",
                        to="spots.equipment",
                    ),
                ),
                (
                    "spot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="spot_equipment",
                        to="spots.spot",
                    ),
                ),
            ],
            options={
                "verbose_name": "Место и оборудование",
                "verbose_name_plural": "Места и оборудования",
            },
        ),
        migrations.AddField(
            model_name="spot",
            name="equipment",
            field=models.ManyToManyField(
                related_name="spots",
                through="spots.SpotEquipment",
                to="spots.equipment",
                verbose_name="Оборудование",
            ),
        ),
        migrations.AddField(
            model_name="spot",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="spots",
                to="spots.location",
                verbose_name="Локация",
            ),
        ),
        migrations.AddField(
            model_name="spot",
            name="price",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="spots",
                to="spots.price",
                verbose_name="Цена",
            ),
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "raiting",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="Оценка отзыва",
                    ),
                ),
                (
                    "description",
                    models.TextField(max_length=100, verbose_name="Текст отзыва"),
                ),
                (
                    "pub_date",
                    models.DateField(auto_now_add=True, verbose_name="Дата создания"),
                ),
                (
                    "booked_spot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="spots.order",
                        verbose_name="Заказ",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="reviews",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Отзыв",
                "verbose_name_plural": "Отзывы",
            },
        ),
        migrations.AddField(
            model_name="order",
            name="spot",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to="spots.spot",
                verbose_name="Коворкинг",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.CreateModel(
            name="Favorite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="favorites",
                        to="spots.location",
                        verbose_name="Коворкинг",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="favorites",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Избранное",
                "verbose_name_plural": "Избранное",
            },
        ),
        migrations.CreateModel(
            name="ExtraPhoto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        help_text="Фото места", upload_to="images/", verbose_name="Фото"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Описание"
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="location_extra_photo",
                        to="spots.location",
                    ),
                ),
            ],
            options={
                "verbose_name": "Фотография",
                "verbose_name_plural": "Фотографии",
                "ordering": ("location",),
            },
        ),
        migrations.AddConstraint(
            model_name="spotequipment",
            constraint=models.UniqueConstraint(
                fields=("spot", "equipment"), name="unique_equipment"
            ),
        ),
        migrations.AddConstraint(
            model_name="spot",
            constraint=models.UniqueConstraint(
                fields=("name", "location"), name="unique_name_in_location"
            ),
        ),
        migrations.AddConstraint(
            model_name="favorite",
            constraint=models.UniqueConstraint(
                fields=("user", "location"), name="unique_user_location_favorite"
            ),
        ),
    ]
