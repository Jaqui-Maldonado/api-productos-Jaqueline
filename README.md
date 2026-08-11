# API Descripcion

API REST desarrollada con Django para administrar un catálogo de productos para un e-commerce.

La API permite crear, consultar, actualizar y eliminar productos. La información se almacena en un archivo `productos.json`.

# Stack

-Python
-Django
-json
-github

# Instalación

# 1. Clonar el repositorio

```bash
git clone https://github.com/Jaqui-Maldonado/api-productos-Jaqueline
```

### 2. Entrar al proyecto

```bash
cd api-productos-Jaqueline
```

### 3. Crear el entorno virtual


```bash
python -m venv venv
```

### 4. Activar el entorno virtual

En PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

## Cómo ejecutar la API

Desde la carpeta raíz del proyecto:

python src/main.py runserver


# Crear producto
EJEMPLO:
Invoke-RestMethod "http://127.0.0.1:8000/productos" -Method POST -ContentType "application/json" -Body '{"nombre":"Laptop Gamer","sku":"LT-GM-001","categoria":"Tecnologia","precio":18500.50,"stock":10}'

**skuproducto** se cambia por el sku de un producto que tengan en productos.json

# Listar productos

 Invoke-RestMethod  "http://127.0.0.1:8000/productos" -Method GET


# Consultar producto por SKU

Invoke-RestMethod  "http://127.0.0.1:8000/productos/"skuproducto"" -Method GET

# Actualizar producto

Invoke-RestMethod -Uri "http://127.0.0.1:8000/productos/"skuproducto"/actualizar" -Method PUT -ContentType "application/json" -Body '{"precio":20000,"stock":15}'  

# Eliminar producto

"http://127.0.0.1:8000/productos/"skuproducto"eliminar" -Method DELETE 

