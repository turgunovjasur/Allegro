from rest_framework import serializers
from .models import *


class ShaxsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shaxs
        fields = "__all__"


class BolimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolim
        fields = '__all__'


class XabarlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xabarlar
        fields = '__all__'


class ArizaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ariza
        fields = '__all__'
        depth = 1





