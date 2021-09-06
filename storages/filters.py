import rest_framework_filters as filters

from .models import Storage, STORAGE_TYPE, WAREHOUSE_TYPE


class StorageFilter(filters.FilterSet):
    min_square = filters.NumberFilter(field_name="square", lookup_expr='gte')
    max_square = filters.NumberFilter(field_name="square", lookup_expr='lte')

    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    warehouse_type = filters.MultipleChoiceFilter(choices=WAREHOUSE_TYPE,
                                                  lookup_expr='icontains')

    storage_type = filters.MultipleChoiceFilter(choices=STORAGE_TYPE,
                                                lookup_expr='icontains')

    metro = filters.CharFilter(field_name='metro__code_name', lookup_expr='icontains')
    company = filters.CharFilter(field_name='company_owner__name', lookup_expr='icontains')

    o = filters.OrderingFilter(
        fields=(
            ('address', 'address'),
            ('price', 'price'),
            ('square', 'square')
        ),
    )

    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Storage
        fields = ['address', 'description',
                  'work_hours_start',
                  'work_hours_end',
                  'metro',
                  'city',

                  'video_surveillance',
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
