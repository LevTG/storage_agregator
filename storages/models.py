from django.db import models
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


class Storage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_owner = models.ForeignKey(Company, on_delete=models.CASCADE)

    address = models.TextField()
    metro = models.ManyToManyField(Station)

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