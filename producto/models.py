from django.db import models
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from socies.models import Socie, Tienda

# Create your models here.


class TipoDeProducto(TaggedItemBase):
    content_object = models.ForeignKey(
        "Producto",
        related_name="productos_tageados",
        on_delete=models.CASCADE,
    )


class UnidadDeMedida(models.Model):
    unidad = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.unidad


class Producto(models.Model):
    socie = models.ForeignKey(
        Socie,
        related_name="socie",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )
    unidad = models.ForeignKey(
        UnidadDeMedida,
        related_name="unidades",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    tipo = TaggableManager()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    cantidad_vendida = models.IntegerField(default=0, null=True)

    class Meta:
        ordering = ("nombre",)

    def __str__(self):
        return self.nombre

    def socie_nombre(self):
        if self.socie_id is not None:
            nombre = self.humane_id.id
            return nombre
        else:
            return {}

    def nombre_producto(self):
        if self.tipo is not None:
            return self.nombre
        else:
            return {}
