from django.http import Http404
from django.shortcuts import render, HttpResponse
from .models import WorldBorder

# Create your views here.
def index(request):
	#paises = WorldBorder.objects.raw("SELECT id, name,area, pop2005, fips, iso2, iso3, un, region, subregion, lon, lat, mpoly FROM mundo_worldborder where name = %s", ['Brazil'])
	paises = WorldBorder.objects.raw("SELECT id, name,area, pop2005, fips, iso2, iso3, un, region, subregion, lon, lat, mpoly FROM mundo_worldborder", 0)
	context = {'paises': paises}
	return render(request, 'index.html' , context)
