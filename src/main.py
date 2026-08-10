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
    if request.method != "POST":
        return JsonResponse({"error": "Metodo no permitido"}, status=405)
#lee el contenido del cuerpo de la solicitud y lo convierte en un diccionario de Python
    datos = json.loads(request.body)
#verifica que los campos requeridos esten presentes en los datos recibidos y sean existentes
    productos = obtener_productos()
    productos.append(datos) #se agrega el nuevo producto a la lista de productos existentes
    guardar_productos(productos)
#respuesta con un mensaje de exito
    return JsonResponse(datos, status=201)

#cuando se accede a la ruta raiz, se ejecuta la funcion inicio
urlpatterns = [
    path("", inicio),
    path("productos", crear_producto),
]


if __name__ == "__main__":
    execute_from_command_line()