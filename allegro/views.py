from rest_framework.viewsets import ModelViewSet
from .models import Profile
from .serializers import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = AuthorSerializer




