from django.urls import path
from .views import ColdchambersListView, ColdchamberDetail

app_name = "coldchamber"

urlpatterns = [
    path("", ColdchambersListView.as_view(), name="coldchambers"),
    path(
        "detalle-camara-de-frio/<int:pk>/",
        ColdchamberDetail.as_view(),
        name="detail_coldchamber",
    ),
]
