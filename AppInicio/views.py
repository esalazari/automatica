from wsgiref.validate import validator
from django.shortcuts import render
from AppCamara.models import *
from AppInicio.libreria import valorUf

# Create your views here.


def home(request):
    _camaras = Camara.objects.filter(registroActivo=True).order_by(
        "registroFechaCreacion"
    )[:4]
    _valor_uf = valorUf()
    _json = []
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
        'camaras': _camaras,
        'json': _json
        }
    return render(request, "base/inicio.html", context=_context)

def cargarDatosIniciales(request):
    TipoCamara.objects.create( codigo = 'TC-001', descripcion = 'Congelado')
    TipoCamara.objects.create( codigo = 'TC-002', descripcion = 'Refrigeración')
