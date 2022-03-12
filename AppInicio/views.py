from django.shortcuts import render
from AppCamara.models import *

# Create your views here.


def home(request):
    _camaras = Camara.objects.filter(registroActivo=True).order_by(
        "registroFechaCreacion"
    )[:4]
    context = {"camaras": _camaras}
    return render(request, "base/inicio.html", context=context)
