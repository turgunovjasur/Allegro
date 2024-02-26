from django.urls import path, include
from rest_framework import routers
from .views import ShaxsViewSet, BolimViewSet, XabarlarViewSet, ArizaViewSet

router = routers.DefaultRouter()
router.register(r"shaxs", ShaxsViewSet)
router.register(r'bolim', BolimViewSet),
router.register(r'xabarlar', XabarlarViewSet),
router.register(r'ariza', ArizaViewSet),

urlpatterns = [
    path('', include(router.urls))
]
