from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.core.exceptions import *


from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status

from .models import Venta, ItemVenta, NotaCredito
from .serializers import (
    ItemVentaSerializer,
    VentaSerializer,
    NotaDeCreditoSerializer,
)

# Create your views here.


class VentaViewSet(viewsets.ModelViewSet):
    """
    API endpoint para ver y editar ventas
    """

    serializer_class = VentaSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Venta.objects.all()
        # anidado = Venta.objects.__getattribute__(id)

        return queryset

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        ventas = Venta.objects.filter(id=params["pk"])
        if ventas.exists():
            serializer = VentaSerializer(ventas, many=True)
            serializer = serializer.data[0]
            return Response(serializer)
        else:
            return HttpResponse("Exception: No hay datos de esta venta")

    def destroy(self, request, *args, **kwargs):
        venta = self.get_object()
        venta.delete()
        mensaje_respuesta = {"mensaje:" "Se Borró la venta"}
        return Response(mensaje_respuesta)

    # def create(self, request, *args, **kwargs):
    #     venta_data = request.data

    #     nueva_venta = Venta.objects.create(
    #         cajere=Venta.objects.get(id=venta_data["cajere"]),
    #         socie_humane=Venta.objects.get(id=venta_data["socioPleno"]),
    #         socie_general=Venta.objects.get(id=venta_data["socioGeneral"]),
    #         tipo_de_venta=venta_data["tipo_de_venta"],
    #         forma_de_pago=venta_data["forma_de_pago"],
    #         bonificacion=venta_data["bonificacion"],
    #         monto_pago=venta_data["monto_pago"],
    #     )

    #     nueva_venta.save()

    #     serializer = VentaSerializer(nueva_venta)
    #     return Response(serializer.data)


class ItemVentaViewSet(viewsets.ModelViewSet):
    """
    API endpoint para ver y editar Items
    """

    serializer_class = ItemVentaSerializer

    def get_queryset(self):
        listado_items = ItemVenta.objects.all()

        return listado_items

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        items = ItemVenta.objects.filter(venta=params["pk"])
        if items.exists():
            serializer = ItemVentaSerializer(items, many=True)
            return Response(serializer.data)
        else:
            return HttpResponse("Exceptions: No hay datos de este item")

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        item.delete()
        mensaje_respuesta = {"mensaje:" "Se Borró el item cargado"}
        return Response(mensaje_respuesta)

    # def create(self, request, *args, **kwargs):
    #     items_data = request.data

    #     nuevo_item = ItemVenta.objects.create(
    #         venta=ItemVenta.objects.get(id=items_data["venta"]),
    #         producto=ItemVenta.objects.get(id=items_data["producto"]),
    #         cantidad=items_data["cantidad"],
    #         sub_total=items_data["sub_total"],
    #     )

    #     nuevo_item.save()

    #     serializer = ItemVentaSerializer(nuevo_item)
    #     return Response(serializer.data)


class NotaDeCreditoViewSet(viewsets.ModelViewSet):
    """
    API endpoint para ver y editar Items
    """

    serializer_class = NotaDeCreditoSerializer

    def get_queryset(self):
        listado_items = NotaCredito.objects.all()
        return listado_items

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        items = NotaCredito.objects.filter(id=params["pk"])
        if items.exists():
            serializer = NotaDeCreditoSerializer(items, many=True)
            return Response(serializer.data)
        else:
            return HttpResponse("Exceptions: No hay datos de este item")

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        item.delete()
        mensaje_respuesta = {"mensaje:" "Se Borró el item cargado"}
        return Response(mensaje_respuesta)
