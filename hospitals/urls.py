from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HospitalViewSet, HospitalDepartmentViewSet, HospitalReviewViewSet

router = DefaultRouter()
router.register(r'hospitals', HospitalViewSet)
router.register(r'departments', HospitalDepartmentViewSet)
router.register(r'reviews', HospitalReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
