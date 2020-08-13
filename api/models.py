from django.db import models
from pytils.translit import slugify
from .services import *
from user.models import User
class CategoryTag(models.Model):

    name = models.CharField('Название фильтра', max_length=255, blank=False, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    tag = models.ForeignKey(CategoryTag, on_delete=models.SET_NULL, blank=True, null=True, related_name='tags',
                                 verbose_name='Фильтр')
    name = models.CharField('Название категории', max_length=255, blank=False, null=True)
    image = models.ImageField('Изображение (xxx x xxx)', upload_to='category/images/', blank=False, null=True)

    def __str__(self):
        return self.name



class ItemMaterial(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    value = models.CharField('Значение', max_length=255, blank=False, null=True)
    def __str__(self):
        return self.name

class ItemLegend(models.Model):
    name = models.CharField('Название условного обозначения', max_length=255, blank=False, null=True)
    value = models.CharField('Значение', max_length=255, blank=False, null=True)
    def __str__(self):
        return self.name

class ItemDifficult(models.Model):
    name = models.CharField('Название уровня сложности', max_length=255, blank=False, null=True)
    level = models.IntegerField('Уровень сложности (Цифра)', default=1)
    def __str__(self):
        return self.name



class Item(models.Model):
    author = models.CharField('Автор', max_length=255, blank=True, null=True)
    material = models.ManyToManyField(ItemMaterial, blank=True,related_name='materials',verbose_name='Материалы')
    legend = models.ManyToManyField(ItemLegend, blank=True,related_name='legends',verbose_name='Условные обозначения')
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, blank=True,null=True,
                                 related_name='items',verbose_name='Относится')
    difficulty = models.ForeignKey(ItemDifficult,on_delete=models.SET_NULL, blank=True,null=True,
                                   related_name='difficulty',verbose_name='Сложность')
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    name_lower = models.CharField('Название', max_length=255, blank=False, null=True,editable=False)
    video_file = models.FileField('Видео локальный файл', max_length=255, blank=True, null=True)
    video_url = models.CharField('Видео ссылка', max_length=255, blank=True, null=True)
    image = models.ImageField('Изображение (xxx x xxx)', upload_to='item/images/', blank=False, null=True)
    is_new = models.BooleanField('Новинка ?', default=False)

    def save(self, *args, **kwargs):
        self.name_lower = self.name.lower()
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class ItemRecomendation(models.Model):
    item = models.ForeignKey(Item,on_delete=models.SET_NULL, blank=True,null=True,
                             related_name='item_recomendations',verbose_name='Относится к')
    top_text = models.TextField('Верхний текст раздела практические рекомендации', max_length=255, blank=True,
                                null=True)
    bottom_text = models.TextField('Нижний текст раздела практические рекомендации', max_length=255, blank=True,
                                   null=True)
    def __str__(self):
        return f'Раздел практические рекомендации для {self.item.name}'

class ItemRecomendationImage(models.Model):
    item_recomendation = models.ForeignKey(ItemRecomendation,on_delete=models.SET_NULL, blank=False, null=True,
                                           related_name='item_recomendation_images', verbose_name='Относится к')
    order_num = models.IntegerField('Порядок вывода', default=1)
    image = models.ImageField('Изображение (xxx x xxx)', upload_to='item/recomendation/images/', blank=False, null=True)
    image_text = models.CharField('Текст на картинку',max_length=30, blank=True,null=True)

    def __str__(self):
        return f'Иображение раздел практические рекомендации для {self.item_recomendation.id}'


class ItemRecomendationBlockA(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    item = models.ForeignKey(Item,on_delete=models.SET_NULL, blank=False,null=True,
                             related_name='recomendation_blocks_a',
                             verbose_name='Относится к')
    top_text = models.TextField('Верхний текст раздела', max_length=255, blank=True,
                                null=True)
    bottom_text = models.TextField('Нижний текст раздела', max_length=255, blank=True,
                                   null=True)
    image = models.ImageField('Изображение (xxx x xxx)', upload_to='item/sub_block_a/images/', blank=False, null=True)
    def __str__(self):
        return f'Раздел А для {self.item.name}'

class ItemRecomendationSubBlockA(models.Model):
    block_a = models.ForeignKey(ItemRecomendationBlockA,on_delete=models.SET_NULL, blank=False, null=True,
                                related_name='recomendation_sub_blocks_a',
                                verbose_name='Относится к')
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    amount = models.IntegerField('Количество',default=1)

    def __str__(self):
        return f'Под раздел А для {self.block_a.name}'

class ItemRecomendationSubBlockAItem(models.Model):
    block_a = models.ForeignKey(ItemRecomendationSubBlockA,on_delete=models.SET_NULL, blank=False, null=True,
                                related_name='recomendation_sub_block_a_items',
                                verbose_name='Относится к')
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    value = models.CharField('Значение', max_length=255, blank=False, null=True)

    def __str__(self):
        return f'Запись для под-раздела А для {self.block_a.name}'


class ItemRecomendationBlockB(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    item = models.ForeignKey(Item,on_delete=models.SET_NULL, blank=False,null=True,
                             related_name='recomendation_blocks_b',verbose_name='Относится к')
    top_text = models.TextField('Верхний текст раздела', max_length=255, blank=True,
                                null=True)
    bottom_text = models.TextField('Нижний текст раздела', max_length=255, blank=True,
                                   null=True)

    def __str__(self):
        return f'Раздел В для {self.item.name}'

class ItemRecomendationSubBlockB(models.Model):
    block_b = models.ForeignKey(ItemRecomendationBlockB,on_delete=models.SET_NULL, blank=False, null=True,
                                related_name='recomendation_sub_blocks_b',
                                verbose_name='Относится к')
    text = models.TextField('Текст', max_length=255, blank=False, null=True)
    row_number = models.IntegerField('Номер ряда',default=1)

    def __str__(self):
        return f'Под раздел B для {self.block_b.name}'

class ItemRecomendationBlockBImage(models.Model):
    block_b = models.ForeignKey(ItemRecomendationBlockB,on_delete=models.SET_NULL, blank=False, null=True,
                                related_name='recomendation_sub_block_b_images',
                                verbose_name='Относится к')
    image = models.ImageField('Изображение (xxx x xxx)', upload_to='item/sub_block_b/images/', blank=False, null=True)

    def __str__(self):
        return f'Под раздел B для {self.block_b.id}'

class ItemRecomendationStep(models.Model):
    step_number = models.IntegerField('Номер шага', blank=True,null=True)
    item = models.ForeignKey(Item,on_delete=models.SET_NULL, blank=False,null=True,
                             related_name='item_steps',verbose_name='Относится к')
    text = models.TextField('Верхний текст раздела', max_length=255, blank=True,
                                null=True)
    def __str__(self):
        return f'Блок шаг для {self.item.name}'

class ItemRecomendationStepImage(models.Model):
    step = models.ForeignKey(ItemRecomendationStep,on_delete=models.SET_NULL, blank=False,null=True,
                             related_name='step_images',verbose_name='Относится к')
    image = models.ImageField('Изображение (xxx x xxx)', upload_to='item/step/images/', blank=False, null=True)
    def __str__(self):
        return f'Блок шаг для {self.step.id}'


class Copyright(models.Model):
    text=models.TextField('Copyright текст',blank=True,null=True)

    def __str__(self):
        return f'Copyright текст'


class Terms(models.Model):
    text = models.TextField('Terms of user agreement текст', blank=True, null=True)

    def __str__(self):
        return f'Terms of user agreement текст'

class FavoriteList(models.Model):
    item = models.ForeignKey(Item,on_delete=models.SET_NULL, blank=False,null=True,
                             verbose_name='Относится к',related_name='fav_item')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True,
                              verbose_name='Относится к')
    def __str__(self):
        return f'Избранное для {self.user.id}'


class LastOpen(models.Model):
    item = models.ForeignKey(Item,on_delete=models.SET_NULL, blank=False,null=True,
                             verbose_name='Относится к')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True,
                              verbose_name='Относится к')
    def __str__(self):
        return f'Последний посмотренный для {self.user.id}'



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True,
                             verbose_name='Относится к')
    is_support_message = models.BooleanField(default=False)
    text = models.TextField(blank=True,null=True)