from rest_framework import serializers
from .models import RevenueStatistic


class RevenueStatisticSerializer(serializers.ModelSerializer):
    revenue = serializers.DecimalField(max_digits=9, decimal_places=2)
    spend_spend = serializers.DecimalField(max_digits=10, decimal_places=2)
    spend_impressions = serializers.IntegerField(read_only=True)
    spend_clicks = serializers.IntegerField(read_only=True)
    spend_conversion = serializers.IntegerField(read_only=True)

    class Meta:
        model = RevenueStatistic
        fields = (
            "name",
            "date",
            "revenue",
            "spend_spend",
            "spend_impressions",
            "spend_clicks",
            "spend_conversion",
        )
