from django.shortcuts import render
from django.http import HttpResponse
from .models import Eshkhi, User, Style
from django.db.models import Q

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""

    # clothes = Eshkhi.objects.all()
    clothes = Eshkhi.objects.filter(Q(color__icontains=q) | Q(description__icontains=q) | Q(style__name__icontains=q) )
    clothes = list(set(clothes))
    styles = Style.objects.all()
    # print((clothes[0].users.all()))
    heading = "ESHKHI"
    context = {"clothes": clothes, "heading": heading, "styles": styles}
    return render(request, 'base/home.html', context)


def about(request):
    return render(request, 'base/about.html')


def contact(request):
    return render(request, 'base/contact.html')


def profile(request, pk):
    user = User.objects.get(id=int(pk))
    q = request.GET.get('q') if request.GET.get('q') != None else ""

    clothes = user.clothes.filter(Q(color__icontains=q) | Q(description__icontains=q) | Q(style__name__icontains=q))
    clothes = list(set(clothes))

    heading = "My favourites"
    context = {'clothes': clothes, "user": user, "heading": heading}
    return render(request, 'base/profile.html', context)
