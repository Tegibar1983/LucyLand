from django.shortcuts import render, redirect
from .models import TouristInfo
from .forms import TouristInfoForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

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

def read_more(request, pk):
    region=TouristInfo.objects.get(id=pk)
    context={'region':region}
    return render(request, 'read_more.html', context=context)


def update_region(request, pk):
    region=TouristInfo.objects.get(id=pk)
    form=TouristInfoForm(instance=region)
    if request.method=="POST":
        form=TouristInfoForm(request.POST, request.FILES, instance=region)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.success(request, 'Sorry Region information is not updated due to invalid form submission')
            return render(request, 'update_region.html', context=context)
    else:
        context={'form':form}
        return render(request, 'update_region.html', context=context)
    


def delete_region(request, pk):
    region=TouristInfo.objects.get(id=pk)
    if request.method=="POST":
        region.delete()
        messages.success(request, 'Region information is deleted successfully')
        return redirect('home')
    else:
        context={'region':region}
        return render(request, 'delete_region.html', context=context)
    


def register_user(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        context={'form':form}
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'register_user.html', context=context)
    else:
        form=UserCreationForm()
        context={'form':form}
        return render(request, 'register_user.html', context=context)