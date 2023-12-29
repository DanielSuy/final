from django.shortcuts import render

from conocenos.models import Conocenos

# Create your views here.

def conocenos(request):
    
    conocenos=Conocenos.objects.all()
    return render(request, "conocenos/conocenos.html", {"conocenos": conocenos})
