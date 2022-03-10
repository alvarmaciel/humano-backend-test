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
    # nro_de_socie = models.IntegerField(default=0, editable=False)
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
    # categoria = models.ForeignKey(
    #     TipoDeSocio, related_name="socio_tipo", on_delete=models.CASCADE
    # )
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
    # tiendas = models.ManyToManyField(Tienda, blank=False, related_name="tienda")

    # class Meta:
    #     abstract = True

    # def __init__(self):
    #     self.fields["activo"].iniial = True

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ("id",)

    # def save(self, *args, **kwargs):
    #     self.nro_de_socie = Socie.objects.all().count() + 1
    #     super(Socie, self).save()


# class Proveedor(Humane):
#     emprendimento = models.CharField(max_length=50, blank=True, null=True)
#     tienda = models.CharField(max_length=50)
#     codigo = models.IntegerField()

#     def __str__(self):
#         return self.nombre

#     class Meta:
#         ordering = ("codigo",)


# class SocioPleno(Humane):
#     emprendimento = models.CharField(max_length=50, blank=True, null=True)
#     tienda = models.CharField(max_length=50)
#     codigo = models.IntegerField()

#     def __str__(self):
#         return self.nombre

#     class Meta:
#         ordering = ("codigo",)


# class SocioGeneral(Humane):
#     tienda = models.CharField(max_length=50)
#     codigo = models.IntegerField()

#     def __str__(self):
#         return self.nombre

#     class Meta:
#         ordering = ("codigo",)
