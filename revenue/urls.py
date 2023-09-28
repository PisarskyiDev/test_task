from django.urls import path

# from .views import revenue_summary
from .views import RevenueStatisticViews

urlpatterns = [
    path(
        "statistics/",
        RevenueStatisticViews.as_view(),
        name="revenue_statistics",
    ),
]

app_name = "revenue"
