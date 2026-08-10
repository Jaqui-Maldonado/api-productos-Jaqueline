import json
from pathlib import Path

from django.http import JsonResponse
from django.urls import path
from django.conf import settings
from django.core.management import execute_from_command_line

#inicializa la configuracion de django
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY="clave-secreta",
    ALLOWED_HOSTS=["*"],
)
#define la ruta del archivo productos.json
ARCHIVO_PRODUCTOS = Path(__file__).parent.parent / "productos.json"

#lee productos (funciones)
def obtener_productos():
    with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

#guarda informacion en productos.json (funciones)
def guardar_productos(productos):
    with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, ensure_ascii=False, indent=4)

#peticion y recibe una respuesta.
def inicio(request):
    return JsonResponse({"mensaje": "API de productos funcionando"})

def crear_producto(request):
    #si llega una peticion que no sea GET, se ejecuta el siguiente bloque de codigo si no se manda al siguiente bloque de codigo
    if request.method == "GET":
        productos = obtener_productos()
        #False para decir que es una lista y no un diccionario
        return JsonResponse(productos, safe=False)
    #si llega una peticion que no sea POST, se ejecuta el siguiente bloque de codigo
    if request.method == "POST":
        datos = json.loads(request.body)

        productos = obtener_productos()
        productos.append(datos) #se agrega el nuevo producto a la lista de productos existentes
        guardar_productos(productos)
    #respuesta con un mensaje de exito
        return JsonResponse(datos, status=201)

    return JsonResponse({"error": "Metodo no permitido"}, status=405)

#funcion para buscar por sku
def buscar_producto(request, sku):
    productos = obtener_productos()

    for producto in productos:
        if producto["sku"] == sku:
            return JsonResponse(producto)
        
        return JsonResponse({"error": "Producto no encontrado"}, status=404)

    
#cuando se accede a la ruta raiz, se ejecuta la funcion inicio
urlpatterns = [
    path("", inicio),
    path("productos", crear_producto),
    path("productos/<str:sku>", buscar_producto), #despues de pruductos, espera el sku

]


if __name__ == "__main__":
    execute_from_command_line()