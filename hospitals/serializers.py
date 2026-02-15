from rest_framework import serializers
from .models import Hospital, HospitalDepartment, HospitalReview

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class HospitalDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalDepartment
        fields = '__all__'

class HospitalReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalReview
        fields = '__all__'
        read_only_fields = ('created_at',)
