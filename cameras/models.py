# Model for storing flock camera locations
from django.db import models

class CameraLocation(models.Model):
    description = models.CharField(max_length=255, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False, help_text="Moderator approval required.")

    def __str__(self):
        return f"{self.description} ({self.latitude}, {self.longitude})"
from django.db import models

# Create your models here.
