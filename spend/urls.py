from django.urls import path
from .views import SpendStatisticViews

urlpatterns = [
    path(
        "statistics/",
        SpendStatisticViews.as_view(),
        name="spend_statistics",
    ),
]

app_name = "spend"
