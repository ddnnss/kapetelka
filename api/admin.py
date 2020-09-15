from django.contrib import admin
from .models import *


class ItemRecomendationInline(admin.TabularInline):
    model = ItemRecomendation
    extra = 0

class ItemRecomendationImageInline(admin.TabularInline):
    model = ItemRecomendationImage
    extra = 0

# block A
class ItemRecomendationBlockAInline(admin.TabularInline):
    model = ItemRecomendationBlockA
    extra = 0

class ItemRecomendationSubBlockAInline(admin.TabularInline):
    model = ItemRecomendationSubBlockA
    extra = 0

class ItemRecomendationSubBlockAItemInline(admin.TabularInline):
    model = ItemRecomendationSubBlockAItem
    extra = 0

# block B
class ItemRecomendationBlockBInline(admin.TabularInline):
    model = ItemRecomendationBlockB
    extra = 0

class ItemRecomendationSubBlockBInline(admin.TabularInline):
    model = ItemRecomendationSubBlockB
    extra = 0

class ItemRecomendationBlockBImageInline(admin.TabularInline):
    model = ItemRecomendationBlockBImage
    extra = 0

class ItemRecomendationStepInline(admin.TabularInline):
    model = ItemRecomendationStep
    extra = 0

class ItemRecomendationStepImageInline(admin.TabularInline):
    model = ItemRecomendationStepImage
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemRecomendationInline,ItemRecomendationBlockAInline,
               ItemRecomendationBlockBInline,ItemRecomendationStepInline]
    class Meta:
        model = Item

class ItemRecomendationAdmin(admin.ModelAdmin):
    inlines = [ItemRecomendationImageInline]
    class Meta:
        model = ItemRecomendation


class ItemRecomendationStepAdmin(admin.ModelAdmin):
    inlines = [ItemRecomendationStepImageInline]
    class Meta:
        model = ItemRecomendationStep


class ItemRecomendationBlockAAdmin(admin.ModelAdmin):
    inlines = [ItemRecomendationSubBlockAInline]
    class Meta:
        model = ItemRecomendationBlockA

class ItemRecomendationBlockBAdmin(admin.ModelAdmin):
    inlines = [ItemRecomendationSubBlockBInline,ItemRecomendationBlockBImageInline]
    class Meta:
        model = ItemRecomendationBlockB

class ItemRecomendationSubBlockAAdmin(admin.ModelAdmin):
    inlines = [ItemRecomendationSubBlockAItemInline]
    class Meta:
        model = ItemRecomendationSubBlockA



admin.site.register(Category)
admin.site.register(CategoryTag)
admin.site.register(Item,ItemAdmin)
admin.site.register(ItemLegend)
admin.site.register(ItemDifficult)
admin.site.register(ItemMaterial)
admin.site.register(ItemRecomendation,ItemRecomendationAdmin)
# admin.site.register(ItemRecomendationImage)
admin.site.register(ItemRecomendationBlockA,ItemRecomendationBlockAAdmin)
admin.site.register(ItemRecomendationBlockB,ItemRecomendationBlockBAdmin)
admin.site.register(ItemRecomendationStep,ItemRecomendationStepAdmin)
# admin.site.register(ItemRecomendationStepImage)
admin.site.register(ItemRecomendationSubBlockA,ItemRecomendationSubBlockAAdmin)
# admin.site.register(ItemRecomendationSubBlockAItem)
# admin.site.register(ItemRecomendationSubBlockB)
# admin.site.register(ItemRecomendationBlockBImage)
admin.site.register(Copyright)
admin.site.register(Terms)
admin.site.register(FavoriteList)
admin.site.register(Message)
