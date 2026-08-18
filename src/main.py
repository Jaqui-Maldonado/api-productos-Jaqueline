from django.conf import settings
from django.core.management import execute_from_command_line

#inicializa la configuracion de django
settings.configure(
    DEBUG=True,
    SECRET_KEY="clave-secreta",
    ALLOWED_HOSTS=["*"],
    ROOT_URLCONF="src.urls", #decimos que las urls estan en el archivo urls.py

    INSTALLED_APPS=[
        "src.apps.SrcConfig", #decimos que la aplicacion esta en el archivo src
        "rest_framework",
        "corsheaders"


    ],

    MIDDLEWARE=[
        "corsheaders.middleware.CorsMiddleware",
        "django.middleware.common.CommonMiddleware",
    ],

     CORS_ALLOWED_ORIGINS=[
        "http://localhost:5173",
    ],

     DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "db.sqlite3",
        }
    },

    DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
 
)

if __name__ == "__main__":
    execute_from_command_line()