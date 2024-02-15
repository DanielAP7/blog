from django.shortcuts import render
from blogap.models import entrada

# Create your views here.
def home(request):
    blogap = entrada.objects.all()
    return render(request, "hola.html", {"blogap":blogap})