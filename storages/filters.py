from rest_framework import filters
from django_filters.rest_framework import FilterSet
from django_filters import NumberFilter, MultipleChoiceFilter
from .models import Storage


class StorageFilter(FilterSet):
    square = NumberFilter(name="square", lookup_expr='gte')
    price = NumberFilter(name="price", lookup_expr='lte')

    warehouse_type = MultipleChoiceFilter()
    storage_type = MultipleChoiceFilter()

    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Storage
        fields = ['address', 'description',
                  'square', 'price',
                  'work_hours_start',
                  'work_hours_end',
                  'video_surveillance',
                  'storage_type',
                  'warehouse_type',

                  'access_24h',
                  'mobile_app',
                  'clever_lock',
                  'cleaning',
                  'online_contract',
                  'ventilation',
                  'shipping',
                  'wrapping',
                  'straight_way',
                  'any_rental_period',
                  'inventory',
                  'inshurance'
                  ]
