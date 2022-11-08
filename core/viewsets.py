from rest_framework import viewsets
from . import models
from . import serializers

class SubscribeViewset(viewsets.ModelViewSet):
    queryset = models.Subscribe.objects.all()
    serializer_class = serializers.SubscribeSerializer