from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from . import views
from .views import SearchResultsListView,SearchLocationListView

urlpatterns=[
    path('',views.home,name='home'),
]
