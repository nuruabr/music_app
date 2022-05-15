from django.shortcuts import render
from .models import MusicsApp_Models
# Create your views here.



def all_data(request):
    data = MusicsApp_Models.objects.all()
    
    return render(request, "Home/home_page.html", {"context": data})