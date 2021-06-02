from django.db import models
import uuid
from insuree.apps import InsureeConfig
from insuree import models as insuree_models
from location import models as location_models

# Create your models here.
class InsureeAuth(models.Model):
    insuree = models.OneToOneField(insuree_models.Insuree, on_delete=models.DO_NOTHING,
                                db_column='InsureeID', blank=True, null=True, related_name="verified_insurees")
    token = models.CharField(max_length=300)
    otp = models.CharField(max_length=10, null=True, blank=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        name = ''
        if self.insuree.other_names:
            name= self.insuree.other_names
        return name

class Notice(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    active = models.BooleanField(default=True)
    created_at =  models.DateTimeField(verbose_name='date added', auto_now_add=True)
    updated_at =   models.DateTimeField(verbose_name='date updated', auto_now_add=True)
    
    def __str__(self):
        return self.title

class HealthFacilityCoordinate(models.Model):
    id = models.AutoField(db_column='hfcId', primary_key=True)
    uuid = models.CharField(db_column='hfcUUID',
                            max_length=36, default=uuid.uuid4, unique=True)
    health_facility = models.ForeignKey(
        location_models.HealthFacility, models.DO_NOTHING, db_column='HFID')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    
    