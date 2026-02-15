from rest_framework import serializers
from .models import EmergencyRequest, EmergencyResponse

class EmergencyRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyRequest
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'updated_at')

class EmergencyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyResponse
        fields = '__all__'
        read_only_fields = ('created_at',)
