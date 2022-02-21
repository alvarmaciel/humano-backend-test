from django.db.models import fields
from rest_framework import serializers
from .models import Producto, TipoDeProducto, UnidadDeMedida
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from taggit.models import Tag, TaggedItem, TaggedItemBase


class UnidadDeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadDeMedida
        fields = ["id", "unidad"]


class ProductoSerializer(TaggitSerializer, serializers.ModelSerializer):
    tipo = TagListSerializerField()

    class Meta:
        model = Producto
        fields = [
            "id",
            "socie",
            "nombre",
            "codigo",
            "nombre",
            "descripcion",
            "unidad",
            "precio",
            "fecha_creacion",
            "tipo",
        ]
        # depth = 1


class TiposNombreSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoDeProducto
        fields = "__all__"


class TipoSerializer(TaggitSerializer, serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ["name", "slug", "id"]
