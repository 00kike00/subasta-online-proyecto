import uuid
from typing import Literal
from datetime import datetime

class Producto:

    def __init__(self, nombre: str, categoria: Literal["Joya", "Arte", "Coche", "Reloj", "Moda"], precio_inicial: float, year: int):
        # Validaciones
        if not nombre:
            raise ValueError(f"El nombre no puede estar vacío")
        if categoria.capitalize() not in ["Joya", "Arte", "Coche","Reloj", "Moda"]:
            raise ValueError(f"{categoria} no es una categoría válida")
        if precio_inicial < 0 or not isinstance(precio_inicial, (float, int)):
            raise ValueError(f"{precio_inicial} no es un valor válido")
        if year > datetime.now().year:
            raise ValueError(f"{year} no es un año válido")
        
        self.nombre = nombre
        self.categoria = categoria
        self.precio_inicial = round(precio_inicial,2)
        self.year = year
        self.id = uuid.uuid4()

    

    # Getters
    def get_id(self) -> uuid.UUID:
        return self.id
    
    def get_nombre(self) -> str:
        return self.nombre
    
    def get_categoria(self) -> str:
        return self.categoria
    
    def get_precio_inicial(self) -> float:
        return self.precio_inicial
    
    def get_year(self) -> int:
        return self.year
        
    # Método string
    def __str__(self) -> str:
        return f"ID: {self.id}\tNombre: {self.nombre}\tCategoría: {self.categoria}\tPrecio inicial: {self.precio_inicial}€\tAño: {self.year}"
    

class ProductoJoya(Producto):
    def __init__(self, nombre, categoria, precio_inicial, year, material: str, quilates: int):
        super().__init__(nombre, categoria, precio_inicial, year)
        self.material = material
        self.quilates = quilates
    
    def __str__(self):
        return super().__str__() + f"\tMaterial: {self.material}\tQuilates: {self.quilates}"

class ProductoArte(Producto):
    def __init__(self, nombre, categoria, precio_inicial, year, artista: str, conservacion: int, estilo: str):
        super().__init__(nombre, categoria, precio_inicial, year)
        self.artista = artista
        self.conservacion = conservacion
        self.estilo = estilo
    
    def __str__(self):
        return super().__str__() + f"\tArtista: {self.artista}\tConservacion: {self.conservacion}\tEstilo: {self.estilo}"

class ProductoCoche(Producto):
    def __init__(self, nombre, categoria, precio_inicial, year, marca: str, kilometraje: float):
        super().__init__(nombre, categoria, precio_inicial, year)
        self.marca = marca
        self.kilometraje = kilometraje
    
    def __str__(self):
        return super().__str__() + f"\tMarca: {self.marca}\tKilometraje: {self.kilometraje}"

class ProductoReloj(Producto):
    def __init__(self, nombre, categoria, precio_inicial, year, marca: str, material: str, movimiento: str):
        super().__init__(nombre, categoria, precio_inicial, year)
        self.marca = marca
        self.material = material
        self.movimiento = movimiento
    
    def __str__(self):
        return super().__str__() + f"\tMarca: {self.marca}\tMaterial: {self.material}\tMovimiento: {self.movimiento}"
    
class ProductoModa(Producto):
    def __init__(self, nombre, categoria, precio_inicial, year, marca: str, tipo: str, color: str, estado: int, talla: int):
        super().__init__(nombre, categoria, precio_inicial, year)
        self.marca = marca
        self.tipo = tipo
        self.color = color
        self.estado = estado
        self.talla = talla
    
    def __str__(self):
        return super().__str__() + f"\tMarca: {self.marca}\tTipo: {self.tipo}\tColor: {self.color}\tEstado: {self.estado}\tTalla: {self.talla}"
