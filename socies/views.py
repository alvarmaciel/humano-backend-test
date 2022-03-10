from django.shortcuts import render
from django.http import Http404

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status

from .models import Tienda, Socie
from .serializers import TiendaSerializer, SocieSerializar


class SociesViewSet(viewsets.ModelViewSet):
    """
    API endpoint para ver y editar por humane
    """

    serializer_class = SocieSerializar
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Socie.objects.all()
        return queryset

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        humane = Socie.objects.filter(id=params["pk"])
        serializer = SocieSerializar(humane, many=True)
        serializer = serializer.data[0]
        return Response(serializer)

    # def create(self, request, *args, **kwargs):
    #     data = request.data

    #     nuevo_socie = Socie.objects.create(
    #         codigo=data["codigo"],
    #         nombre=data["nombre"],
    #         apellido=data["apellido"],
    #         emprendimiento=data["emprendimiento"],
    #         dni=data["dni"],
    #         descripcion=data["descripcion"],
    #         domicilio=data["domicilio"],
    #         codigo_postal=data["codigo_postal"],
    #         telefono=data["telefono"],
    #         email=data["email"],
    #         activo=data["activo"],
    #         proveedor=data["proveedor"],
    #         humane=data["humane"],
    #     )
    #     nuevo_socie.save()

    #     for tienda in data["tiendas"]:
    #         tienda_object = Tienda.objects.get(nombre=tienda["nombre"])
    #         nuevo_socie.tiendas.add(tienda_object)

    #     serializers = SocieSerializar(nuevo_socie)

    #     return Response(serializers.data)

    # def update(self, request, *args, **kwargs):
    #     socie_object = self.get_object()
    #     data = request.data

    #     socie_object.codigo = data["codigo"]
    #     socie_object.nombre = data["nombre"]
    #     socie_object.apellido = data["apellido"]
    #     socie_object.emprendimiento = data["emprendimiento"]
    #     socie_object.dni = data["dni"]
    #     socie_object.descripcion = data["descripcion"]
    #     socie_object.domicilio = data["domicilio"]
    #     socie_object.codigo_postal = data["codigo_postal"]
    #     socie_object.telefono = data["telefono"]
    #     socie_object.email = data["email"]
    #     socie_object.activo = data["activo"]
    #     socie_object.proveedor = data["proveedor"]
    #     socie_object.humane = data["humane"]
    #     socie_object.tiendas.set("")

    #     for tienda in data["tiendas"]:
    #         nueva_tienda = Tienda.objects.get(nombre=tienda["nombre"])
    #         socie_object.tiendas.add(nueva_tienda)

    #     socie_object.save()
    #     serializers = SocieSerializar(socie_object)

    #     return Response(serializers.data)

    # def partial_update(self, request, *args, **kwargs):
    #     socie_object = self.get_object()
    #     data = request.data

    #     try:
    #         if request.data.get("tiendas"):
    #             socie_object.tiendas.set("")
    #             for tienda in data["tiendas"]:
    #                 nueva_tienda = Tienda.objects.get(nombre=tienda["nombre"])
    #                 socie_object.tiendas.add(nueva_tienda)
    #     except KeyError:
    #         pass

    #     socie_object.codigo = data.get("codigo", socie_object.codigo)
    #     socie_object.nombre = data.get("nombre", socie_object.nombre)
    #     socie_object.apellido = data.get("apellido", socie_object.apellido)
    #     socie_object.emprendimiento = data.get(
    #         "emprendimiento", socie_object.emprendimiento
    #     )
    #     socie_object.dni = data.get("dni", socie_object.dni)
    #     socie_object.descripcion = data.get("descripcion", socie_object.descripcion)
    #     socie_object.domicilio = data.get("domicilio", socie_object.domicilio)
    #     socie_object.codigo_postal = data.get(
    #         "codigo_postal", socie_object.codigo_postal
    #     )
    #     socie_object.telefono = data.get("telefono", socie_object.telefono)
    #     socie_object.email = data.get("email", socie_object.email)
    #     socie_object.activo = data.get("activo", socie_object.activo)
    #     socie_object.proveedor = data.get("proveedor", socie_object.proveedor)
    #     socie_object.humane = data.get("humane", socie_object.humane)

    #     socie_object.save()
    #     serializers = SocieSerializar(socie_object)

    #     return Response(serializers.data)


class TiendaViewSet(viewsets.ModelViewSet):
    """
    API endpoint para ver y editar por humane
    """

    serializer_class = TiendaSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Tienda.objects.all()
        return queryset

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        tienda = Tienda.objects.filter(id=params["pk"])
        serializer = TiendaSerializer(tienda, many=True)
        serializer = serializer.data[0]
        # serializer = serializer.data[0]
        return Response(serializer)


# class ProveedoresViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint para ver y editar por Proveedor
#     """

#     serializer_class = ProveedorSerializer
#     # permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         queryset = Proveedor.objects.all()
#         return queryset

#     def retrieve(self, request, *args, **kwargs):
#         params = kwargs
#         print(params["pk"])
#         proveedor = Proveedor.objects.filter(codigo=params["pk"])
#         serializer = ProveedorSerializer(proveedor, many=True)
#         serializer = serializer.data[0]
#         return Response(serializer)


# class HumanesGeneralViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint para ver y editar por humane
#     """

#     serializer_class = HumanesGeneralSerializer
#     # permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         queryset = SocioGeneral.objects.all()  # TODO
#         return queryset

#     def retrieve(self, request, *args, **kwargs):
#         params = kwargs
#         print(params["pk"])
#         humane = SocioGeneral.objects.filter(id=params["pk"])
#         serializer = HumanesGeneralSerializer(humane, many=True)
#         serializer = serializer.data[0]
#         return Response(serializer)
