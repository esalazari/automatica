from django.shortcuts import render
from AppCamara.models import *

# Create your views here.


def home(request):
    _camaras = Camara.objects.filter(registroActivo=True).order_by(
        "registroFechaCreacion"
    )[:4]
    context = {"camaras": _camaras}
    return render(request, "base/inicio.html", context=context)

def cargarDatosIniciales(request):
    TipoCamara.objects.create( codigo = 'TC-001', descripcion = 'Congelado')
    TipoCamara.objects.create( codigo = 'TC-002', descripcion = 'Refrigeración')
