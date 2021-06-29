from rest_framework import filters
from django_filters.rest_framework import FilterSet
from django_filters import NumberFilter, MultipleChoiceFilter
from .models import Storage, STORAGE_TYPE, WAREHOUSE_TYPE


class StorageFilter(FilterSet):
    min_square = NumberFilter(field_name="square", lookup_expr='gte')
    max_square = NumberFilter(field_name="square", lookup_expr='lte')

    min_price = NumberFilter(field_name="price", lookup_expr='gte')
    max_price = NumberFilter(field_name="price", lookup_expr='lte')

    warehouse_type = MultipleChoiceFilter(choices=WAREHOUSE_TYPE,
                                          to_field_name='warehouse_type',
                                          lookup_expr='in')
    storage_type = MultipleChoiceFilter(choices=STORAGE_TYPE,
                                        to_field_name='storage_type',
                                        lookup_expr='in')

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
