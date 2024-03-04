from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class ShaxsViewSet(ModelViewSet):
    queryset = Shaxs.objects.all()
    serializer_class = ShaxsSerializer


class BolimViewSet(ModelViewSet):
    queryset = Bolim.objects.all()
    serializer_class = BolimSerializer


class XabarlarViewSet(viewsets.ModelViewSet):
    queryset = Xabarlar.objects.all()
    serializer_class = XabarlarSerializer


class ArizaViewSet(viewsets.ModelViewSet):
    queryset = Ariza.objects.all()
    serializer_class = ArizaSerializer


class YangiliklarViewSet(viewsets.ModelViewSet):
    queryset = Yangiliklar.objects.all()
    serializer_class = YangiliklarSerializer






