from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework import generics


class ItemDificultySearch(generics.RetrieveAPIView):
    queryset = Item.objects.filter()
    serializer_class = ItemSerializer


class ItemDificultyAll(generics.ListAPIView):
    queryset = ItemDifficult.objects.all()
    serializer_class = ItemDifficultySerializer


class ItemDetail(generics.RetrieveAPIView):
    queryset = Item.objects.filter()
    serializer_class = ItemSerializer

class Categories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ItemsList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ShortItemSerializer


class SearchItem(APIView):
    def get(self, request,query):
        qs = Item.objects.filter(name_lower__contains=query.lower())
        serializer = ShortItemSerializer(qs, many=True)
        return Response(serializer.data)


class Tags(generics.ListAPIView):
    queryset = CategoryTag.objects.all()
    serializer_class = CategoryTagSerializer


class CategoriesByTag(APIView):
    def get(self, request,id):
        qs = Category.objects.filter(tag=id)
        serializer = CategorySerializer(qs, many=True)
        return Response(serializer.data)


class UserFavoriteList(APIView):
    def get(self, request):
        try:
            qs = FavoriteList.objects.filter(user=request.user)
            serializer = FavoriteListSerializer(qs, many=True)
            return Response(serializer.data)
        except:
            return Response(status=403)


class UserFavoriteAdd(APIView):
    def post(self, request,id):
        item,created = FavoriteList.objects.get_or_create(user=request.user, item_id=id)
        if not created:
            item.delete()
            return Response(status=200)
        else:
            return Response(status=201)


class UserFavoriteClear(APIView):
    def post(self, request):
        FavoriteList.objects.filter(user=request.user).delete()
        return Response(status=200)


class UserLastSeenList(APIView):
    def get(self, request):
        qs = LastOpen.objects.filter(user=request.user)
        serializer = FavoriteListSerializer(qs, many=True)
        return Response(serializer.data)

class UserMessagesList(APIView):
    def get(self, request):
        qs = Message.objects.filter(user=request.user)
        serializer = UserMessagesSerializer(qs, many=True)
        return Response(serializer.data)

class UserMessageAdd(APIView):
    def post(self, request):
        Message.objects.create(user=request.user,text=request.data['text'])
        return Response(status=201)


class UserLastSeenListUpdate(APIView):
    def post(self, request,id):
        try:
            qs = LastOpen.objects.get(user=request.user)
            qs.item = Item.objects.get(id=id)
            qs.save()
            return Response(status=200)
        except:
            LastOpen.objects.create(user=request.user,item_id=id)
            return Response(status=201)


class CopyrightText(APIView):
    def get(self,request):
        qs = Copyright.objects.filter(id=1)
        serializer = CopyrightSerializer(qs,many=False)
        return Response(serializer.data)

class TermsText(APIView):
    def get(self, request):
        qs = Terms.objects.filter(id=1)
        serializer = TermsSerializer(qs, many=False)
        return Response(serializer.data)