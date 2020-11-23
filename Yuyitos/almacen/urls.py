from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from . import views

app_name = "almacen"

urlpatterns = [
    path('', views.index, name='index'),
    path('registro_clientes/', views.regclientes, name='regclientes'),
    path('registro_proveedores/', views.regprove, name='regprove'),
    path('registro_productos/', views.regproductos, name='regproductos'),
    path('registro_familia/', views.regfamilia, name='regfamilia'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
