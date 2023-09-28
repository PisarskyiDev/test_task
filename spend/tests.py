from decimal import Decimal

from django.db.models import Sum
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from revenue.models import RevenueStatistic
from .models import SpendStatistic


class SpendStatisticViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.spend_statistic1 = SpendStatistic.objects.create(
            name="Product A",
            date="2023-09-01",
            spend=100.50,
            impressions=1000,
            clicks=200,
            conversion=10,
        )
        self.spend_statistic2 = SpendStatistic.objects.create(
            name="Product A",
            date="2023-09-02",
            spend=150.75,
            impressions=1500,
            clicks=250,
            conversion=12,
        )
        self.revenue_statistic1 = RevenueStatistic.objects.create(
            name="Product B",
            date="2023-09-03",
            revenue=Decimal("75.25"),
            spend=self.spend_statistic1,
        )

    def test_spend_statistic_views(self):
        url = "/api/spend/statistics/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0]["name"], "Product A")
        self.assertEqual(response.data[0]["date"], "2023-09-01")
        self.assertEqual(response.data[0]["spend"], "100.50")
        self.assertEqual(response.data[0]["impressions"], 1000)
        self.assertEqual(response.data[0]["clicks"], 200)
        self.assertEqual(response.data[0]["conversion"], 10)
        self.assertEqual(response.data[0]["revenue"], "75.25")

        self.assertEqual(response.data[1]["name"], "Product A")
        self.assertEqual(response.data[1]["date"], "2023-09-02")
        self.assertEqual(response.data[1]["spend"], "150.75")
        self.assertEqual(response.data[1]["impressions"], 1500)
        self.assertEqual(response.data[1]["clicks"], 250)
        self.assertEqual(response.data[1]["conversion"], 12)
        self.assertEqual(response.data[1]["revenue"], None)

    def test_spend_statistic_views_empty(self):
        SpendStatistic.objects.all().delete()
        url = "/api/spend/statistics/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
