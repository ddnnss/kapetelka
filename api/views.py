from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework import generics

class ItemDetail(generics.RetrieveAPIView):
    queryset = Item.objects.filter()
    serializer_class = ItemSerializer

class Categories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class Tags(generics.ListAPIView):
    queryset = CategoryTag.objects.all()
    serializer_class = CategoryTagSerializer




class CategoriesByTag(APIView):
    def get(self, request,id):
        qs = Category.objects.filter(tag=id)
        serializer = CategorySerializer(qs, many=True)
        return Response(serializer.data)

class UserFavoriteList(APIView):
    def get(self, request,pk):
        qs = FavoriteList.objects.filter(user_id=pk)
        serializer = FavoriteListSerializer(qs, many=True)
        return Response(serializer.data)

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