from django.db import models
from django.contrib.auth.models import User
from producto.models import Producto
from taggit.managers import TaggableManager
from socies.models import Socie, Tienda
from decimal import Decimal


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
    # socie_general = models.ForeignKey(
    #     SocioGeneral,
    #     related_name="socioGeneral",
    #     on_delete=models.PROTECT,
    #     null=True,
    #     blank=True,
    # )
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
    bonificacion = models.DecimalField(
        max_digits=9, decimal_places=2, blank=True, null=True, default=0
    )

    recargo = models.DecimalField(
        max_digits=9, decimal_places=2, blank=True, null=True, default=0
    )

    monto_total = models.DecimalField(
        max_digits=9, decimal_places=2, blank=True, null=True, default=0
    )

    class Meta:
        ordering = [
            "-creado_el",
        ]

    def __str__(self):
        return 'cliente "%s" nro venta "%s"' % (self.socie, self.id)

    # def set_bonificacion(self):
    #     if self.tipo_de_venta != "Humane":
    #         self.bonificacion = 0
    #         return self.bonificacion
    #     else:
    #         self.bonificacion = 20
    #         return self.bonificacion

    # def set_recargo(self):
    #     if self.forma_de_pago == "Tarjeta" or self.forma_de_pago == "Mercado Pago":
    #         self.recargo = 10
    #         return self.recargo
    #     else:
    #         self.recargo = 0
    #         return self.recargo

    # def get_monto_total(self):
    #     items_vendidos = Venta.objects.get(id=self.id).items.all()
    #     total_ventas = 0
    #     for e in items_vendidos:
    #         total_ventas += e.parcial
    #     # self.set_bonificacion()
    #     self.set_recargo()
    #     bonificacion = total_ventas * (self.bonificacion / Decimal(100))
    #     recargo = total_ventas * (self.recargo / Decimal(100))
    #     self.monto_total = total_ventas - bonificacion + recargo
    #     return total_ventas

    # def save(self, *args, **kwargs):
    #     if Venta.objects.filter(id=self.id).exists():
    #         self.get_monto_total()
    #     super(Venta, self).save(*args, **kwargs)


class ItemVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name="items", on_delete=models.CASCADE)
    producto = models.ForeignKey(
        Producto, related_name="producto_elegido", on_delete=models.CASCADE
    )
    cantidad = models.IntegerField(default=1)
    parcial = models.DecimalField(
        max_digits=9, decimal_places=2, default=0, blank=True, null=True
    )
    devolucion = models.BooleanField(default=False)

    def __str__(self):
        return "venta %s prducto %s item %s" % (self.venta.id, self.producto, self.id)

    # @property
    # def parcial(self):
    #     return self.cantidad * self.producto.precio

    # def get_cantidad(self):
    #      cantidad = self.cantidad
    #      return cantidad

    # def actualizar_monto_venta(self):
    #     ventas = ItemVenta.objects.filter(venta=self.venta)
    #     for i in ventas:
    #         i.venta.get_monto_total()

    # def save(self, *args, **kwargs):
    #     precio_unitario = self.producto.precio
    #     self.parcial = self.producto.precio * self.cantidad
    #     # self.actualizar_monto_venta()
    #     super(ItemVenta, self).save(*args, **kwargs)


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
    # gasto_diario = models.CharField(max_length=50)
    creado_el = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = [
            "-creado_el",
        ]

    def __str__(self):
        return "%s" % self.salida
