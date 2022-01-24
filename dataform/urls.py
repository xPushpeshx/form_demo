from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('data/',views.data,name='data'),
    path('getfile/',views.getfile,name='getfile'),
]