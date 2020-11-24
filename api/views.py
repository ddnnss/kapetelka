from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework import generics
from PIL import Image, ImageDraw,ImageFont
from datetime import timedelta,datetime


class Manufacturers(generics.ListAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()

class ManufacturerCreate(generics.CreateAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()

class ManufacturerDelete(generics.DestroyAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()

class ManufacturerEdit(generics.UpdateAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()

#----------------

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

class SubCategoryCheckAll(APIView):
    def get(self, request):
        subcats = SubCategory.objects.all()
        responce = []
        for subcat in subcats:
            for sort in subcat.sortitem_set.all():
                items = Item.objects.filter(sort=sort, status=True)
                print(len(items))
                if len(items) < subcat.min_number:
                    responce.append({
                        'id': subcat.id,
                        'name': sort.name
                    })

        return Response(responce, status=200)
class SubCategoryCheck(APIView):
    def get(self,request,pk):
        print(pk)
        subcat = SubCategory.objects.get(id=pk)
        responce=[]

        for sort in subcat.sortitem_set.all():
            items = Item.objects.filter(sort=sort,status=True)
            print(len(items))
            if len(items) < subcat.min_number   :
                responce.append({
                    'id':sort.id+subcat.id,
                    'name':sort.name
                })


        return Response(responce,status=200)

class SubCategoryCreate(APIView):
    def post(self,request):
        print(request.data)
        SubCategory.objects.create(name=request.data['name'],
                                   category_id=request.data['category'],
                                   min_number=request.data['min_number'])
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
            tester_id=int(data['tester']) if data['tester'] != '' else None,
            comment=data['comment'],
            iid=data['iid'] if data['iid'] != '' else None,
            good_time=data['good_time'] if data['good_time'] != '' else None,
            created=data['created_at'] if data['created_at'] != '' else None,
            item_number=data['number'],

            name=f'{data["name"]}'

        )
        for i in range(1,int(data['number'])+1):
            Item.objects.create(iid=f"{i:03d}",
                                name=data["name"],
                                sort=item_sort,
                                status=data['status']
                                )

        return Response (status=200)

class ItemChangeStatus(APIView):
    def post(self,request,pk):
        print(request.data)
        items = Item.objects.filter(sort_id=pk)
        for item in items:
            if request.data['status'] == 'Списан':
                item.status=False
            if request.data['status'] == 'Ожидание':
                item.status=None
            if request.data['status'] == 'В наличии':
                item.status = True
            item.save()

        return Response(status=200)


class ItemGetImage(APIView):
    def post(self,request):
        print(request.data)
        item = Item.objects.get(id=int(request.data['id']))
        print(item)
        img = Image.new('RGB', (500, 330), color='white')
        name = f'{item.sort.iid}-{item.iid}.png'
        font = ImageFont.truetype(font='Gilroy-Regular.ttf', size=20)
        fontBold = ImageFont.truetype(font='Gilroy-Bold.ttf', size=20)
        d = ImageDraw.Draw(img)
        d.text((10, 10), 'Название:', font=fontBold, fill=(0, 0, 0))
        d.text((200, 10), item.name, font=font, fill=(0, 0, 0))

        d.text((10, 40), 'Категория: ', font=fontBold, fill=(0, 0, 0))
        d.text((200, 40), item.sort.subcategory.category.name, font=font, fill=(0, 0, 0))

        d.text((10, 70), 'Подкатегория: ', font=fontBold, fill=(0, 0, 0))
        d.text((200, 70), item.sort.subcategory.name, font=font, fill=(0, 0, 0))

        d.text((10, 100), 'Поставщик: ', font=fontBold, fill=(0, 0, 0))
        d.text((200, 100), f'{item.sort.supplier.name }', font=font, fill=(0, 0, 0))

        d.text((10, 130), 'Приемщик: ', font=fontBold, fill=(0, 0, 0))
        d.text((200, 130), f'{item.sort.tester.name if item.sort.tester  else "НЕ УКАЗАНО"}', font=font, fill=(0, 0, 0))

        d.text((10, 170), 'Дата приема: ', font=fontBold, fill=(0, 0, 0))
        d.text((200, 170), f'{item.sort.created.strftime("%d/%m/%Y") if item.sort.created  else "НЕ УКАЗАНО"}', font=font, fill=(0, 0, 0))

        d.text((10, 200), 'Срок годности: ', font=fontBold, fill=(0, 0, 0))
        d.text((200, 200), f'{item.sort.good_time.strftime("%d/%m/%Y") if item.sort.good_time  else "НЕ УКАЗАНО"}', font=font, fill=(0, 0, 0))

        d.text((10, 230), 'Серийный номер: ', font=fontBold, fill=(0, 0, 0))
        d.text((200, 230), item.iid, font=font, fill=(0, 0, 0))

        d.text((10, 260), 'ID Партии: ', font=fontBold, fill=(0, 0, 0))
        d.text((200, 260), f'{item.sort.iid if item.sort.iid  else "НЕ УКАЗАНО"}', font=font, fill=(0, 0, 0))

        d.text((10, 290), 'ID Товара: ', font=fontBold, fill=(0, 0, 0))
        d.text((200, 290), f'{item.id}', font=font, fill=(0, 0, 0))


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


# class Sorts(APIView):
#     def get(self, request):
#         queryset = SortItem.objects.all()
#         serializer = SortItemSerializer(queryset)
#         return Response(serializer.data, status=200)

class SortDelete(generics.DestroyAPIView):
    serializer_class = SortItemSerializer
    queryset = SortItem.objects.all()

class SortUpdate(APIView):
    def post(self, request, pk):
        print(request.data)
        sort=SortItem.objects.get(id=pk)
        if request.data.get('status'):
            items = Item.objects.filter(sort=sort)
            for item in items:
                if request.data['status'] == 'Списан':
                    item.status = False
                if request.data['status'] == 'Ожидание':
                    item.status = None
                if request.data['status'] == 'В наличии':
                    item.status = True
                item.save()
        sort.good_time = request.data['good_time']
        sort.created = request.data['created']
        sort.iid = request.data['iid']
        sort.comment = request.data['comment']
        sort.save()

        return Response(status=200)


class SortCheck(APIView):
    def get(self, request):
        sorts = SortItem.objects.all()
        responce = []
        for sort in sorts:
            print(sort.good_time < datetime.now().date() +timedelta(days=7))
            if sort.good_time < datetime.now().date() +timedelta(days=7) and not sort.good_time == datetime.now().date():
                responce.append({
                    'id':sort.id,
                    'type':'warning',
                    'name': sort.name,
                    'date':sort.good_time
                })
            if sort.good_time == datetime.now().date():
                responce.append({
                    'id': sort.id,
                    'type': 'error',
                    'name': sort.name,
                    'date': 'сегодня'
                })

        return Response(responce, status=200)
#----------------

class Equips(generics.ListAPIView):
    queryset = Equiment.objects.all()
    serializer_class = EquimentSerializer

class EquipCreate(APIView):
    def post(self, request):
        print(request.data)
        data = request.data
        Equiment.objects.create(
            name=data['name'],
            iid=data['iid'],
            comment=data['comment'],
            start_work=data['start_work'],
            manufactor=data['manufactor']

                                    )
        return Response(status=200)
    # queryset = Equiment.objects.all()
    # serializer_class = EquimentSerializer

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

class EquipTestDelete(generics.DestroyAPIView):
    serializer_class = EquimentTestSerializer
    queryset = EquimentTest.objects.all()

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


class EquipGetImage(APIView):
    def post(self,request):
        print(request.data)
        eqip = Equiment.objects.get(id=int(request.data['id']))
        print(eqip)

        img = Image.new('RGB', (500, 270), color='white')
        name = f'eqip{eqip.id}.png'
        font = ImageFont.truetype(font='Gilroy-Regular.ttf', size=20)
        fontBold = ImageFont.truetype(font='Gilroy-Bold.ttf', size=20)
        d = ImageDraw.Draw(img)
        d.text((10, 10), 'С/Н:', font=fontBold, fill=(0, 0, 0))
        d.text((230, 10), f'{eqip.iid}', font=font, fill=(0, 0, 0))

        d.text((10, 40), 'Название:', font=fontBold, fill=(0, 0, 0))
        d.text((10, 70), f'{eqip.name}', font=font, fill=(0, 0, 0))

        d.text((10, 100), 'Комментарий:', font=fontBold, fill=(0, 0, 0))
        d.text((230, 100), f'{eqip.comment}', font=font, fill=(0, 0, 0))

        d.text((10, 130), 'Ввод в эксплуатацию:', font=fontBold, fill=(0, 0, 0))
        d.text((230, 130), f'{eqip.start_work.strftime("%d/%m/%Y")}', font=font, fill=(0, 0, 0))

        d.text((10, 160), 'Производитель:', font=fontBold, fill=(0, 0, 0))
        d.text((10, 190), f'{eqip.manufactor}', font=font, fill=(0, 0, 0))


        img.save(f'media/{name}')

        return Response({'path':f'media/{name}'},status=200)
#----------------

class SampleTypes(generics.ListAPIView):
    serializer_class = SampleTypeSerializer
    queryset = SampleType.objects.all()

class SampleTypeCreate(generics.CreateAPIView):
    serializer_class = SampleTypeSerializer
    queryset = SampleType.objects.all()

class SampleTypeDelete(generics.DestroyAPIView):
    serializer_class = SampleTypeSerializer
    queryset = SampleType.objects.all()

class SampleTypeEdit(generics.UpdateAPIView):
    serializer_class = SampleTypeSerializer
    queryset = SampleType.objects.all()

#----------------

class SampleStates(generics.ListAPIView):
    serializer_class = SampleStateSerializer
    queryset = SampleState.objects.all()

class SampleStateCreate(generics.CreateAPIView):
    serializer_class = SampleStateSerializer
    queryset = SampleState.objects.all()

class SampleStateDelete(generics.DestroyAPIView):
    serializer_class = SampleStateSerializer
    queryset = SampleState.objects.all()

class SampleStateEdit(generics.UpdateAPIView):
    serializer_class = SampleStateSerializer
    queryset = SampleState.objects.all()

#----------------

class SampleExpiriments(generics.ListAPIView):
    serializer_class = SampleExpirementSerializer
    queryset = SampleExpirement.objects.all()

class SampleExpirimentCreate(APIView):
    def post(self,request):
        print(request.data)
        newItem = SampleExpirement.objects.create(
            name=request.data['name'],
            subject=request.data['subject'],
            weight=request.data['weight'],
            iso=request.data['iso'],
        )
        for field in request.data['field']:
            print(field['value'])
            if field['value'] != '':
                SampleExpirementField.objects.create(
                    expiriment=newItem,
                    name=field['value']
                )

        return Response(status=200)

    # serializer_class = SampleExpirementSerializer
    # queryset = SampleExpirement.objects.all()

class SampleExpirimentDelete(generics.DestroyAPIView):
    serializer_class = SampleExpirementSerializer
    queryset = SampleExpirement.objects.all()

class SampleExpirimentEdit(generics.UpdateAPIView):
    serializer_class = SampleExpirementSerializer
    queryset = SampleExpirement.objects.all()

#----------------


class Samples(generics.ListAPIView):
    serializer_class = SampleSerializer
    queryset = Sample.objects.all()

class SampleCreate(APIView):
    def post(self,request):
        print(request.data)
        items = Sample.objects.filter(date_get_sample=request.data['date_get_sample'])
        newItem = Sample.objects.create(
            iid=f"{len(items)+1:04d}",
            type_id=request.data['type'],
            state_id=request.data['state'],
            manufacturer_id=request.data['manufacturer'],
            serial_number=request.data['serial_number'],
            date_get_sample=request.data['date_get_sample'],
            comment=request.data['comment'],
            arrived=request.data['arrived'],
            done=request.data['done'],
            too_small=request.data['too_small'],
            broken=request.data['broken'],
            go_bad=request.data['go_bad'],


        )
        for ex in request.data['expirement']:
            exp = SampleExpirement.objects.get(id=ex)
            newItem.expirement.add(exp)
        return Response(status=200)
    # serializer_class = SampleSerializer
    # queryset = Sample.objects.all()

class SampleDelete(generics.DestroyAPIView):
    serializer_class = SampleSerializer
    queryset = Sample.objects.all()

class SampleEdit(generics.UpdateAPIView):
    serializer_class = SampleSerializer
    queryset = Sample.objects.all()

class SampleGetImage(APIView):
    def post(self,request):
        print(request.data)
        sample = Sample.objects.get(id=int(request.data['id']))
        print(sample)
        expririments = SampleExpirement.objects.filter(sample=sample)
        print(len(expririments))
        img = Image.new('RGB', (500, 270+ (len(expririments) + 50)), color='white')
        name = f'A{sample.date_get_sample}RUSAPROPL{sample.iid}.png'
        print(name)
        font = ImageFont.truetype(font='Gilroy-Regular.ttf', size=20)
        fontBold = ImageFont.truetype(font='Gilroy-Bold.ttf', size=20)
        d = ImageDraw.Draw(img)
        d.text((10, 10), 'Код', font=fontBold, fill=(0, 0, 0))
        d.text((200, 10),  f'A{sample.date_get_sample}RUSAPROPL{sample.iid}', font=font, fill=(0, 0, 0))

        d.text((10, 40), 'Тип:', font=fontBold, fill=(0, 0, 0))
        d.text((200, 40), f'{sample.type.name}', font=font, fill=(0, 0, 0))

        d.text((10, 70), 'Состояние:', font=fontBold, fill=(0, 0, 0))
        d.text((200, 70), f'{sample.state.name}', font=font, fill=(0, 0, 0))

        d.text((10, 100), 'С/Н:', font=fontBold, fill=(0, 0, 0))
        d.text((200, 100), f'{sample.serial_number}', font=font, fill=(0, 0, 0))

        d.text((10, 130), 'Дата получения:', font=fontBold, fill=(0, 0, 0))
        d.text((200, 130), f'{sample.date_get_sample.strftime("%d/%m/%Y")}', font=font, fill=(0, 0, 0))

        d.text((10, 160), 'Испытания:', font=fontBold, fill=(0, 0, 0))
        j = 1
        ii = 30
        for i in expririments:
            d.text((10, 160+ii), f'{j}.', font=fontBold, fill=(0, 0, 0))
            d.text((30, 160+ii), f'{i.iso} {i.subject} {i.weight}', font=font, fill=(0, 0, 0))
            ii += 30
            j += 1

        img.save(f'media/{name}')

        return Response({'path':f'media/{name}'},status=200)

#----------------
