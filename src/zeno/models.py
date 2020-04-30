from django.db import models

# Create your models here.

class ZenoItem(models.Model):
  zenoid = models.IntegerField(null=True, blank=True) 
  timestamp = models.CharField(max_length=100, null=True, blank=True)
  temperature = models.FloatField(null=True, blank=True)
  duration = models.CharField(max_length=250, null=True, blank=True)
