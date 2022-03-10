from django.db.models import fields
from rest_framework import serializers
from .models import Socie, Tienda
from producto.models import Producto
from producto.serializers import ProductoSerializer


class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        fields = [
            "id",
            "nombre",
            "email",
        ]


class SocieSerializar(serializers.ModelSerializer):
    productos = ProductoSerializer(source="socie", many=True, read_only=True)
    # tiendas = TiendaSerializer(many=True)

    class Meta:
        model = Socie
        fields = [
            "id",
            # "nro_de_socie",
            "codigo",
            "apellido",
            "nombre",
            "dni",
            "email",
            "telefono",
            "domicilio",
            "codigo_postal",
            "emprendimiento",
            "descripcion",
            "fecha_de_ingreso",
            "fecha_de_egreso",
            "modo_de_egreso",
            "productos",
            "activo",
            "proveedor",
            "adherente",
        ]
        depth = 1


# class ProveedorSerializer(serializers.ModelSerializer):
#     productos = ProductoSerializer(source="proveedores", many=True, read_only=True)

#     class Meta:
#         model = Proveedor
#         fields = [
#             "id",
#             "nombre",
#             "apellido",
#             "dni",
#             "emprendimento",
#             "descripcion",
#             "email",
#             "telefono",
#             "domicilio",
#             "codigo_postal",
#             "tienda",
#             "codigo",
#             "productos",
#         ]


# class HumanesGeneralSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SocioGeneral
#         fields = [
#             "id",
#             "nombre",
#             "apellido",
#             "dni",
#             "descripcion",
#             "domicilio",
#             "codigo_postal",
#             "tienda",
#             "codigo",
#             #       "productos",
#         ]
