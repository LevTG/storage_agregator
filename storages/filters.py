import rest_framework_filters as filters
from django.db.models import Q

from .models import Storage, STORAGE_TYPE, WAREHOUSE_TYPE


# По какой-то причине данные попадающие в MultipleChoiceFilter обрабатываются некорректно (возможно из-за кастомного поля до этого). И все ломается
# Для этого создала этот CustomFiter

class CustomMultipleChoiceFilter(filters.MultipleChoiceFilter):
    def filter(self, qs, value):
        if not value:
            # Even though not a noop, no point filtering if empty.
            return qs

        if self.is_noop(qs, value):
            return qs

        if not self.conjoined:
            q = Q()
        for v in set(value):
            if v == self.null_value:
                v = None
            predicate = self.get_filter_predicate([[v]])
            if self.conjoined:
                qs = self.get_method(qs)(**predicate)
            else:
                q |= Q(**predicate)

        if not self.conjoined:
            qs = self.get_method(qs)(q)

        return qs.distinct() if self.distinct else qs


class StorageFilter(filters.FilterSet):
    min_square = filters.NumberFilter(field_name="square", lookup_expr='gte')
    max_square = filters.NumberFilter(field_name="square", lookup_expr='lte')

    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    warehouse_type = CustomMultipleChoiceFilter(choices=WAREHOUSE_TYPE,
                                                lookup_expr='in')

    storage_type = CustomMultipleChoiceFilter(choices=STORAGE_TYPE,
                                              lookup_expr='in')

    metro = filters.CharFilter(field_name='metro__name', lookup_expr='in')

    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Storage
        fields = ['address', 'description',
                  'work_hours_start',
                  'work_hours_end',

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
