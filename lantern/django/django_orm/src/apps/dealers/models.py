from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models import Index


class Country(models.Model):
    country_name = models.CharField(max_length=30, blank=True, null=False)
    country_number = models.CharField(max_length=4, blank=True, null=False)

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class City(models.Model):
    city_name = models.CharField(max_length=30)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')


class Dealer(User):
    dealer_name = models.CharField(max_length=30)
    dealer_email = models.CharField(max_length=60)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.dealer_name
