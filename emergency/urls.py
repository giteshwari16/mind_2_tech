from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmergencyRequestViewSet, EmergencyResponseViewSet

router = DefaultRouter()
router.register(r'emergency-requests', EmergencyRequestViewSet)
router.register(r'emergency-responses', EmergencyResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
