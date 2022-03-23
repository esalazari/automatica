from argparse import Namespace
from django.urls import path
from AppCamara import views, dx
from django.conf import settings
from django.conf.urls.static import static

app_name = "camaras"

urlpatterns = [
    path("json-listar-camaras/", dx.jsonListarCamaras, name="json-lista-camaras"),
    path(
        "camaras-de-frio/",
        views.camarasfrio,
        name="camaras-de-frio",
    ),
    path(
        "camaras-refrigeracion/",
        views.camarasRefrigeracion,
        name="camaras-refrigeracion",
    ),
    path(
        "camaras-congelado/",
        views.camarasCongelado,
        name="camaras-congelado",
    ),
    path(
        "camara-detalle/<int:id>",
        views.camaraDetalle,
        name="camara-detalle",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
