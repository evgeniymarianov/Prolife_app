from django_filters import rest_framework as filters
from .models import Gift


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class GiftFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name='category__name', lookup_expr='in')
    create_date = filters.RangeFilter()

    class Meta:
        model = Gift
        fields = ['category', 'create_date']
