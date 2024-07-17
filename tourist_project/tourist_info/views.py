<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import render, redirect
from .models import TouristInfo
from .forms import TouristInfoForm

# Create your views here.

def home(request):
    all_regions=TouristInfo.objects.all()

    context={'all_regions' : all_regions}
    return render(request, 'home.html', context=context)

def create_region(request):
    if request.method=="POST":
        form=TouristInfoForm(request.POST, request.FILES)
        context={'form':form}
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'create_region.html', context=context)
    else:
        form=TouristInfoForm()
        context={'form':form}
        return render(request, 'create_region.html', context=context)
>>>>>>> 8da5056bc9c0ef8474439e7ec4c9b6cc57e3e5b9
