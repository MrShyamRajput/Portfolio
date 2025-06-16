from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    context={
        'Technical_Skills':Technical_Skills.objects.all(),
        'Tools_and_Technologies':Tools_and_Technologies.objects.all(),
        'Interests':Interests.objects.all(),
        'Projects':Projects.objects.all(),
        'Scrollbar_imgs':Scrollar_Images.objects.all()
    }
    return render(request,"main/home.html",context)