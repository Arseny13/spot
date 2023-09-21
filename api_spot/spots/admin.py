from django.contrib import admin


from .models import (Category, Equipment, Favorite, ExtraPhoto,
                     Location, Order, Price, Review, Spot)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(ExtraPhoto)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('location', 'id', 'image', 'description')


class ImageInline(admin.TabularInline):
    model = ExtraPhoto
    extra = 0
    min_num = 1


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'street',
        'house_number',
        'apartment_number',
        'latitude',
        'longitude',
    )
    list_filter = ('street', 'house_number')
    search_fields = ('street', 'house_number')
    inlines = [ImageInline]


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('price', 'discount', 'description')
    search_fields = ('spot', )


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'location')


@admin.register(Spot)
class SpotAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'location', 'category', 'description')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'booked_spot',
        'pub_date',
    )
    readonly_fields = ('pub_date',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "spot",
        "user",
    )
    empty_value_display = "-пусто)))-"
    list_display = ('pk', 'spot', 'user', 'start_time', 'end_time')
    empty_value_display = '-пусто)))-'


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk', 'description')
