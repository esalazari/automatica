from django.shortcuts import render
from apps.machine.models import Machine, ImageMachine
from apps.cold_chambers.models import ColdChambers

# Create your views here.


def home(request):
    machines = Machine.objects.all()
    coldchambers = ColdChambers.objects.all()
    context = {"machines": machines, "coldchambers": coldchambers}
    return render(request, "body.html", context=context)
