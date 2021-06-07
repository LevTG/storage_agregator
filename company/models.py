from django.db import models
from storages.models import Storage


class Company(models.Model):

    name = models.CharField(max_length=50, blank=True, null=True)

    owner = models.OneToOneField('authentication.Profile', on_delete=models.CASCADE)
    city = models.CharField(max_length=30, blank=True, null=True)
    is_private = models.BooleanField(default=False)
    storages = models.ManyToManyField(Storage)
