from django.shortcuts import render
from django.http import Http404

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from taggit.models import Tag, TaggedItem

#from caja.models import ItemVenta

from .models import Producto, TipoDeProducto, UnidadDeMedida

from .serializers import (
    ProductoSerializer,
    TipoSerializer,
    TiposNombreSerializer,
    UnidadDeMedidaSerializer,
)

# Create your views here.


class ProductosViewSet(viewsets.ModelViewSet):
    """
    API endpoint para ver y editar por productos
    """

    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        listado_productos = Producto.objects.all()
        return listado_productos



    def retrieve(self, request, *args, **kwargs):
        params = kwargs

        # Consultar a la base por ID
        productos = Producto.objects.filter(id=params["pk"])
        serializer = ProductoSerializer(productos, many=True)
        serializer = serializer.data[0]  # Lo saco de la lista
        return Response(serializer)

    def destroy(self, request, *args, **kwargs):
        producto = self.get_object()
        producto.delete()
        mensaje_respuesta = {"mensaje": "Se borró el item"}
        return Response(mensaje_respuesta)


class UnidadDeMedidaViewSet(viewsets.ModelViewSet):
    """
    API endpoint para ver y editar unidades de medida
    """

    serializer_class = UnidadDeMedidaSerializer
    queryset = UnidadDeMedida.objects.all()

    def get_queryset(self):
        listado_unidades = UnidadDeMedida.objects.all()
        return listado_unidades

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        unidades = UnidadDeMedida.objects.filter(id=params["pk"])
        serializer = UnidadDeMedidaSerializer(unidades, many=True)
        serializer = serializer.data[0]  # Lo saco de la lista
        return Response(serializer)

    def destroy(self, request, *args, **kwargs):
        unidad = self.get_object()
        unidad.delete()
        mensaje_respuesta = {"mensaje": "Se borró el item"}

        return Response(mensaje_respuesta)


class TagsViewSet(viewsets.ModelViewSet):
    serializer_class = TipoSerializer

    def get_queryset(self):
        queryset = Tag.objects.all()
        # lookup_field = 'slug'
        return queryset

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params["pk"])
        etiquetas = TipoDeProducto.objects.filter(tag_id=params["pk"])
        print(etiquetas)
        serializer_tag_id = TiposNombreSerializer(etiquetas, many=True)
        return Response(serializer_tag_id.data)
