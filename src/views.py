import json

from django.http import JsonResponse
from .models import Producto

#peticion y recibe una respuesta. ruta inicial
def inicio(request):
    return JsonResponse({"mensaje": "API de productos funcionando"})

def crear_producto(request):
    #si llega una peticion que no sea GET, se ejecuta el siguiente bloque de codigo si no se manda al siguiente bloque de codigo
    if request.method == "GET":
        productos = Producto.objects.all()

        datos = []

        for producto in productos:
            datos.append({
                "nombre": producto.nombre,
                "sku": producto.sku,
                "categoria": producto.categoria,
                "precio": float(producto.precio),
                "stock": producto.stock
            })
        #False para decir que es una lista y no un diccionario
        return JsonResponse(datos, safe=False)
    #si llega una peticion que no sea POST, se ejecuta el siguiente bloque de codigo
    if request.method == "POST":
        datos = json.loads(request.body)
        

#valida que el sku no exista y que el precio sea mayor a 0
        if Producto.objects.filter(sku=datos["sku"]).exists():
            return JsonResponse({"error": "El SKU ya existe"}, status=400)
        
        if datos ["precio"] <= 0:
            return JsonResponse({"error": "El precio debe ser mayor a 0"}, status=400)


        productos = Producto.objects.create(
            nombre=datos["nombre"],
            sku=datos["sku"],
            categoria=datos["categoria"],
            precio=datos["precio"],
            stock=datos["stock"]
        )
        return JsonResponse({"create": "true"},status=200)

    return JsonResponse({"error": "Metodo no permitido"}, status=405)

#funcion para buscar por sku
def buscar_producto(request, sku):
    try:
        producto = Producto.objects.get(sku=sku)

    except Producto.DoesNotExist:
        return JsonResponse({
            "error": "Producto no encontrado"
        }, status=404)

    return JsonResponse({
        "nombre": producto.nombre,
        "sku": producto.sku,
        "categoria": producto.categoria,
        "precio": float(producto.precio),
        "stock": producto.stock,
    })

#actualizar stock y precio del producto.
def actualizar_producto(request, sku):
    if request.method != "PUT":
        return JsonResponse({"error": "Metodo no permitido"}, status=405)

    try:
        producto = Producto.objects.get(sku=sku)

    except Producto.DoesNotExist:
        return JsonResponse({
            "error": "Producto no encontrado"
        }, status=404)

    datos = json.loads(request.body)

    producto.precio = datos["precio"]
    producto.stock = datos["stock"]

    producto.save()

    return JsonResponse({
        "nombre": producto.nombre,
        "sku": producto.sku,
        "categoria": producto.categoria,
        "precio": float(producto.precio),
        "stock": producto.stock,
    })

    #eliminar producto
def eliminar_producto(request, sku):
    if request.method != "DELETE":
        return JsonResponse({"error": "Metodo no permitido"}, status=405)
    
    try:
        producto = Producto.objects.get(sku=sku)

    except Producto.DoesNotExist:
        return JsonResponse({
            "error": "Producto no encontrado"
        }, status=404)

    producto.delete()

    return JsonResponse({
        "mensaje": "Producto eliminado"
    })