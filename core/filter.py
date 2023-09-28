from django_filters import (
    rest_framework as filters,
)


class Filter(filters.FilterSet):
    min_date = filters.DateFilter(field_name="date", lookup_expr="gte")
    max_date = filters.DateFilter(field_name="date", lookup_expr="lte")
    name = filters.CharFilter(field_name="name", lookup_expr="iexact")

    class Meta:
        model = None
        fields = []

    @staticmethod
    def get_filter_backend() -> list:
        return [filters.DjangoFilterBackend]
