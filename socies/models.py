from django.db import models

# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Tienda(models.Model):
    nombre = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    email = models.CharField(
        max_length=254,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.nombre


class TipoDeSocio(models.Model):
    tipo = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.tipo


class Socie(models.Model):
    codigo = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    apellido = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    nombre = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    dni = models.CharField(max_length=9, blank=True, null=True)
    domicilio = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    telefono = models.CharField(
        max_length=17,
        default="+54 9 ",
        null=True,
        blank=True,
    )
    emprendimiento = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(
        blank=True,
        null=True,
    )
    fecha_de_ingreso = models.DateField(auto_now_add=True)
    fecha_de_egreso = models.DateField(blank=True, null=True)
    modo_de_egreso = models.CharField(max_length=10, blank=True, null=True)
    codigo_postal = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    email = models.CharField(  #
        max_length=254,
        null=True,
        blank=True,
    )

    activo = models.BooleanField(default=False)
    proveedor = models.BooleanField(default=False, null=True, blank=True)
    adherente = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ("id",)
