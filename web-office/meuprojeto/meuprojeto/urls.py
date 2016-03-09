"""meuprojeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))

Meu Exemplo [https://docs.djangoproject.com/en/1.9/intro/tutorial03/]
[http://10.1.3.156:8000/detalhes/1/]
url(r'^$', views.index),
url(r'^detalhes/(?P<id>[0-9]+)/$', views.detalhes, name='detalhes'),
"""


from django.conf.urls import include, url
from django.contrib import admin
from pessoa import views

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.index),
	url(r'^detalhes/(?P<id>[0-9]+)/$', views.detalhes, name='detalhes'),
 	url(r'^cadastro/', views.cadastro, name='cadastro'),
	url(r'^editar/(?P<id>[0-9]+)/$', views.editar, name='editar'),
	#url(r'^cadastro/$', views.cadastro, name='cadastro'),
]
