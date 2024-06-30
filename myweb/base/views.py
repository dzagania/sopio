from django.shortcuts import render
from django.http import HttpResponse
from .models import Eshkhi, User

def home(request):
    clothes = Eshkhi.objects.all()
    context = {"clothes": clothes}
    return render(request, 'base/home.html', context)


def about(request):
    return render(request, 'base/about.html')


def contact(request):
    return render(request, 'base/contact.html')


def profile(request, pk):
    user = User.objects.get(id=int(pk))
    clothes = user.clothes.all()
    context = {'clothes': clothes, "user": user}
    return render(request, 'base/profile.html', context)
