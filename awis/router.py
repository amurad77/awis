from core.viewsets import SubscribeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('subscribe', SubscribeViewset)