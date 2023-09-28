from django.test import TestCase
from decimal import Decimal
from rest_framework.test import APIRequestFactory

from spend.models import SpendStatistic
from .models import RevenueStatistic
from .views import RevenueStatisticViews
from .serializers import RevenueStatisticSerializer


class RevenueStatisticTests(TestCase):
    def setUp(self):
        self.revenue_statistic1 = RevenueStatistic.objects.create(
            name="Product A", date="2023-09-01", revenue=Decimal("100.50")
        )
        self.revenue_statistic2 = RevenueStatistic.objects.create(
            name="Product A", date="2023-09-02", revenue=Decimal("150.75")
        )
        self.factory = APIRequestFactory()

    def test_revenue_statistic_view(self):
        view = RevenueStatisticViews.as_view()
        url = "/api/spend/statistics/"
        request = self.factory.get(url)
        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["name"], "Product A")
        self.assertEqual(response.data[0]["date"], "2023-09-01")
        self.assertEqual(response.data[0]["revenue"], "100.50")

    def test_revenue_statistic_serializer(self):
        spend = SpendStatistic.objects.create(
            name="Product A", date="2023-09-01"
        )
        serializer_data = {
            "name": "Product B",
            "date": "2023-09-03",
            "revenue": 75.25,
            "spend_spend": spend.pk,
            "spend_impressions": 1000,
            "spend_clicks": 200,
            "spend_conversion": 10,
        }
        serializer = RevenueStatisticSerializer(data=serializer_data)
        self.assertTrue(serializer.is_valid())

        errors = serializer.errors
        self.assertEqual(errors, {})
