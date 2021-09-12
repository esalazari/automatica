from django.shortcuts import render
from apps.machine.models import Machine, ImageMachine

# Create your views here.


def home(request):
    machines = Machine.objects.all()
    context = {"machines": machines}
    return render(request, "body.html", context=context)
