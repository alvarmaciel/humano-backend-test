from django.db import models

# from phonenumber_field.modelfields import PhoneNumberField (necesitamos incluir las características de Dolores para
# usar esto

# Create your models here.


# class Tienda(models.Model):
#     nombre = models.CharField(
#         max_length=50,
#         blank=True,
#         null=True,
#     )
#     email = models.CharField(
#         max_length=254,
#         null=True,
#         blank=True,
#     )

#     def __str__(self):
#         return self.nombre


class Socie(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    apellido = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    emprendimiento = models.CharField(max_length=50, blank=True, null=True)
    dni = models.CharField(max_length=9, blank=True, null=True)
    descripcion = models.TextField(
        blank=True,
        null=True,
    )
    domicilio = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    codigo_postal = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    telefono = models.CharField(
        max_length=17,
        default="+54 ",
        null=True,
        blank=True,
    )
    email = models.CharField(
        max_length=254,
        null=True,
        blank=True,
    )

    activo = models.BooleanField(default=True)
    proveedor = models.BooleanField(default=False, null=True, blank=True)
    humane = models.BooleanField(default=True, null=True, blank=True)
    #    tiendas = models.ManyToManyField(Tienda, blank=False, related_name="tienda")

    # class Meta:
    #     abstract = True

    # def __init__(self):
    #     self.fields["activo"].iniial = True

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ("codigo",)
