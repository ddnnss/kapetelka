from rest_framework import serializers
from .models import *

class ItemDifficultySerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemDifficult
        fields = ['id','name','level']

class UserMessagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['is_support_message','text']

class ShortFavoriteListSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavoriteList
        fields = '__all__'

class ShortItemSerializer(serializers.ModelSerializer):
    difficulty = ItemDifficultySerializer(many=False)
    fav_item = ShortFavoriteListSerializer(many=True)
    class Meta:
        model = Item
        fields = ['id','name','image','difficulty','fav_item']

class CategorySerializer(serializers.ModelSerializer):
    items = ShortItemSerializer(many=True)
    class Meta:
        model = Category
        fields = ['name','image','tag','items']

class FavoriteListSerializer(serializers.ModelSerializer):
    item = ShortItemSerializer(many=False)
    class Meta:
        model = FavoriteList
        fields = ['item']

class CategoryTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTag
        fields = ['id','name']


class CopyrightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Copyright
        fields = ['text']

class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        fields = ['text']

class ItemRecomendationSubBlockAItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRecomendationSubBlockAItem
        fields = ['name','value']


class ItemRecomendationSubBlockASerializer(serializers.ModelSerializer):
    recomendation_sub_block_a_items = ItemRecomendationSubBlockAItemSerializer(many=True)
    class Meta:
        model = ItemRecomendationSubBlockA
        fields = ['name','amount','recomendation_sub_block_a_items']


class ItemRecomendationBlockASerializer(serializers.ModelSerializer):
    recomendation_sub_blocks_a = ItemRecomendationSubBlockASerializer(many=True)
    class Meta:
        model = ItemRecomendationBlockA
        fields = ['name','top_text','bottom_text','image','recomendation_sub_blocks_a']


class ItemRecomendationSubBlockBSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRecomendationSubBlockB
        fields = ['text','row_number',]


class ItemRecomendationBlockBImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRecomendationBlockBImage
        fields = ['image']


class ItemRecomendationBlockBSerializer(serializers.ModelSerializer):
    recomendation_sub_blocks_b = ItemRecomendationSubBlockBSerializer(many=True)
    recomendation_sub_block_b_images = ItemRecomendationBlockBImageSerializer(many=True)
    class Meta:
        model = ItemRecomendationBlockA
        fields = ['name','top_text','bottom_text','recomendation_sub_blocks_b','recomendation_sub_block_b_images']


class ItemRecomendationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRecomendationImage
        fields = ['image','image_text']


class ItemRecomendationStepImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRecomendationStepImage
        fields = ['image']


class ItemRecomendationStepSerializer(serializers.ModelSerializer):
    step_images = ItemRecomendationStepImagesSerializer(many=True)
    class Meta:
        model = ItemRecomendationStep
        fields = ['step_number','text','step_images']


class ItemRecomendationsSerializer(serializers.ModelSerializer):
    item_recomendation_images = ItemRecomendationImageSerializer(many=True)
    class Meta:
        model = ItemRecomendation
        fields = ['top_text','bottom_text','item_recomendation_images']

class ItemLegendSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemLegend
        fields = ['name','value']

class ItemMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMaterial
        fields = ['name','value']


class ItemSerializer(serializers.ModelSerializer):
    difficulty = ItemDifficultySerializer(many=False)
    item_recomendations = ItemRecomendationsSerializer(many=True)
    item_steps = ItemRecomendationStepSerializer(many=True)
    recomendation_blocks_a = ItemRecomendationBlockASerializer(many=True)
    recomendation_blocks_b = ItemRecomendationBlockBSerializer(many=True)
    material = ItemMaterialSerializer(many=True)
    legend = ItemLegendSerializer(many=True)
    class Meta:
        model = Item
        fields = ['name',
                  'image',
                  'difficulty',
                  'video_file',
                  'video_url',
                  'is_new',
                  'material',
                  'legend',
                  'item_recomendations',
                  'recomendation_blocks_a',
                  'recomendation_blocks_b',
                  'item_steps']



