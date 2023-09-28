from django.db.models import Sum
from rest_framework import generics

from core.filter import Filter
from .models import SpendStatistic
from .serializers import SpendStatisticSerializer


class SpendStatisticFilter(Filter):
    class Meta:
        model = SpendStatistic
        fields = []


class SpendStatisticViews(generics.ListAPIView):
    queryset = (
        SpendStatistic.objects.values("name", "date")
        .annotate(
            spend=Sum("spend"),
            impressions=Sum("impressions"),
            clicks=Sum("clicks"),
            conversion=Sum("conversion"),
            revenue=Sum("revenuestatistic__revenue"),
        )
        .order_by("date", "name")
    )
    serializer_class = SpendStatisticSerializer
    filter_backends = Filter.get_filter_backend()
    filter_set_class = Filter

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.filter_set_class(self.request.GET, queryset=queryset).qs
