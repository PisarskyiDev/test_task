from django.db.models import Sum
from rest_framework import generics

from .models import SpendStatistic
from .serializers import SpendStatisticSerializer


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
