from django.shortcuts import render

from AppProducto.models import Producto

# Create your views here.


def camarasfrio(request):
    _productos = Producto.objects.filter(registroActivo=True)
    _context = {"productos": _productos}
    return render(request, "camaras_listar.html", context=_context)


def camarasRefrigeracion(request):
    _productos = Producto.objects.filter(registroActivo=True, tipo=1)
    _context = {"productos": _productos}
    return render(request, "camaras_refrigeracion.html", context=_context)


def camarasCongelado(request):
    _productos = Producto.objects.filter(registroActivo=True, tipo=2)
    _context = {"productos": _productos}
    return render(request, "camaras_refrigeracion.html", context=_context)
