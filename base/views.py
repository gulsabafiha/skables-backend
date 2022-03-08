from .models import Customuser
from rest_framework import viewsets,status
from rest_framework.permissions import AllowAny
from .serializers import PaintingSerializer, UserSerializer, ArtistSerializer
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


class UserViewSet(viewsets.ModelViewSet):
    queryset = Customuser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


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
