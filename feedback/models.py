import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _

from profile.models import Profile
from storages.models import Storage


FEEDBACK_STATUS = (('a', 'accepted'), ('d', 'declined'), ('m', 'on moderation'))


class StorageFeedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    rating = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.ForeignKey(Profile, related_name='feedbacks', on_delete=models.CASCADE)
    storage = models.ForeignKey(Storage, related_name='feedbacks', on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)

    status = models.CharField(choices=FEEDBACK_STATUS, default='m')
