from rest_framework import viewsets , generics
from . import models
from . import serializers


class UserCreateSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer