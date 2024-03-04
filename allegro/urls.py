from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"shaxs", ShaxsViewSet)
router.register(r'bolim', BolimViewSet),
router.register(r'xabarlar', XabarlarViewSet),
router.register(r'ariza', ArizaViewSet),
router.register(r'yangiliklar', YangiliklarViewSet),

urlpatterns = [
    path('', include(router.urls))
]
