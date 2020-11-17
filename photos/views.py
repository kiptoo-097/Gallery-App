from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Image, Category, Location

# Create your views here.


def home(request):
    images= Image.objects.all()
    return render(request, "home.html", {"images":images})

def about(request):
    return render(request,"about.html")


def search_category(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "image": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})

def getLocation(request,location):
    locations = Image.getLocation(location)
    return render(request,'location.html',{'image':locations})