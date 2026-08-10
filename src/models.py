from dataclasses import dataclass


@dataclass
class Producto:
    nombre: str
    sku: str
    categoria: str
    precio: float
    stock: int