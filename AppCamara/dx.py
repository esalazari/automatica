from django.http import JsonResponse
from AppCamara.models import *


def jsonListarCamaras(request):
    _json = []
    _contador = 0
    _camaras = Camara.objects.filter(registroActivo=True)

    for _camara in _camaras:
        _contador += 1
        _item = {
            "numero": _contador,
            "id": _camara.id,
            "nombre": _camara.nombre,
            "codigo": _camara.codigo,
            "pdf": "",
            "valor_neto": "",
            "iva_incluido": "",
            "oferta_neto": _camara.id,
            "oferta_con_iva": "",
        }
        _json.append(_item)
    return JsonResponse(_json, safe=False)
