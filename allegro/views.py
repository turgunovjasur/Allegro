from rest_framework.viewsets import ModelViewSet
from .models import Shaxsiy_kabinet, Bolim
from .serializers import Shaxsiy_kabinetSerializer, BolimSerializer


class Shaxsiy_kabinetViewSet(ModelViewSet):
    queryset = Shaxsiy_kabinet.objects.all()
    serializer_class = Shaxsiy_kabinetSerializer


class BolimViewSet(ModelViewSet):
    queryset = Bolim.objects.all()
    serializer_class = BolimSerializer




