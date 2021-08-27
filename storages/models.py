from django.contrib.gis.db.models import PointField
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid

from multiselectfield import MultiSelectField

from images.models import ImageAlbum
from company.models import Company
from metro.models import Station

WAREHOUSE_TYPE = (('warm', 'Теплый склад',), ('cold', 'Холодный склад'), ('sea', 'Морской контейнер'),
                  ('box', 'Индивидуальный бокс (умный замок)'), ('zshk', 'Кладовки в ЖК'),
                  ('free', 'Свободные помещения'))

STORAGE_TYPE = (('cloud', 'Облачное хранение'), ('individual', 'Индивидуальное хранение'),
                ('responsibility', 'Ответственное хранение'), ('private', 'Частные кладовки'))

STORAGE_STATUS = (('a', 'accepted'), ('d', 'declined'), ('p', 'in process'), ('m', 'on moderation'))


class Storage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_owner = models.ForeignKey(Company, on_delete=models.CASCADE)

    address = models.TextField()
    metro = models.ManyToManyField(Station)
    city = models.CharField(max_length=50, blank=True, null=True)

    # Society
    email = models.EmailField(_('email address'), db_index=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?\d{9,16}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 16 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)

    # Social Network
    vk = models.CharField(max_length=50, blank=True, null=True)
    facebook = models.CharField(max_length=50, blank=True, null=True)
    ok = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)

    location = PointField(null=True)

    description = models.TextField(blank=True, null=True)

    square = models.FloatField(max_length=20, blank=True, null=True)
    price = models.FloatField(max_length=20, blank=True, null=True)

    album = models.OneToOneField(ImageAlbum, related_name='model', on_delete=models.CASCADE, null=True, blank=True)

    work_hours_start = models.TimeField(default='00:00:00')
    work_hours_end = models.TimeField(default='23:59:59')

    warehouse_type = MultiSelectField(choices=WAREHOUSE_TYPE, max_choices=len(WAREHOUSE_TYPE), blank=True, null=True)
    storage_type = MultiSelectField(choices=STORAGE_TYPE, max_choices=len(STORAGE_TYPE), blank=True, null=True)

    video_surveillance = models.BooleanField(default=False)
    access_24h = models.BooleanField(default=False)
    mobile_app = models.BooleanField(default=False)
    clever_lock = models.BooleanField(default=False)
    cleaning = models.BooleanField(default=False)
    online_contract = models.BooleanField(default=False)
    ventilation = models.BooleanField(default=False)
    shipping = models.BooleanField(default=False)
    wrapping = models.BooleanField(default=False)
    straight_way = models.BooleanField(default=False)
    any_rental_period = models.BooleanField(default=False)
    inventory = models.BooleanField(default=False)
    inshurance = models.BooleanField(default=False)

    status = models.CharField(max_length=20, choices=STORAGE_STATUS, default='m')

    @property
    def services(self):
        return {
            'access_24h': self.access_24h,
            'mobile_app': self.mobile_app,
            'clever_lock': self.clever_lock,
            'cleaning': self.cleaning,
            'online_contract': self.online_contract,
            'ventilation': self.ventilation,
            'shipping': self.shipping,
            'wrapping': self.wrapping,
            'straight_way': self.straight_way,
            'any_rental_period': self.any_rental_period,
            'inventory': self.inventory,
            'inshurance': self.inshurance,
            'video_surveillance': self.video_surveillance
        }

    @property
    def social(self):
        return {
            'vk': self.vk,
            'facebook': self.facebook,
            'ok': self.ok,
            'instagram': self.instagram
        }

    @property
    def longitude(self):
        return self.location.x

    @property
    def latitude(self):
        return self.location.y


class Manager(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    telegram_id = models.CharField(max_length=9)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    storage = models.ForeignKey(Storage, related_name='managers', on_delete=models.CASCADE)
