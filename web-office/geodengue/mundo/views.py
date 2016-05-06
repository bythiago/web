from django.http import Http404
from django.shortcuts import render, HttpResponse
from .models import WorldBorder

# Create your views here.
def openlayers(request):
	#paises = WorldBorder.objects.raw("SELECT id, name,area, pop2005, fips, iso2, iso3, un, region, subregion, lon, lat, mpoly FROM mundo_worldborder where name = %s", ['Brazil'])
	paises = WorldBorder.objects.raw("SELECT id, name,area, pop2005, fips, iso2, iso3, un, region, subregion, lon, lat, mpoly FROM mundo_worldborder", 0)
	context = {'paises': paises}
	return render(request, 'openlayers.html' , context)

# aldeia digital
def leafletjs(request):
	#paises = WorldBorder.objects.raw("SELECT id, name,area, pop2005, fips, iso2, iso3, un, region, subregion, lon, lat, mpoly FROM mundo_worldborder where name = %s", ['Brazil'])
	paises = WorldBorder.objects.raw("SELECT id, name, lon, lat, pop2005, mpoly FROM mundo_worldborder where name = %s", ['Brazil'])
	context = {'paises': paises}
	return render(request, 'leafletjs.html' , context)

def index(request):
	return render(request, 'index.html')

