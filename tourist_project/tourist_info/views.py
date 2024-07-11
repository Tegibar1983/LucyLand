from django.shortcuts import render
from .models import TouristInfo

# Create your views here.

def home(request):
    all_tourists=TouristInfo.objects.all()

    context={'all_tourists' : all_tourists}
    return render(request, 'home.html', context=context)


