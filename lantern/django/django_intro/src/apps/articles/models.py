from django.conf import settings
from django.db import models


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)


class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=255, verbose_name='Title', db_index=True)
    body = models.TextField(max_length=5000, verbose_name='Article body')
    tags = models.ManyToManyField(to='Tag', related_name='articles', blank=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name='articles'
    )


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'Country'


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=30)
    country_id = models.ForeignKey(
        'Country',
        on_delete=models.DO_NOTHING,
        db_column='country_id',
        blank=True, null=False
    )

    class Meta:
        managed = False
        db_table = 'City'


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=30)
    restaurant_address = models.CharField(max_length=60, blank=True, null=False)
    restaurant_number = models.CharField(max_length=13, unique=True, blank=True, null=False)
    country_id = models.ForeignKey(
        'Country',
        on_delete=models.DO_NOTHING,
        db_column='country_id',
        blank=True, null=False
    )
    city_id = models.ForeignKey(
        'City',
        on_delete=models.DO_NOTHING,
        db_column='city_id',
        blank=True, null=False
    )
    menu_id = models.ForeignKey(
        'RestaurantMenu',
        on_delete=models.DO_NOTHING,
        db_column='menu_id',
        blank=True, null=False
    )

    class Meta:
        managed = False
        db_table = 'Restaurant'


class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    menu_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Menu'


class Dish(models.Model):
    dish_id = models.AutoField(primary_key=True)
    dish_name = models.CharField(max_length=50)
    ingredients = models.TextField(blank=True, null=False)
    weight = models.IntegerField(blank=True, null=False)
    price = models.FloatField(blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'Dish'


class RestaurantMenu(models.Model):
    menu_id = models.ForeignKey(
        'Menu',
        on_delete=models.DO_NOTHING,
        db_column='menu_id',
        blank=True,
        null=False
    )
    dish_id = models.ForeignKey(
        'Dish',
        on_delete=models.DO_NOTHING,
        db_column='dish_id',
        blank=True,
        null=False
    )

    class Meta:
        managed = False
        db_table = 'Restaurant_menu'


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_first_name = models.CharField(max_length=30, blank=False, null=False)
    employee_last_name = models.CharField(max_length=30, blank=False, null=False)
    employee_birthday = models.DateField(blank=False, null=False)
    employee_phone_number = models.CharField(max_length=13, blank=False, null=False, unique=True)
    employee_address = models.CharField(max_length=50, blank=True, null=False)
    employee_salary = models.FloatField(blank=False, null=False)
    employee_work_experience = models.TextField(blank=True, null=False)
    restaurant_id = models.ForeignKey(
        'Restaurant',
        on_delete=models.DO_NOTHING,
        db_column='restaurant_id',
        blank=True,
        null=False
    )

    class Meta:
        managed = False
        db_table = 'Employee'
