from django.db import models
from .services import *
from user.models import User


class Supplier(models.Model):
    name = models.CharField('Поставщик', max_length=255, blank=False, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

class Tester(models.Model):
    name = models.CharField('Приемщик', max_length=255, blank=False, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Приемщик'
        verbose_name_plural = 'Приемщики'


class Category(models.Model):
    name = models.CharField('Категория товаров', max_length=255, blank=False, null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'

class SortItem(models.Model):
    supplier = models.ForeignKey(Supplier,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Поставщик')
    tester = models.ForeignKey(Tester,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Приемщик')
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Категория')
    name = models.CharField('Партия товаров', max_length=255, blank=True, null=True)
    iid = models.CharField('Серийный номер', max_length=255, blank=True, null=True)
    item_number = models.CharField('Кол-во товара', max_length=255, blank=True, null=True)
    comment = models.TextField('Комментарий', blank=True, null=True)
    good_time = models.DateField(blank=True,null=True)
    created = models.DateField(blank=True,null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партия товаров'
        verbose_name_plural = 'Партии товаров'





class Item(models.Model):
    sort = models.ForeignKey(SortItem,on_delete=models.CASCADE, blank=True,null=True, verbose_name='Партия товара')
    status = models.BooleanField(default=True)
    iid = models.CharField('IID', max_length=255, blank=True, null=True)
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    comment = models.TextField('Комментарий', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.name_lower = self.name.lower()
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'



class Equiment(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    iid = models.CharField('IID', max_length=255, blank=True, null=True)
    comment = models.TextField('Комментарий', blank=True, null=True)

    def __str__(self):
        return f'{self.iid} - {self.name}'

    class Meta:
        verbose_name = 'Еденица оборудования'
        verbose_name_plural = 'Еденицы оборудования'


class EquimentTest(models.Model):
    equipment = models.ForeignKey(Equiment, on_delete=models.CASCADE, blank=True, null=True, verbose_name='J,jheljdfybt')
    comment = models.TextField('Комментарий', blank=True, null=True)
    check_date = models.DateField(blank=True, null=True)
    calibrate_date = models.DateField(blank=True, null=True)
    test_date = models.DateField(blank=True, null=True)