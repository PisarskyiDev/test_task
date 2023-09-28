from django.db.models import Sum
from rest_framework import generics

from core.filter import Filter
from .models import RevenueStatistic
from .serializers import RevenueStatisticSerializer


class RevenueStatisticFilter(Filter):
    class Meta:
        model = RevenueStatistic
        fields = []


class RevenueStatisticViews(generics.ListAPIView):
    queryset = (
        RevenueStatistic.objects.values("name", "date")
        .annotate(
            revenue=Sum("revenue"),
            spend_spend=Sum("spend__spend"),
            spend_impressions=Sum("spend__impressions"),
            spend_clicks=Sum("spend__clicks"),
            spend_conversion=Sum("spend__conversion"),
        )
        .order_by("date", "name")
    )
    serializer_class = RevenueStatisticSerializer
    filter_backends = Filter.get_filter_backend()
    filter_set_class = RevenueStatisticFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.filter_set_class(self.request.GET, queryset=queryset).qs
