from django.urls import path

from .views import RevenueStatisticViews

urlpatterns = [
    path("", RevenueStatisticViews.as_view(), name="revenue_statistics"),
]

app_name = "revenue"
