from django.shortcuts import render
from AppProducto.models import *

# Create your views here.


def home(request):
    context = {}
    return render(request, "base/inicio.html", context=context)
