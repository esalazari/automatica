from django.urls import path
from AppInicio.views import home
from django.conf import settings
from django.conf.urls.static import static

app_name = "website"

urlpatterns = [
    path("", home, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
