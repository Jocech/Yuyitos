from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *


# Create your views here.


def index(request):
    return render(request,'index.html',{})

def regclientes(request):
    if request.POST: 
        rut_cli = request.POST.get('rutcli',False)
        nom_cli = request.POST.get('nomcli',False)
        ape_cli = request.POST.get('apecli',False)
        direccion = request.POST.get('direcli',False)
        fono = request.POST.get('fonocli',False)
        correo = request.POST.get('correocli',False)
        c = Cliente(rut_cli=rut_cli,nom_cli=nom_cli,ape_cli=ape_cli,direccion=direccion,fono=fono,correo=correo)
        c.save()
        return HttpResponseRedirect(reverse('almacen:regclientes'))
    return render(request,'regclientes.html',{})

def regprove(request):
    if request.POST:
        rut_prov = request.POST.get('rutprove',False)
        nom_prov = request.POST.get('nomprove',False)
        email = request.POST.get('contactoprove',False)
        fono_prov = request.POST.get('fonoprove',False)
        direccion = request.POST.get('direcprove',False)
        rubro = request.POST.get('rubroprove',False)
        p = Proveedor(rut_prov=rut_prov,nom_prov=nom_prov,email=email,fono_prov=fono_prov,direccion=direccion,rubro=rubro)
        p.save()
        return HttpResponseRedirect(reverse('almacen:regprove'))
    return render(request,'regproveedores.html',{})


def regproductos(request):
    if request.POST:
        desc_prod = request.POST.get('descprodu',False)
        v_compra = request.POST.get('compraprodu',False)
        v_venta = request.POST.get('ventaprodu',False)
        marca = request.POST.get('marcaprodu',False)
        #fam = request.POST.get('codfamprodu',False)
        pr = Producto(desc_prod=desc_prod,v_compra=v_compra,v_venta=v_venta,marca = marca)#,fam = fam
        pr.save()
        return HttpResponseRedirect(reverse('almacen:regproductos'))
    return render(request,'regproductos.html', {})

def regfamilia(request):
    if request.POST:
        cod_fam = request.POST.get('codfam',False)
        nom_fam = request.POST.get('nomfam',False)
        f = Familia(cod_fam=cod_fam,nom_fam=nom_fam)
        f.save()
        return HttpResponseRedirect(reverse('almacen:regfamilia'))
    return render(request,'regfamilia.html',{})


def listar_fam(request):
    context = {
        'lista_fam' : Familia.objects.all()
    }
    return render(request, 'regproductos.html', context)

