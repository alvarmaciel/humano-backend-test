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
        return Response(serializer)

