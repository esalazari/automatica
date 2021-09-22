from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from apps.cold_chambers.models import ColdChambers

# Create your views here.

# Llama a todas las maquinas disponibles en la base de datos
class ColdchambersListView(ListView):
    # dirección del template donde irá la clase
    template_name = "coldchamber/coldchamber.html"
    # objetos traido desde la base de datos
    queryset = ColdChambers.objects.all()
    # Cantidad de productos por paginas
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["coldchambers"] = ColdChambers.objects.all

        return context


class ColdchamberDetail(DetailView):
    model = ColdChambers
    template_name = "coldchamber/coldchamber_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["coldchambers"] = ColdChambers.objects.all

        return context
