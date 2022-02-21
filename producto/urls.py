from django.db import router
from django.urls import path, include
from rest_framework import routers
from producto import views

router = routers.DefaultRouter()
router.register(r"productos", views.ProductosViewSet, basename="productos")
router.register(r"tipos", views.TagsViewSet, basename="tipos")
router.register("unidades", views.UnidadDeMedidaViewSet, basename="unidades")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework_producto")
    ),
]
