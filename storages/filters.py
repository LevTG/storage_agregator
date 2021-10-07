import rest_framework_filters as filters

from .models import Storage, STORAGE_TYPE, WAREHOUSE_TYPE


class DistanceOrderingFilter(filters.OrderingFilter):
    def get_default_ordering(self, view):
        return ('distance', )


class StorageFilter(filters.FilterSet):
    pk = filters.CharFilter(method='id_filter')
    min_square = filters.NumberFilter(field_name="square", lookup_expr='gte')
    max_square = filters.NumberFilter(field_name="square", lookup_expr='lte')

    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    warehouse_type = filters.MultipleChoiceFilter(choices=WAREHOUSE_TYPE,
                                                  lookup_expr='icontains')

    storage_type = filters.MultipleChoiceFilter(choices=STORAGE_TYPE,
                                                lookup_expr='icontains')

    metro = filters.CharFilter(method='metro_filter')
    company = filters.CharFilter(field_name='company_owner__name', lookup_expr='icontains')

    ordering = DistanceOrderingFilter(
        fields=(
            ('address', 'address'),
            ('price', 'price'),
            ('square', 'square'),
            ('distance', 'distance')
        ),
    )

    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)

    def metro_filter(self, queryset, name, value):
        name = 'metro__code_name__in'
        values = [val for val in value.split(',') if val]
        return queryset.filter(**{
            name: values,
        })

    def id_filter(self, queryset, name, value):
        name = 'id__in'
        values = [val for val in value.split(',') if val]
        return queryset.filter(**{name: values,})

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


class StorageCommonFilter(StorageFilter):
    ordering = filters.OrderingFilter(
        fields=(
            ('address', 'address'),
            ('price', 'price'),
            ('square', 'square'),
        ),
    )
