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


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, required=False)

    class Meta:
        model = SubCategory
        fields = [
            'id',
            'name',
            'category'
        ]


class SortItemSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(many=False)
    tester = TesterSerializer(many=False)
    subcategory = SubCategorySerializer(many=False)

    class Meta:
        model = SortItem
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    sort = SortItemSerializer(many=False, required=False)

    class Meta:
        model = Item
        fields = '__all__'


class EquimentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equiment
        fields = '__all__'


class EquimentTestDateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquimentTestDateType
        fields = '__all__'


class EquimentTestSerializer(serializers.ModelSerializer):
    equipment = EquimentSerializer(many=False, required=False)
    date_type = EquimentTestDateTypeSerializer(many=False, required=False)

    class Meta:
        model = EquimentTest
        fields = '__all__'


class SampleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleType
        fields = '__all__'


class SampleStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleState
        fields = '__all__'


class SampleExpirementFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleExpirementField
        fields = '__all__'

class SampleExpirementSerializer(serializers.ModelSerializer):
    field = SampleExpirementFieldSerializer(many=False)
    class Meta:
        model = SampleExpirement
        fields = '__all__'


class SampleSerializer(serializers.ModelSerializer):
    type = SampleTypeSerializer(many=False)
    state = SampleStateSerializer(many=False)
    expirement = SampleExpirementSerializer(many=True)

    class Meta:
        model = Sample
        fields = '__all__'
