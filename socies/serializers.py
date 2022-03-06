from django.db.models import fields
from rest_framework import serializers
from .models import Socie
from producto.models import Producto
from producto.serializers import ProductoSerializer


# class TiendaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tienda
#         fields = [
#             "id",
#             "nombre",
#             "email",
#         ]


class SocieSerializar(serializers.ModelSerializer):
    productos = ProductoSerializer(source="socie", many=True, read_only=True)

    class Meta:
        model = Socie
        fields = [
            "id",
            "codigo",
            "nombre",
            "apellido",
            "dni",
            "emprendimiento",
            "email",
            "descripcion",
            "telefono",
            "domicilio",
            "codigo_postal",
            "productos",
            "activo",
            "proveedor",
            "humane",
        ]
        depth = 1
