from django.db import models

class Hospital(models.Model):
    HOSPITAL_TYPES = [
        ('general', 'General Hospital'),
        ('specialty', 'Specialty Hospital'),
        ('clinic', 'Clinic'),
        ('emergency', 'Emergency Care Center'),
    ]
    
    name = models.CharField(max_length=200)
    hospital_type = models.CharField(max_length=20, choices=HOSPITAL_TYPES)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    emergency_services = models.BooleanField(default=True)
    bed_capacity = models.IntegerField(null=True, blank=True)
    available_beds = models.IntegerField(null=True, blank=True)
    average_wait_time = models.IntegerField(help_text="Average wait time in minutes", null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-rating', 'name']

class HospitalDepartment(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.hospital.name} - {self.name}"

class HospitalReview(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review for {self.hospital.name} by {self.user_name}"
