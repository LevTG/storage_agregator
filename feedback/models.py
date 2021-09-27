import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from storages.models import Storage
from profile.models import Profile


FEEDBACK_STATUS = (('a', 'accepted'), ('d', 'declined'), ('m', 'on moderation'))


class StorageFeedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(_('email address'), db_index=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?\d{9,16}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 16 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)

    rating = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    storage = models.ForeignKey(Storage, related_name='feedbacks', on_delete=models.CASCADE, null=True)
    text = models.TextField(null=True, blank=True)

    status = models.CharField(choices=FEEDBACK_STATUS, default='m', max_length=1)

    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.text, self.username)


class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    feedback = models.ForeignKey(StorageFeedback, related_name='answer', on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)

    status = models.CharField(choices=FEEDBACK_STATUS, default='m', max_length=1)

    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['created_on']
