from email import message
from .models import Customuser
from rest_framework import viewsets,status
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import PaintingSerializer, UserSerializer, ArtistSerializer,UserSerializerWithToken
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer=UserSerializerWithToken(self.user).data
        for k,v in serializer.items():
            data[k]=v
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



""" class UserViewSet(viewsets.ModelViewSet):
    queryset = Customuser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,) """

@api_view(['POST'])
def registerUser(request):
    data=request.data
    try:
        user=Customuser.objects.create(
            username=data['username'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serializer=UserSerializerWithToken(user,many=False)
        return Response(serializer.data)
    except:
        message={'detail':'User with the email already exists'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getUser(request):
    users=Customuser.objects.all()
    serializer=UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user=request.user
    serializer=UserSerializerWithToken(user,many=False)

    data=request.data

    user.first_name=data['name']
    user.username=data['username']
    user.email=data['email']
    if data['password'] != '':
        user.password=make_password(data['password'])
    user.save()
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user=request.user
    serializer=UserSerializer(user,many=False)
    return Response(serializer.data)



class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = (AllowAny,)


class PaintingViewSet(viewsets.ModelViewSet):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer
    permission_classes = (AllowAny,)


@api_view(['GET'])
def product_detail(request,pk):
    try:
        obj=Painting.objects.get(id=pk)
    except Painting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer=PaintingSerializer(obj)
    return Response(serializer.data)
