from django.shortcuts import render
from balmy_beach.models import AirT, WaterT, WaterQuality

# Create your views here.
def home_page(request):
    t_air_list = AirT.objects.last()
    t_water_list = WaterT.objects.last()
    q_water_list = WaterQuality.objects.last()
    return render(request, 'index.html', {'airtemps': t_air_list,'watertemps': t_water_list, 'waterqual': q_water_list})

    