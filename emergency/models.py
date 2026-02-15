from django.db import models
from django.contrib.auth.models import User

class EmergencyRequest(models.Model):
    EMERGENCY_TYPES = [
        ('medical', 'Medical Emergency'),
        ('accident', 'Accident'),
        ('fire', 'Fire'),
        ('crime', 'Crime'),
        ('other', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    emergency_type = models.CharField(max_length=20, choices=EMERGENCY_TYPES)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    contact_phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.emergency_type} - {self.address}"

class EmergencyResponse(models.Model):
    emergency_request = models.OneToOneField(EmergencyRequest, on_delete=models.CASCADE)
    responder_name = models.CharField(max_length=100)
    responder_type = models.CharField(max_length=50)  # ambulance, police, fire dept
    estimated_arrival = models.DateTimeField()
    current_location_lat = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    current_location_lng = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Response to {self.emergency_request}"
