from django.db import models
from django.core.validators import RegexValidator

from storages.models import Storage
from profile.models import Profile

APPLICATION_STATUS = (('a', 'accepted'), ('d', 'declined'), ('p', 'in process'), ('m', 'on moderation'))


class Application(models.Model):
    name = models.CharField(max_length=20)
    email_regex = RegexValidator(regex=r'^[\S]{5,30}$',
                                 message="Email must be entered in the format: 'aaaa@kkkk.lll'")
    email = models.CharField(validators=[email_regex], max_length=30)

    phone_regex = RegexValidator(regex=r'^\+?\d{9,16}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)

    text = models.TextField(blank=True, null=True)

    date_carry = models.DateField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=APPLICATION_STATUS, default='a')
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Profile, on_delete=models.CASCADE)
