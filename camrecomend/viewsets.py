from re import T
from rest_framework import viewsets
from . import models
from . import serializers

class TestViewset(viewsets.ModelViewSet):
    queryset = models.Test.objects.all()
    serializer_class = serializers.TestSerializer