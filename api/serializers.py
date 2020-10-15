from rest_framework import serializers
from .models import *

class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'


class TesterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tester
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class SortItemSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(many=False)
    tester = TesterSerializer(many=False)
    category = CategorySerializer(many=False)

    class Meta:
        model = SortItem
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    sort = SortItemSerializer(many=False,required=False)

    class Meta:
        model = Item
        fields = '__all__'

class EquimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equiment
        fields = '__all__'

class EquimentTestSerializer(serializers.ModelSerializer):
    equipment = EquimentSerializer(many=False,required=False)

    class Meta:
        model = EquimentTest
        fields = '__all__'
