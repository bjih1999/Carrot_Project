from django.db import models
from django.utils import timezone

class Carrot(models.Model):
    time = models.DateTimeField(default=timezone.now, null=True)
    temperature = models.FloatField()
    wetness = models.FloatField()
    end_status = models.IntegerField(default=0)

    class Meta:
        ordering = ['time',]
