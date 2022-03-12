from multiprocessing import context
from django.shortcuts import render

from AppCamara.models import Camara, ImagenCamara

# Create your views here.


def camarasfrio(request):
    _camaras = Camara.objects.filter(registroActivo=True)
    _context = {"camaras": _camaras}
    return render(request, "camaras_listar.html", context=_context)


def camarasRefrigeracion(request):
    _camaras = Camara.objects.filter(registroActivo=True, tipo=2)
    _context = {"camaras": _camaras}
    return render(request, "camaras_refrigeracion.html", context=_context)


def camarasCongelado(request):
    _camaras = Camara.objects.filter(registroActivo=True, tipo=1)
    _context = {"camaras": _camaras}
    return render(request, "camaras_refrigeracion.html", context=_context)


def camaraDetalle(request, id):
    _camara = Camara.objects.get(id=id)
    _imagenPortada = _camara.imagen.filter(registroActivo=True)[:1].get()
    print(_imagenPortada)
    _imagenes = _camara.imagen.all()
    _context = {"camara": _camara, "imagenes": _imagenes, "portada": _imagenPortada}
    return render(request, "camara_detalle.html", context=_context)
