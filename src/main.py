from django.http import JsonResponse
from django.urls import path
from django.conf import settings
from django.core.management import execute_from_command_line

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY="clave-secreta",
    ALLOWED_HOSTS=["*"],
)

#peticion y recibe una respuesta
def inicio(request):
    return JsonResponse({"mensaje": "API de productos funcionando"})

#cuando se accede a la ruta raiz, se ejecuta la funcion inicio
urlpatterns = [
    path("", inicio),
]


if __name__ == "__main__":
    execute_from_command_line()