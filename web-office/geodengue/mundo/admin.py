from django.contrib.gis import admin
from .models import WorldBorder, AldeiaDigital, AreasRisco, Ciclovia
from .models import LinhaOnibus, Saude, Lote, AcMunicipio, RjMunicipio

admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(AldeiaDigital, admin.OSMGeoAdmin)
admin.site.register(AreasRisco, admin.OSMGeoAdmin)
admin.site.register(Ciclovia, admin.OSMGeoAdmin)
admin.site.register(LinhaOnibus, admin.OSMGeoAdmin)
admin.site.register(Saude, admin.OSMGeoAdmin)
admin.site.register(Lote, admin.OSMGeoAdmin)
admin.site.register(AcMunicipio, admin.OSMGeoAdmin)
admin.site.register(RjMunicipio, admin.OSMGeoAdmin)

'''
admin.site.register(WorldBorder, admin.GeoModelAdmin)
login geodengue
senha 123geodengue
'''