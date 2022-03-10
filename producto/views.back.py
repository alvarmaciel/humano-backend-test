from django.shortcuts import render
from django.http import Http404

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Producto
from .serializers import ProductoSerializer
# Create your views here.

class ListProductoView(APIView):
    """
    View para listar todos los productos en el sitema
    * no requiere autenticación
    """

    def get(self, request, format = None):
        """
        Devuelve la lista de productos
        """
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response (serializer.data)

class UpdateDeleteProductoView(APIView):
    """
    View para modificar base de datos
    * post, put, patch, delete requiere autenticación
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request, format = None):
        """
        Devuelve la lista de productos
        """
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, format=None):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None):
        productos = Producto.objects.all()
        Producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

