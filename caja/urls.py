from django.db import router
from django.urls import path, include
from rest_framework import routers
from caja import views

router = routers.DefaultRouter()
router.register(r"ventas", views.VentaViewSet, basename="ventas")
router.register(r"items-ventas", views.ItemVentaViewSet, basename="items-ventas")
router.register(r"salidas", views.NotaDeCreditoViewSet, basename="salidas")
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework_caja")),
]
