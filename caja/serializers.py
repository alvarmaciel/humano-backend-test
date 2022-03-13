from django.db.models import fields
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from .models import Venta, ItemVenta, NotaCredito

from producto.serializers import ProductoSerializer
from .models import ItemVenta, Venta, NotaCredito
from producto.models import Producto


class ItemVentaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemVenta
        fields = [
            "venta",
            "producto",
            "cantidad",
            "parcial",
            "devolucion",
        ]


class VentaSerializer(serializers.ModelSerializer):

    items_en_venta = ItemVentaSerializer(source="items", many=True, read_only=True)

    class Meta:
        model = Venta
        fields = [
            "id",
            "cajere",
            "creado_el",
            "socie",
            "tipo_de_venta",
            "forma_de_pago",
            "items_en_venta",
            "bonificacion",
            "recargo",
            "monto_total",
        ]



class NotaDeCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaCredito
        fields = [
            "id",
            "salida",
            "humane",
            "remito_nro",
            "monto",
        ]
