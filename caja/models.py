from django.db import models
from django.contrib.auth.models import User
from producto.models import Producto
from taggit.managers import TaggableManager
from socies.models import Socie, Tienda


class Venta(models.Model):
    cajere = models.ForeignKey(
        User, related_name="cajere", on_delete=models.CASCADE, null=True
    )
    creado_el = models.DateTimeField(auto_now_add=True)
    tipos_de_venta = [
        ("Humane", "Hum"),
        ("General", "Gen"),
    ]
    # items = models.ManyToManyRel("ItemVenta")
    socie = models.ForeignKey(
        Socie,
        related_name="socies",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    tipo_de_venta = models.CharField(max_length=7, choices=tipos_de_venta, null=True)
    formas_de_pago = [
        ("Efectivo", "Efectivo"),
        ("Moneda Par", "Moneda Par"),
        ("Tarjeta", "tarjeta"),
        ("Debito", "Debito"),
        ("Transferencia", "Transferencia"),
        ("Humane", "Humane"),
        ("Mercado Pago", "MP"),
    ]
    forma_de_pago = models.CharField(max_length=15, choices=formas_de_pago, null=True)
    bonificacion = models.IntegerField(default=0)
    monto_pago = models.DecimalField(
        max_digits=9, decimal_places=2, blank=True, null=True, default=0
    )

    class Meta:
        ordering = [
            "-creado_el",
        ]

    def __str__(self):
        return 'cliente "%s" nro venta "%s"' % (self.socie, self.id)



class ItemVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name="items", on_delete=models.CASCADE)
    producto = models.ForeignKey(
        Producto, related_name="producto_elegido", on_delete=models.CASCADE
    )
    cantidad = models.IntegerField(default=1)
    sub_total = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    devolucion = models.BooleanField(default=False)

    def __str__(self):
        return "venta %s prducto %s item %s" % (self.venta.id, self.producto, self.id)



class NotaCredito(models.Model):
    tipo_de_salida = [
        ("Humane", "Humane"),
        ("Pago Proveedores", "Proveedor"),
        ("Diferencia de caja", "Diferencia de caja"),
        ("Gasto Diario", "Gasto Diario"),
    ]
    salida = models.CharField(
        max_length=20, choices=tipo_de_salida, default="Proveedor"
    )
    humane = models.ForeignKey(Socie, on_delete=models.PROTECT, null=True, blank=True)
    remito_nro = models.CharField(max_length=50, null=True, blank=True)
    creado_el = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = [
            "-creado_el",
        ]

    def __str__(self):
        return "%s" % self.salida
