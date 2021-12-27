from currency.models import ContactCreate, Rate

from django_filters import rest_framework as filters


class RateFilter(filters.FilterSet):

    class Meta:
        model = Rate
        fields = {
            'buy': ('lt', 'lte', 'gt', 'gte', 'exact'),
            'sale': ('lt', 'lte', 'gt', 'gte', 'exact'),
        }


class ContactCreateFilter(filters.FilterSet):

    class Meta:
        model = ContactCreate
        fields = {
            'created': ('date', 'lte', 'gte'),
        }
