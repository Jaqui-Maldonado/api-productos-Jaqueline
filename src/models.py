from dataclasses import dataclass

#Crea clases que guardan los datos de forma rapida y sencilla
@dataclass
class Producto:
    nombre: str
    sku: str
    categoria: str
    precio: float
    stock: int