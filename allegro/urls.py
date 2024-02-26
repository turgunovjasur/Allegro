from django.urls import path, include
from rest_framework import routers
from .views import Shaxsiy_kabinetViewSet, BolimViewSet

router = routers.DefaultRouter()
router.register(r"shaxsiy_kabinet", Shaxsiy_kabinetViewSet)
router.register(r'bolim', BolimViewSet)

urlpatterns = [
    path('', include(router.urls))
]
