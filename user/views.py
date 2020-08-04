from rest_framework.response import Response
from rest_framework.views import *
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

class GetInfo(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)


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

