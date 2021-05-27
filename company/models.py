from django.db import models
from authentication.models import Profile


class Company(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)
    city = models.CharField(max_length=30, blank=True, null=True)
