from django.contrib import admin
from .models import ItemVenta, Venta, NotaCredito

# Register your models here.
admin.site.register(Venta)
admin.site.register(ItemVenta)
admin.site.register(NotaCredito)
