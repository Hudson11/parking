from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import ParkingView

router = SimpleRouter()
router.register('parking', ParkingView)
