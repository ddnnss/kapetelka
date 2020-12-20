import json

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import *
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework import generics
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
from django.template import Context
from django.template.loader import get_template

class GetUser(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user



class UpdateUser(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            if request.data.get('email'):
                request.user.auth_token.delete()
            if request.data.get('password1') and request.data.get('password2') and request.data.get('password1') == request.data.get('password2'):
                request.user.set_password(request.data.get('password2'))
                request.user.save()
                request.user.auth_token.delete()
            return Response(status=200)
        else:
            return Response(status=400)

class SendTestMail(APIView):
    def post(self,request):
        msg = ''
        title = ''
        if request.data.get("type") == 'callBack':
            msg = f'Телефон :{request.data.get("phone")}'
            title = 'Форма обратной связи (кухни)'
        if request.data.get("type") == 'quiz':
            msg = f'Телефон :{request.data.get("phone")} | Ответы : {request.data.get("quiz")}'
            title = 'Форма квиза (кухни)'

        file = None
        if request.FILES.get('file'):
            file = request.FILES.get('file')
        mail = EmailMessage(title, msg, 'd@skib.org', ('d@skib.org',))
        if file:
            mail.attach(file.name, file.read(), file.content_type)
        mail.send()
        return Response({'result':'ok'})
