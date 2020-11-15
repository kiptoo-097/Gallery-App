from django.shortcuts import render
from .models import Images


# Create your views here.
def home(request):
    images= Images.objects.all()
    return render(request, "home.html")