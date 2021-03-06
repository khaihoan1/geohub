from django.db.models import Q
from django_filters import rest_framework as filters

from service.models import Service


class MultipleValueM2MFilter(filters.Filter):
    def filter(self, queryset, value):
        if not value:
            return queryset
        values = value.strip().split(',') if isinstance(value, str) else value
        values = set(v.strip() for v in values)
        lhs = '{}__{}'.format(self.field_name, 'in')  # left hand side
        return queryset.prefetch_related(self.field_name.split('__')[0]).filter(Q(**{lhs: list(values)})).distinct()


class ServiceFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    category = filters.BaseInFilter(lookup_expr='in', field_name='category__name')
    os_platform = MultipleValueM2MFilter(field_name='os_platform__name', lookup_expr='in')
    os_free = filters.BooleanFilter(field_name='os_platform__is_free')
    price__gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        models = Service
