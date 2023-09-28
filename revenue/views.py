from django.db.models import Sum
from rest_framework import generics

from .models import RevenueStatistic
from .serializers import RevenueStatisticSerializer


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
