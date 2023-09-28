from rest_framework import serializers
from .models import SpendStatistic


class SpendStatisticSerializer(serializers.ModelSerializer):
    revenue = serializers.DecimalField(
        read_only=True, max_digits=9, decimal_places=2
    )

    class Meta:
        model = SpendStatistic
        fields = (
            "name",
            "date",
            "spend",
            "impressions",
            "clicks",
            "conversion",
            "revenue",
        )
