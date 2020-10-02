from django.db import models

# Create your models here.

class Familia(models.Model):
    cod_fam = models.AutoField(primary_key=True)
    nom_fam = models.CharField(max_length=30)

class Producto(models.Model):
    id_prod = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    v_compra = models.IntegerField()
    v_venta = models.IntegerField()
    marca = models.CharField(max_length=50)
    stock = models.IntegerField()
    fam = models.ForeignKey(Familia,on_delete=models.CASCADE)

class Pedido(models.Model):
    num_ped = models.AutoField(primary_key=True)