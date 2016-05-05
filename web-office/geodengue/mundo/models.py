from django.contrib.gis.db import models

class WorldBorder(models.Model):
  # Regular Django fields corresponding to the attributes in the
  # world borders shapefile.
  name = models.CharField(max_length=50)
  area = models.IntegerField()
  pop2005 = models.IntegerField('Population 2005')
  fips = models.CharField('FIPS Code', max_length=2)
  iso2 = models.CharField('2 Digit ISO', max_length=2)
  iso3 = models.CharField('3 Digit ISO', max_length=3)
  un = models.IntegerField('United Nations Code')
  region = models.IntegerField('Region Code')
  subregion = models.IntegerField('Sub-Region Code')
  lon = models.FloatField()
  lat = models.FloatField()

  # GeoDjango-specific: a geometry field (MultiPolygonField)
  mpoly = models.MultiPolygonField()

  # Returns the string representation of the model.
  def __str__(self):              # __unicode__ on Python 2
      return self.name

#AldeiaDigital
class AldeiaDigital(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    name = models.CharField(max_length=254)
    descr = models.CharField(max_length=254)
    folder = models.CharField(max_length=254)
    status = models.CharField(max_length=254)
    situacao = models.CharField(max_length=254)
    tipo = models.CharField(max_length=255)
    geom = models.MultiPointField(srid=4326)

    def __str__(self):
        return self.name

#AreasRisco
class AreasRisco(models.Model):
    solicita = models.CharField(max_length=254)
    cadastro = models.CharField(max_length=254)
    risco = models.CharField(max_length=254)
    problema = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)

    def __str__(self):
        return self.risco

class Ciclovia(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    tipo = models.CharField(max_length=254)
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self):
        return self.tipo

class LinhaOnibus(models.Model):
    descricao = models.CharField(max_length=254)
    empresa = models.CharField(max_length=254)
    sentido = models.CharField(max_length=254)
    n_linha = models.CharField(max_length=254)
    descricao_field = models.CharField(max_length=254)
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self):
        return '{} - {}'.format(self.empresa, self.descricao)

class Saude(models.Model):
    unidade = models.IntegerField()
    descricao = models.CharField(max_length=254)
    endereco = models.CharField(max_length=254)
    tel_ramal = models.CharField(max_length=254)
    tipo = models.CharField(max_length=254)
    hora_funci = models.CharField(max_length=254)
    responsave = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)

    def __str__(self):
        return self.descricao


class Lote(models.Model):
    cadastro = models.FloatField()
    observacao = models.CharField(max_length=254)
    geo_id = models.FloatField()
    tipo = models.FloatField()
    num_lote = models.CharField(max_length=254)
    testada = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return '{} {}'.format(self.num_lote, self.testada)

class AcMunicipio(models.Model):
    nm_municip = models.CharField(max_length=60)
    cd_geocmu = models.CharField(max_length=7)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.nm_municip.encode('utf8')

class RjMunicipio(models.Model):
    nm_municip = models.CharField(max_length=60)
    cd_geocmu = models.CharField(max_length=7)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.nm_municip.encode('utf8')
# IMPORTANT
#('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),