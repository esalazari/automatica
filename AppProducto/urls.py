from argparse import Namespace
from django.urls import path
from AppProducto import views, dx
from django.conf import settings
from django.conf.urls.static import static

app_name = "productos"

urlpatterns = [
    path("json-lista-producto/", dx.jsonListarProductos, name="json-lista-producto"),
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
