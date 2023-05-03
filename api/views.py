from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import filters
from app.models import Base, File
from accounts.models import CustomUser
from .serializers import BaseSerializer, FileSerializer, UserSerializer

class getBase(generics.ListAPIView):
    queryset = Base.objects.all()
    serializer_class = BaseSerializer
    permission_classes = (AllowAny,)
    filter_backends = [filters.OrderingFilter]
    ordering = ['name']


@api_view(['POST'])
def addBase(request):
    serializer = BaseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()

@api_view(['GET'])
def getUser(request):
    users = CustomUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


class addUser(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

@api_view(['GET'])
def getFile(request):
    files = File.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)
