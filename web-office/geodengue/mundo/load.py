import os
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder, AldeiaDigital, AreasRisco, Ciclovia
from .models import LinhaOnibus, Saude, Lote, AcMunicipio, RjMunicipio

world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'mpoly' : 'MULTIPOLYGON',
}

world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'TM_WORLD_BORDERS-0.3.shp'))

def run(verbose=True):
    lm = LayerMapping(WorldBorder, world_shp, world_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)

# Auto-generated `LayerMapping` dictionary for AldeiaDigital model
aldeiadigital_mapping = {
    'name' : 'name',
    'descr' : 'descr',
    'folder' : 'folder',
    'status' : 'status',
    'situacao' : 'situacao',
    'tipo' : 'tipo',
    'geom' : 'MULTIPOINT',
}

aldeia_digital_kml = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/aldeia_digital_oficial', 'aldeia_digital_oficial.shp'))

def run_aldeia(verbose=True):
  lm = LayerMapping(AldeiaDigital, aldeia_digital_kml, aldeiadigital_mapping,
                    transform=False, encoding='ISO-8859-1')

  lm.save(strict=True, verbose=verbose)

# Auto-generated `LayerMapping` dictionary for AreasRisco model
areasrisco_mapping = {
    'solicita' : 'solicita',
    'cadastro' : 'cadastro',
    'risco' : 'risco',
    'problema' : 'problema',
    'geom' : 'MULTIPOINT',
}


areas_risco_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/areas_risco', 'areas_risco.shp'))

def run_areasrisco(verbose=True):
  lm = LayerMapping(AreasRisco, areas_risco_shp, areasrisco_mapping,
                    transform=False, encoding='ISO-8859-1')

  lm.save(strict=True, verbose=verbose)

# Auto-generated `LayerMapping` dictionary for Ciclovias model
ciclovias_mapping = {
    'id' : 'id',
    'tipo' : 'tipo',
    'geom' : 'MULTILINESTRING',
}


ciclovias_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/ciclovias', 'ciclovias.shp'))

def run_ciclovia(verbose=True):
  lm = LayerMapping(Ciclovia, ciclovias_shp, ciclovias_mapping,
                    transform=False, encoding='ISO-8859-1')

  lm.save(strict=True, verbose=verbose)

# Auto-generated `LayerMapping` dictionary for LinhaOnibus model
linhaonibus_mapping = {
    'descricao' : 'descricao',
    'empresa' : 'empresa',
    'sentido' : 'sentido',
    'n_linha' : 'n_linha',
    'descricao_field' : 'descricao_',
    'geom' : 'MULTILINESTRING',
}



linhaonibus_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/linhas_onibus', 'linhas_onibus.shp'))

def run_linhaonibus(verbose=True):
  lm = LayerMapping(LinhaOnibus, linhaonibus_shp, linhaonibus_mapping,
                    transform=False, encoding='ISO-8859-1')

  lm.save(strict=True, verbose=verbose)

# Auto-generated `LayerMapping` dictionary for Lote model
lote_mapping = {
    'cadastro' : 'cadastro',
    'observacao' : 'observacao',
    'geo_id' : 'geo_id',
    'tipo' : 'tipo',
    'num_lote' : 'num_lote',
    'testada' : 'testada',
    'geom' : 'MULTIPOLYGON',
}

lote_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/lotesvr', 'lotesvr.shp'))

def run_lote(verbose=True):
  lm = LayerMapping(Lote, lote_shp, lote_mapping,
                    transform=False, encoding='ISO-8859-1')

  lm.save(strict=True, verbose=verbose)

# Auto-generated `LayerMapping` dictionary for Saude model
saude_mapping = {
    'unidade' : 'unidade',
    'descricao' : 'descricao',
    'endereco' : 'endereco',
    'tel_ramal' : 'tel_ramal',
    'tipo' : 'tipo',
    'hora_funci' : 'hora_funci',
    'responsave' : 'responsave',
    'geom' : 'MULTIPOINT',
}

saude_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/saude_municipal', 'saude_municipal.shp'))

def run_saude(verbose=True):
  lm = LayerMapping(Saude, saude_shp, saude_mapping,
                    transform=False, encoding='ISO-8859-1')

  lm.save(strict=True, verbose=verbose)

# Auto-generated `LayerMapping` dictionary for AcMunicipio model
acmunicipio_mapping = {
    'nm_municip' : 'NM_MUNICIP',
    'cd_geocmu' : 'CD_GEOCMU',
    'geom' : 'MULTIPOLYGON',
}

acmunicipio_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/ac_municipios', '12MUE250GC_SIR.shp'))

def run_acmunicipio(verbose=True):
  lm = LayerMapping(AcMunicipio, acmunicipio_shp, acmunicipio_mapping,
                    transform=False, encoding='UTF-8')

  lm.save(strict=True, verbose=verbose)

# Auto-generated `LayerMapping` dictionary for RjMunicipio model
rjmunicipio_mapping = {
    'nm_municip' : 'NM_MUNICIP',
    'cd_geocmu' : 'CD_GEOCMU',
    'geom' : 'MULTIPOLYGON',
}

rjmunicipio_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/rj_municipios', '33MUE250GC_SIR.shp'))

def run_rjmunicipio(verbose=True):
  lm = LayerMapping(RjMunicipio, rjmunicipio_shp, rjmunicipio_mapping,
                    transform=False, encoding='UTF-8')

  lm.save(strict=True, verbose=verbose)