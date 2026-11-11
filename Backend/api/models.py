from django.db import models


class WindyAccessLog(models.Model):
    """Simple IP-based rate limiter for Windy API access (2 per day)."""
    ip_address = models.GenericIPAddressField()
    accessed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'windy_access_log'

    def __str__(self):
        return f"{self.ip_address} - {self.accessed_at}"


class FarmArea(models.Model):
    """Stores a farmer's drawn area with crop/soil metadata."""
    name                  = models.CharField(max_length=255)
    area_coordinates      = models.JSONField(default=list)
    center_coordinates    = models.JSONField(blank=True, null=True)
    # Crop info
    primaryCrop           = models.CharField(max_length=255, blank=True, default='')
    secondaryCrops        = models.CharField(max_length=255, blank=True, default='')
    soilType              = models.CharField(max_length=255, blank=True, default='')
    irrigationSystem      = models.CharField(max_length=255, blank=True, default='')
    # Fertilization
    fertilizers           = models.CharField(max_length=255, blank=True, default='')
    fertilizationFrequency = models.CharField(max_length=255, blank=True, default='')
    fertilizationMethod   = models.CharField(max_length=255, blank=True, default='')
    # Pests
    commonPests           = models.CharField(max_length=255, blank=True, default='')
    pesticides            = models.CharField(max_length=255, blank=True, default='')
    # Yield
    previousYield         = models.CharField(max_length=255, blank=True, default='')
    soilTestResults       = models.CharField(max_length=255, blank=True, default='')
    yieldLosses           = models.CharField(max_length=255, blank=True, default='')
    additionalNotes       = models.TextField(blank=True, default='')
    # File uploads
    soilReports           = models.FileField(upload_to='farm_areas/soil_reports/',    blank=True, null=True)
    yieldData             = models.FileField(upload_to='farm_areas/yield_data/',       blank=True, null=True)
    cropPhotos            = models.FileField(upload_to='farm_areas/crop_photos/',      blank=True, null=True)
    otherDocuments        = models.FileField(upload_to='farm_areas/other_documents/',  blank=True, null=True)
    # Timestamps
    created_at            = models.DateTimeField(auto_now_add=True)
    updated_at            = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'farm_area'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
