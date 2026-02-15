from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Hospital, HospitalDepartment, HospitalReview
from .serializers import HospitalSerializer, HospitalDepartmentSerializer, HospitalReviewSerializer

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.filter(is_active=True)
    serializer_class = HospitalSerializer
    
    @action(detail=False, methods=['get'])
    def nearby(self, request):
        lat = float(request.query_params.get('lat', 0))
        lng = float(request.query_params.get('lng', 0))
        radius = float(request.query_params.get('radius', 10))  # Default 10km radius
        
        # Simple distance calculation (in production, use proper geospatial queries)
        nearby_hospitals = []
        for hospital in self.queryset:
            distance = ((float(hospital.latitude) - lat) ** 2 + (float(hospital.longitude) - lng) ** 2) ** 0.5
            if distance <= radius:
                nearby_hospitals.append(hospital)
        
        serializer = self.get_serializer(nearby_hospitals, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def departments(self, request, pk=None):
        hospital = self.get_object()
        departments = hospital.departments.filter(is_active=True)
        serializer = HospitalDepartmentSerializer(departments, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def add_review(self, request, pk=None):
        hospital = self.get_object()
        serializer = HospitalReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(hospital=hospital)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        hospital = self.get_object()
        reviews = hospital.reviews.all()
        serializer = HospitalReviewSerializer(reviews, many=True)
        return Response(serializer.data)

class HospitalDepartmentViewSet(viewsets.ModelViewSet):
    queryset = HospitalDepartment.objects.filter(is_active=True)
    serializer_class = HospitalDepartmentSerializer

class HospitalReviewViewSet(viewsets.ModelViewSet):
    queryset = HospitalReview.objects.all()
    serializer_class = HospitalReviewSerializer
