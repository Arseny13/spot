# Generated by Django 4.2.5 on 2023-09-27 20:40

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название оборудования')),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Оборудования',
            },
        ),
        migrations.CreateModel(
            name='ExtraPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Фото места', upload_to='images/', verbose_name='Фото')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
                'ordering': ('location',),
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Избранное',
                'verbose_name_plural': 'Избранное',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Название')),
                ('open_time', models.TimeField(verbose_name='Время открытия')),
                ('close_time', models.TimeField(verbose_name='время закрытия')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=10, verbose_name='Номер дома')),
                ('metro', models.CharField(blank=True, max_length=128, null=True, verbose_name='Метро')),
                ('city', models.CharField(max_length=64, verbose_name='Город')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, validators=[django.core.validators.MinValueValidator(limit_value=-90, message='Широта должна быть в диапазоне от -90 до 90'), django.core.validators.MaxValueValidator(limit_value=90, message='Широта должна быть в диапазоне от -90 до 90')], verbose_name='Широта')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, validators=[django.core.validators.MinValueValidator(limit_value=-180, message='Долгота должна быть в диапазоне от -180 до 180'), django.core.validators.MaxValueValidator(limit_value=180, message='Долгота должна быть в диапазоне от -180 до 180')], verbose_name='Долгота')),
                ('main_photo', models.ImageField(blank=True, help_text='Главное фото локации', upload_to='images/main_photo/', verbose_name='Главное фото')),
                ('plan_photo', models.ImageField(blank=True, help_text='План коворкинга', upload_to='images/plans/', verbose_name='План')),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Локация',
                'verbose_name_plural': 'Локации',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Ожидается оплата', 'Ожидается оплата'), ('Не оплачено', 'Не оплачено'), ('Оплачено', 'Оплачено'), ('Завершен', 'Завершен'), ('Отменен', 'Отменен')], default='Ожидается оплата', max_length=16)),
                ('date', models.DateField(verbose_name='Дата заказа')),
                ('start_time', models.TimeField(choices=[(datetime.time(0, 0), '00:00'), (datetime.time(1, 0), '01:00'), (datetime.time(2, 0), '02:00'), (datetime.time(3, 0), '03:00'), (datetime.time(4, 0), '04:00'), (datetime.time(5, 0), '05:00'), (datetime.time(6, 0), '06:00'), (datetime.time(7, 0), '07:00'), (datetime.time(8, 0), '08:00'), (datetime.time(9, 0), '09:00'), (datetime.time(10, 0), '10:00'), (datetime.time(11, 0), '11:00'), (datetime.time(12, 0), '12:00'), (datetime.time(13, 0), '13:00'), (datetime.time(14, 0), '14:00'), (datetime.time(15, 0), '15:00'), (datetime.time(16, 0), '16:00'), (datetime.time(17, 0), '17:00'), (datetime.time(18, 0), '18:00'), (datetime.time(19, 0), '19:00'), (datetime.time(20, 0), '20:00'), (datetime.time(21, 0), '21:00'), (datetime.time(22, 0), '22:00')], default=datetime.time(0, 0), verbose_name='Время начала брони')),
                ('end_time', models.TimeField(choices=[(datetime.time(1, 0), '00:55'), (datetime.time(2, 0), '01:55'), (datetime.time(3, 0), '02:55'), (datetime.time(4, 0), '03:55'), (datetime.time(5, 0), '04:55'), (datetime.time(6, 0), '05:55'), (datetime.time(7, 0), '06:55'), (datetime.time(8, 0), '07:55'), (datetime.time(9, 0), '08:55'), (datetime.time(10, 0), '09:55'), (datetime.time(11, 0), '10:55'), (datetime.time(12, 0), '11:55'), (datetime.time(13, 0), '12:55'), (datetime.time(14, 0), '13:55'), (datetime.time(15, 0), '14:55'), (datetime.time(16, 0), '15:55'), (datetime.time(17, 0), '16:55'), (datetime.time(18, 0), '17:55'), (datetime.time(19, 0), '18:55'), (datetime.time(20, 0), '19:55'), (datetime.time(21, 0), '20:55'), (datetime.time(22, 0), '21:55'), (datetime.time(23, 0), '22:55')], default=datetime.time(1, 0), verbose_name='Время конца брони')),
                ('bill', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Итоговый чек')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('date', 'start_time'),
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(limit_value=1, message='Цена не может быть меньше или равна нулю.')], verbose_name='Цена')),
                ('discount', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(limit_value=70, message='Скидка не может превышать 70%')], verbose_name='Скидка')),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(limit_value=1, message='Цена не может быть меньше или равна нулю.')], verbose_name='Итоговая стоимость')),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
            },
        ),
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название рабочего места')),
                ('category', models.CharField(choices=[('Рабочее место', 'Рабочее место'), ('Переговорная', 'Переговорная')], max_length=64, verbose_name='Категория')),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
                'ordering': ('location', 'category'),
            },
        ),
        migrations.CreateModel(
            name='SpotEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spot_equipment', to='spots.equipment')),
                ('spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spot_equipment', to='spots.spot')),
            ],
            options={
                'verbose_name': 'Место и оборудование',
                'verbose_name_plural': 'Места и оборудования',
            },
        ),
        migrations.AddField(
            model_name='spot',
            name='equipment',
            field=models.ManyToManyField(related_name='spots', through='spots.SpotEquipment', to='spots.equipment', verbose_name='Оборудование'),
        ),
        migrations.AddField(
            model_name='spot',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spots', to='spots.location', verbose_name='Локация'),
        ),
        migrations.AddField(
            model_name='spot',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='spots', to='spots.price', verbose_name='Цена'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка отзыва')),
                ('description', models.TextField(max_length=100, verbose_name='Текст отзыва')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('booked_spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='spots.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ('id',),
            },
        ),
    ]