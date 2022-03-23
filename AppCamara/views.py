from multiprocessing import context
from django.shortcuts import render
from AppInicio.libreria import valorUf
import json
import requests

from AppCamara.models import Camara, ImagenCamara

# Create your views here.

def camarasfrio(request):
    _camaras = Camara.objects.filter(registroActivo=True)
    _json = []
    _valor_uf = valorUf()
    for _camara in _camaras:
        _precio = _camara.valorUF * _valor_uf
        _precio_antes = _precio + _precio * 0.1
        _precio_intalacion = _precio + _precio * 0.2
        _item = {
            'id': _camara.id,
            'nombre': _camara.nombre,
            'dimension': _camara.dimension,
            'tipo': _camara.tipo.descripcion,
            'precio_old': int(_precio_antes),
            'precio': int(_precio),
            'precio_intalacion':int(_precio_intalacion)
        }
        _json.append(_item)
    _context = {
        "camaras": _camaras,
        "json": _json,
    }
    return render(request, "camaras_listar.html", context=_context)


def camarasRefrigeracion(request):
    _camaras = Camara.objects.filter(registroActivo=True, tipo=1)
    _json = []
    _valor_uf = valorUf()
    for _camara in _camaras:
        _precio = _camara.valorUF * _valor_uf
        _precio_antes = _precio + _precio * 0.1
        _precio_intalacion = _precio + _precio * 0.2
        _item = {
            'id': _camara.id,
            'nombre': _camara.nombre,
            'dimension': _camara.dimension,
            'tipo': _camara.tipo.descripcion,
            'precio_old': int(_precio_antes),
            'precio': int(_precio),
            'precio_intalacion':int(_precio_intalacion)
        }
        _json.append(_item)
    _context = {
        "camaras": _camaras,
        "json": _json,
    }
    return render(request, "camaras_refrigeracion.html", context=_context)


def camarasCongelado(request):
    _camaras = Camara.objects.filter(registroActivo=True, tipo=2)
    _json = []
    _valor_uf = valorUf()
    for _camara in _camaras:
        _precio = _camara.valorUF * _valor_uf
        _precio_antes = _precio + _precio * 0.1
        _precio_intalacion = _precio + _precio * 0.2
        _item = {
            'id': _camara.id,
            'nombre': _camara.nombre,
            'dimension': _camara.dimension,
            'tipo': _camara.tipo.descripcion,
            'precio_old': int(_precio_antes),
            'precio': int(_precio),
            'precio_intalacion':int(_precio_intalacion)
        }
        _json.append(_item)
    _context = {
        "camaras": _camaras,
        "json": _json,
    }
    return render(request, "camaras_congelado.html", context=_context)


def camaraDetalle(request, id):
    _camara = Camara.objects.get(id=id)
    _imagenPortada = _camara.imagen.filter(registroActivo=True)[:1].get()
    _imagenes = _camara.imagen.all()
    _context = {"camara": _camara, "imagenes": _imagenes, "portada": _imagenPortada}
    return render(request, "camara_detalle.html", context=_context)
