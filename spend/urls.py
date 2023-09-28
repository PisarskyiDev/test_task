from django.urls import path

from .views import SpendStatisticViews

urlpatterns = [
    path("", SpendStatisticViews.as_view(), name="spend_statistics"),
]

app_name = "spend"
