from django.db import models

# Create your models here.

class Familia(models.Model):
    cod_fam = models.AutoField(primary_key=True)
    nom_fam = models.CharField(max_length=30)

class Producto(models.Model):
    id_prod = models.AutoField(primary_key=True)
    desc_prod = models.CharField(max_length=50)
    v_compra = models.IntegerField()
    v_venta = models.IntegerField()
    marca = models.CharField(max_length=50)
    #stock = models.IntegerField()
    fam = models.ForeignKey(Familia,on_delete=models.CASCADE)

class Proveedor(models.Model):
    rut_prov = models.CharField(primary_key=True,max_length=10)
    nom_prov = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    fono_prov = models.IntegerField()
    direccion = models.CharField(max_length=50)
    rubro = models.CharField(max_length=50)

class Pedido(models.Model):
    num_ped = models.AutoField(primary_key=True)
    fec_ped = models.DateField(auto_now = False, auto_now_add = False)
    desc_ped = models.CharField(max_length=50)
    total_ped = models.IntegerField()
    prov = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    prod = models.ForeignKey(Producto,on_delete=models.CASCADE)

class Venta(models.Model):
    n_boleta = models.AutoField(primary_key=True)
    acredito = models.BooleanField()
    fec_boleta = models.DateField(auto_now=False,auto_now_add=False)
    total_boleta = models.IntegerField()
    estado = models.CharField(max_length=10)
    prod = models.ForeignKey(Producto,on_delete=models.CASCADE)

class Cliente(models.Model):
    rut_cli = models.CharField(max_length=10)
    nom_cli = models.CharField(max_length=30)
    ape_cli = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    fono = models.IntegerField()
    correo = models.CharField(max_length=50)

class Abono(models.Model):
    fec_abono = models.DateField(auto_now=False,auto_now_add=False)
    cant_abono = models.IntegerField()
    deuda = models.IntegerField()
    cli = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    n_bole = models.ForeignKey(Venta, on_delete=models.CASCADE)
