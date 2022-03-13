from django.db.models import fields
from rest_framework import serializers
from .models import Producto, TipoDeProducto, UnidadDeMedida
from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from taggit.models import Tag


class UnidadDeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadDeMedida
        fields = ["id", "unidad"]

class TiposNombreSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoDeProducto
        fields = "__all__"


class TipoSerializer(TaggitSerializer, serializers.ModelSerializer):


    class Meta:
        model = Tag
        # fields = ["id", "object_id", "content_type_id", "tag_id", "productos"]
        fields = ["name", "slug", "id"]


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


