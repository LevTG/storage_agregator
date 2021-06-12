from django.db import models
import uuid


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)

    owner = models.ForeignKey('profile.Profile', on_delete=models.CASCADE)
    city = models.CharField(max_length=30, blank=True, null=True)
    is_private = models.BooleanField(default=False)

    def applications(self):
        return self.storage_set.select_related('application_set')

    def __str__(self):
        return self.name
