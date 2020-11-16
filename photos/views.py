from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from .models import Images


# Create your views here.
def home(request):
    images= Images.objects.all()
    return render(request, "index.html", {"images":images})


class Search(ListView):
    model = Images
    context_object_name = 'images_list'
    template_name = 'search.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        if Images.objects.filter(Q(image_category=query)):
            return Images.objects.filter(Q(image_category=query))

class SearchLocation(ListView):
    model = Images
    context_object_name = 'images_list'
    template_name = 'location.html'
    

    def get_queryset(self): 
        query = self.request.GET.get('q')
        if Images.objects.filter(Q(image_location=query)):
            return Images.objects.filter(Q(image_location=query))

