from django.http import JsonResponse
from AppProducto.models import *


def jsonListarProductos(request):
    _json = []
    _contador = 0
    _productos = Producto.objects.filter(registroActivo=True)

    for _producto in _productos:
        _contador += 1
        _item = {
            "numero": _contador,
            "id": _producto.id,
            "nombre": _producto.nombre,
            "codigo": _producto.codigo,
            "pdf": "",
            "valor_neto": "",
            "iva_incluido": "",
            "oferta_neto": _producto.id,
            "oferta_con_iva": "",
        }
        _json.append(_item)
    return JsonResponse(_json, safe=False)
