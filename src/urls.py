from django.urls import path
from . import views


#cuando se accede a la ruta raiz, se ejecuta la funcion inicio
urlpatterns = [

    path("", views.inicio),
    path("productos", views.crear_producto),
    path("productos/<str:sku>", views.buscar_producto), #despues de pruductos, espera el sku
    path("productos/<str:sku>/actualizar", views.actualizar_producto),
    path("productos/<str:sku>/eliminar", views.eliminar_producto),
]

