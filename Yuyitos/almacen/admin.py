from django.contrib import admin
from .models import Familia, Producto, Proveedor, Pedido, Venta, Cliente, Abono

# Register your models here.
admin.site.register(Familia)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Pedido)
admin.site.register(Venta)
admin.site.register(Cliente)
admin.site.register(Abono)