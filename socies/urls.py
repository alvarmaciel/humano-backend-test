from django.db import router
from django.urls import path, include
from rest_framework import routers
from socies import views

router = routers.DefaultRouter()
router.register(r"socies", views.SociesViewSet, basename="socies")
# router.register(r"proveedores", views.ProveedoresViewSet, basename="proveedores")
# router.register(r"general", views.HumanesGeneralViewSet, basename="general")
router.register(r"tiendas", views.TiendaViewSet, basename="tienda")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework_socies")
    ),
]
