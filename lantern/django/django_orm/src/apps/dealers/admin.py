from django.contrib import admin

from apps.dealers.models import Country, City, Dealer


@admin.register(Country)
class Country(admin.ModelAdmin):
    list_display = ('country_name',)


@admin.register(City)
class City(admin.ModelAdmin):
    list_display = ('city_name',)


@admin.register(Dealer)
class Dealer(admin.ModelAdmin):
    list_display = ('dealer_name',)
