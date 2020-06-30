from django.contrib import admin
from django.utils.safestring import mark_safe
from apps.cars.models import Car, Color, CarModel, CarBrand


@admin.register(Car)
class Car(admin.ModelAdmin):
    list_display = ('model', 'extra_title',)


@admin.register(Color)
class Color(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(CarModel)
class CarMode(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(CarBrand)
class CarBrand(admin.ModelAdmin):
    list_display = ('name', '_image')

    def _image(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" style="height: 50px">')
        return 'Not Found image'
