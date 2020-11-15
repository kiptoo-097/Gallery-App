from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from .models import Images


# Create your views here.
def home(request):
    images= Images.objects.all()
    return render(request, "home.html")

class Search(ListView):
    model = Images
    context_object_name = 'images_list'
    template_name = 'search.html'
    
