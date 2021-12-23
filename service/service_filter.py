from functools import reduce
import operator

from django.db.models import Q
from django_filters import rest_framework as filters
from service.models import Service


class MultipleValueM2MFilter(filters.Filter):
    def filter(self, queryset, value):
        values = value.strip().split(',') if isinstance(value, str) else value
        values = set(v.strip() for v in values)
        lhs = '{self.field_name}__{}'  # left hand side
        if self.lookup_expr == 'in':
            return Q(**{lhs.format('in'): list(values)})
        else:
            return reduce(
                operator.or_,
                (Q(**{lhs.format(self.lookup_expr): value}) for value in values)
            )


class ServiceFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    category = filters.BaseInFilter(lookup_expr='in', field_name='category__name')
    os_platform = MultipleValueM2MFilter(field_name='os_platform__name', lookup_expr='in')
    # os_platform = MultipleValeM2MFilter(field_name='os_platform__name')

    class Meta:
        model = Service
        fields = ('name', 'category', 'os_platform')
        # fields = {
        #     # 'price': ['lt', 'gt'],
        #     'name': ['icontains'],
        #     'category': ['in'],
        #     # 'os_platform__name': ['iexact'],
        #     # 'os_platform__is_free': ['exact']
        # }
