from rest_framework import serializers
from .models import Shaxsiy_kabinet, Bolim


class Shaxsiy_kabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shaxsiy_kabinet
        fields = "__all__"


class BolimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolim
        fields = '__all__'
