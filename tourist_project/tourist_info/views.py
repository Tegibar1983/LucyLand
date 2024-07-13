from django.shortcuts import render
from .models import TouristInfo

# Create your views here.

def home(request):
    all_regions=TouristInfo.objects.all()

    context={'all_regions' : all_regions}
    return render(request, 'home.html', context=context)


