from django_filters import rest_framework as filters

from car_exchange_app.models import Car


class CarFilter(filters.FilterSet):
    min_run = filters.NumberFilter(field_name="run", lookup_expr='gte')
    max_run = filters.NumberFilter(field_name="run", lookup_expr='lte')

    class Meta:
        model = Car
        fields = ['category', 'min_run', 'max_run', 'category__sub_category']
