from django.db import models

from company.models import Company


ACCESS_TYPE = (('24h', 'around clock'), ('ttt', 'from time to time'))
SURVEILLANCE_TYPE = (('v', 'video'), ('h', 'human'), ('n', 'none'))
TEMPERATURE_TYPE = (('c', 'cold'), ('w', 'warm'))


class Storage(models.Model):
    address = models.TextField()
    owner = models.ForeignKey(Company, on_delete=models.CASCADE)

    description = models.TextField(blank=True, null=True)

    square = models.CharField(max_length=20)
    price = models.CharField(max_length=20)

    access = models.CharField(max_length=30, choices=ACCESS_TYPE)
    work_hours_start = models.TimeField(null=True, blank=True)
    work_hours_end = models.TimeField(null=True, blank=True)

    surveillance = models.CharField(max_length=10, choices=SURVEILLANCE_TYPE)

    climate = models.CharField(max_length=4, choices=TEMPERATURE_TYPE)



