from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework import generics
from PIL import Image, ImageDraw,ImageFont


class Suppliers(generics.ListAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()

class SupplierCreate(generics.CreateAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()

class SupplierDelete(generics.DestroyAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()

class SupplierEdit(generics.UpdateAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()

#----------------

class Testers(generics.ListAPIView):
    serializer_class = TesterSerializer
    queryset = Tester.objects.all()

class TesterCreate(generics.CreateAPIView):
    serializer_class = TesterSerializer
    queryset = Tester.objects.all()

class TesterDelete(generics.DestroyAPIView):
    serializer_class = TesterSerializer
    queryset = Tester.objects.all()

class TesterEdit(generics.UpdateAPIView):
    serializer_class = TesterSerializer
    queryset = Tester.objects.all()

#----------------

class Categories(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryCreate(generics.CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryDelete(generics.DestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryEdit(generics.UpdateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

#----------------

class SubCategories(generics.ListAPIView):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()

class SubCategoryCreate(APIView):
    def post(self,request):
        print(request.data)
        SubCategory.objects.create(name=request.data['name'],category_id=request.data['category'])
        return Response (status=200)

class SubCategoryDelete(generics.DestroyAPIView):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()

class SubCategoryEdit(generics.UpdateAPIView):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()

#----------------

class ItemCreate(APIView):
    def post(self,request):
        print(request.data)
        data = request.data
        cat = Category.objects.get(id=data['category'])
        print(cat)
        item_sort = SortItem.objects.create(
            subcategory_id=int(data['subcategory']),
            supplier_id=int(data['supplier']),
            tester_id=int(data['tester']),
            comment=data['comment'],
            iid=data['iid'],
            good_time=data['good_time'],
            created=data['created_at'],
            item_number=data['number'],

            name=f'Партия : {data["name"]}'

        )
        for i in range(1,int(data['number'])+1):
            Item.objects.create(iid=f"{i:03d}",
                                name=data["name"],
                                sort=item_sort
                                )

        return Response (status=200)

class ItemGetImage(APIView):
    def post(self,request):
        print(request.data)
        item = Item.objects.get(id=int(request.data['id']))
        print(item)
        img = Image.new('RGB', (500, 270), color='white')
        name = f'{item.sort.iid}-{item.iid}.png'
        font = ImageFont.truetype(font='font.ttf', size=20)
        d = ImageDraw.Draw(img)
        d.text((10, 10), item.name, font=font, fill=(0, 0, 0))
        d.text((10, 40), f'Категория: {item.sort.subcategory.category.name}', font=font, fill=(0, 0, 0))
        d.text((10, 70), f'Подкатегория: {item.sort.subcategory.name}', font=font, fill=(0, 0, 0))
        d.text((10, 100), f'Дата приема: {item.sort.created}', font=font, fill=(0, 0, 0))
        d.text((10, 130), f'Срок годности: {item.sort.good_time}', font=font, fill=(0, 0, 0))
        d.text((10, 160), f'Серия: {item.sort.iid}-{item.iid}', font=font, fill=(0, 0, 0))
        img.save(f'media/{name}')

        return Response({'path':f'media/{name}'},status=200)

class ItemUpdate(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class Items(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

#----------------

class Sorts(generics.ListAPIView):
    queryset = SortItem.objects.all()
    serializer_class = SortItemSerializer

class SortDelete(generics.DestroyAPIView):
    serializer_class = SortItemSerializer
    queryset = SortItem.objects.all()

#----------------

class Equips(generics.ListAPIView):
    queryset = Equiment.objects.all()
    serializer_class = EquimentSerializer

class EquipCreate(generics.CreateAPIView):
    queryset = Equiment.objects.all()
    serializer_class = EquimentSerializer

class EquipDelete(generics.DestroyAPIView):
    queryset = Equiment.objects.all()
    serializer_class = EquimentSerializer

class EquipEdit(generics.UpdateAPIView):
    queryset = Equiment.objects.all()
    serializer_class = EquimentSerializer

#----------------

class EquipTests(generics.ListAPIView):
    queryset = EquimentTest.objects.all()
    serializer_class = EquimentTestSerializer

class EquipTestsCreate(APIView):
    def post(self,request):
        print(request.data)
        data=request.data
        EquimentTest.objects.create(equipment_id=int(data['equipment']),
                                    date_type_id=data['date_type'],
                                    date=data['date'],
                                    event=data['event'],
                                    comment=data['comment'],
                                    )
        return Response(status=200)
    # serializer_class = EquimentTestSerializer
    # queryset = EquimentTest.objects.all()

class EquipTestDateTypes(generics.ListAPIView):
    queryset = EquimentTestDateType.objects.all()
    serializer_class = EquimentTestDateTypeSerializer

class EquipTestDateTypeCreate(generics.CreateAPIView):
    queryset = EquimentTestDateType.objects.all()
    serializer_class = EquimentTestDateTypeSerializer

class EquipTestDateTypeDelete(generics.DestroyAPIView):
    queryset = EquimentTestDateType.objects.all()
    serializer_class = EquimentTestDateTypeSerializer

class EquipTestDateTypeEdit(generics.UpdateAPIView):
    queryset = EquimentTestDateType.objects.all()
    serializer_class = EquimentTestDateTypeSerializer

#----------------




