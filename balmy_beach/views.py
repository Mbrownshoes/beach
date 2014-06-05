from django.shortcuts import render
from balmy_beach.models import AirT, WaterT, WaterQuality

# Create your views here.
def home(request):
    airt = AirT.objects.all()
    return render(request, 'index.html', {'airt': airt})