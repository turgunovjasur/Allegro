from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .models import Shaxs, Bolim, Xabarlar, Ariza
from .serializers import ShaxsSerializer, BolimSerializer, XabarlarSerializer, ArizaSerializer


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







