from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import EmergencyRequest, EmergencyResponse
from .serializers import EmergencyRequestSerializer, EmergencyResponseSerializer

class EmergencyRequestViewSet(viewsets.ModelViewSet):
    queryset = EmergencyRequest.objects.all()
    serializer_class = EmergencyRequestSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user if request.user.is_authenticated else None)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        emergency_request = self.get_object()
        emergency_request.status = 'accepted'
        emergency_request.save()
        
        response_data = {
            'message': 'Emergency request accepted',
            'emergency_request': EmergencyRequestSerializer(emergency_request).data
        }
        return Response(response_data)
    
    @action(detail=True, methods=['post'])
    def resolve(self, request, pk=None):
        emergency_request = self.get_object()
        emergency_request.status = 'resolved'
        emergency_request.save()
        
        response_data = {
            'message': 'Emergency request resolved',
            'emergency_request': EmergencyRequestSerializer(emergency_request).data
        }
        return Response(response_data)
    
    @action(detail=False, methods=['get'])
    def nearby(self, request):
        lat = float(request.query_params.get('lat', 0))
        lng = float(request.query_params.get('lng', 0))
        radius = float(request.query_params.get('radius', 10))  # Default 10km radius
        
        # Simple distance calculation (in production, use proper geospatial queries)
        nearby_requests = []
        for emergency in self.queryset.filter(status='pending'):
            distance = ((float(emergency.latitude) - lat) ** 2 + (float(emergency.longitude) - lng) ** 2) ** 0.5
            if distance <= radius:
                nearby_requests.append(emergency)
        
        serializer = self.get_serializer(nearby_requests, many=True)
        return Response(serializer.data)

class EmergencyResponseViewSet(viewsets.ModelViewSet):
    queryset = EmergencyResponse.objects.all()
    serializer_class = EmergencyResponseSerializer
    
    @action(detail=True, methods=['patch'])
    def update_location(self, request, pk=None):
        response = self.get_object()
        response.current_location_lat = request.data.get('latitude')
        response.current_location_lng = request.data.get('longitude')
        response.save()
        
        return Response({
            'message': 'Location updated successfully',
            'response': EmergencyResponseSerializer(response).data
        })
