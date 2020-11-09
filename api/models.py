from django.db import models
from .services import *
from user.models import User

class Manufacturer(models.Model):
    name = models.CharField('Производитель', max_length=255, blank=False, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

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
    name = models.CharField('Категория', max_length=255, blank=False, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Категория')
    name = models.CharField('Подкатегория', max_length=255, blank=False, null=True)
    min_number = models.IntegerField(default=0)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class SortItem(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Поставщик')
    tester = models.ForeignKey(Tester, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Приемщик')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, blank=True, null=True,
                                    verbose_name='Подкатегория')
    name = models.CharField('Партия товаров', max_length=255, blank=True, null=True)
    iid = models.CharField('Серийный номер', max_length=255, blank=True, null=True)
    item_number = models.CharField('Кол-во товара', max_length=255, blank=True, null=True)
    comment = models.TextField('Комментарий', blank=True, null=True)
    good_time = models.DateField(blank=True, null=True)
    created = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партия товаров'
        verbose_name_plural = 'Партии товаров'


class Item(models.Model):
    sort = models.ForeignKey(SortItem, on_delete=models.CASCADE, blank=True, null=True,
                             verbose_name='Партия товара',related_name='items')
    status = models.BooleanField(null=True,blank=True,default=None)
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
    manufactor = models.CharField('Производитель', max_length=255, blank=True, null=True)
    start_work = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.iid} - {self.name}'

    class Meta:
        verbose_name = 'Еденица оборудования'
        verbose_name_plural = 'Еденицы оборудования'


class EquimentTestDateType(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=True)


class EquimentTest(models.Model):
    date_type = models.ForeignKey(EquimentTestDateType, on_delete=models.SET_NULL, blank=True, null=True)
    equipment = models.ForeignKey(Equiment, on_delete=models.CASCADE, blank=True, null=True, related_name='test')
    event = models.CharField('Событие', max_length=255, blank=False, null=True)
    comment = models.TextField('Комментарий', blank=True, null=True)
    date = models.DateField(blank=True, null=True)


class SampleType(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=True)


class SampleState(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=True)


class SampleExpirement(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    subject = models.CharField('На что', max_length=255, blank=False, null=True)
    weight = models.CharField('Вес', max_length=255, blank=False, null=True)
    iso = models.CharField('Стандарт', max_length=255, blank=False, null=True)


class SampleExpirementField(models.Model):
    expiriment = models.ForeignKey(SampleExpirement, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='field')
    name = models.CharField('Название', max_length=255, blank=False, null=True)

class Sample(models.Model):
    iid = models.CharField('IID', max_length=255, blank=True, null=True)
    type = models.ForeignKey(SampleType, on_delete=models.CASCADE, blank=True, null=True)
    state = models.ForeignKey(SampleState, on_delete=models.CASCADE, blank=True, null=True)
    expirement = models.ManyToManyField(SampleExpirement, blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE, blank=True, null=True)
    serial_number = models.CharField('Серийный номер', max_length=255, blank=True, null=True)
    status = models.BooleanField('Статус', default=True)
    comment = models.TextField('Комментарий', blank=True, null=True)
    date_get_sample = models.DateField(blank=True, null=True)
    date_close_sample = models.DateField(blank=True, null=True)
    arrived = models.IntegerField('Поступило',blank=True, null=True)
    done = models.IntegerField('Сделано',blank=True, null=True)
    too_small = models.IntegerField('Малый объем',blank=True, null=True)
    broken = models.IntegerField('Скисло',blank=True, null=True)
    go_bad = models.IntegerField('Непригодны',blank=True, null=True)


    def __str__(self):
        return f'{self.iid} - {self.iid}'

    class Meta:
        verbose_name = 'Образец'
        verbose_name_plural = 'Образцы'
