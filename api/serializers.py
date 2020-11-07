from rest_framework import serializers
from .models import *

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

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
            'category',
            'min_number'
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





class EquimentTestDateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquimentTestDateType
        fields = '__all__'

class EquimentSerializerTemp(serializers.ModelSerializer):

    class Meta:
        model = Equiment
        fields = '__all__'

class EquimentTestSerializer(serializers.ModelSerializer):
    equipment = EquimentSerializerTemp(many=False, required=False)
    date_type = EquimentTestDateTypeSerializer(many=False, required=False)

    class Meta:
        model = EquimentTest
        fields = '__all__'

class EquimentSerializer(serializers.ModelSerializer):
    test = EquimentTestSerializer(many=True)
    class Meta:
        model = Equiment
        fields = [
            'id',
            'name',
            'iid',
            'comment',
            'test',
            'start_work',
            'manufactor',

        ]
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
    field = SampleExpirementFieldSerializer(many=True,required=False,read_only=True)
    class Meta:
        model = SampleExpirement
        fields = '__all__'


class SampleSerializer(serializers.ModelSerializer):
    type = SampleTypeSerializer(many=False,required=False,read_only=True)
    state = SampleStateSerializer(many=False,required=False,read_only=True)
    expirement = SampleExpirementSerializer(many=True,required=False,read_only=True)
    manufacturer = ManufacturerSerializer(many=False,required=False,read_only=True)

    class Meta:
        model = Sample
        fields = '__all__'
