from typing import Literal

from models.Producto import Producto, ProductoJoya, ProductoArte, ProductoCoche, ProductoReloj, ProductoModa
from models.Usuario import Usuario, Pujador, Administrador
from models.Subasta import Subasta
from models import Puja

from Services.Usuario_Service import UsuarioService
from Services.Puja_Service import PujaService

class SubastaService:
    def __init__(self):
        self.subastas = []
        self.usuario_service = UsuarioService()
    
    def registrar_producto(self,
                           nombre: str, 
                           categoria: Literal["Joya", "Arte", "Coche", "Reloj", "Moda"], 
                           precio_inicial: float, 
                           year: int,
                           material: str=None, 
                           quilates: int=None,
                           artista: str=None, 
                           conservacion: int=None, 
                           estilo: str=None,
                           marca: str=None, 
                           kilometraje: float=None,
                           movimiento: str=None,
                           tipo: str=None, 
                           color: str=None, estado: int=None, 
                           talla: int=None
                        ) -> Producto:
        '''
        Crea una instancia de la subclase de producto que corresponde a la categoría y devuelve el objeto
        '''
        categoria = categoria.capitalize()
        if categoria not in ["Joya", "Arte", "Coche", "Reloj", "Moda"]:
            raise ValueError("Categoría no disponible")
        
        if categoria == "Joya":
            producto = ProductoJoya(nombre=nombre, categoria=categoria, precio_inicial=precio_inicial, year=year, material=material, quilates=quilates)
        elif categoria == "Arte":
            producto = ProductoArte(nombre=nombre, categoria=categoria, precio_inicial=precio_inicial, year=year, artista=artista, conservacion=conservacion, estilo=estilo)
        elif categoria == "Coche":
            producto = ProductoCoche(nombre=nombre, categoria=categoria, precio_inicial=precio_inicial, year=year, marca=marca, kilometraje=kilometraje)
        elif categoria == "Reloj":
            producto = ProductoReloj(nombre=nombre, categoria=categoria, precio_inicial=precio_inicial, year=year, marca=marca, material=material, movimiento=movimiento)
        else:
            producto = ProductoModa(nombre=nombre, categoria=categoria, precio_inicial=precio_inicial, year=year, marca=marca, tipo=tipo, color=color, estado=estado, talla=talla)
        return producto
    
    def abrir_subasta(self, producto: Producto, administrador: Administrador) -> Subasta:
        '''
        Abre una subasta nueva si el usuario tiene permisos para ello y la añade a la lista de subastas
        '''
        if administrador.is_admin():
            subasta = Subasta(producto, administrador)
            self.subastas.append(subasta)
        else:
            raise TypeError("El usuario no tiene permisos para abrir una subasta")
        
        return subasta
    
    def buscar_subasta(self, subasta_id) -> Subasta:
        for subasta in self.subastas:
            if subasta.id == subasta_id:
                return subasta
        raise ValueError(f"No existe subasta con el ID: {subasta_id}")
    
    def pujar(self, subasta: Subasta, cantidad: float, pujador: Pujador) -> None:
        '''
        Puja por una subasta si el usuario tiene permisos para ello
        '''
        if pujador.is_admin():
            raise TypeError("Los administradores no pueden pujar")
        else:
            if self.buscar_subasta(subasta.id) != subasta:
                raise ValueError("La subasta no está registrada")
            subasta.puja_service.crear_puja(cantidad=cantidad, pujador_obj=pujador)
            
        

    def cerrar_subasta(self, subasta: Subasta, administrador: Administrador) -> None:
        '''
        Cierra la subasta si el usuario tiene permisos para ello
        '''
        if administrador.is_admin():
            subasta.cerrar_subasta()
        else:
            raise TypeError("El usuario no tiene permisos para abrir una subasta")
    
    def mostrar_subastas_activas(self) -> None:
        '''
        Muestra por pantalla las subastas que aun siguen abiertas
        '''
        print("="*30,"\n")
        print("\tSUBASTAS ACTIVAS\n")
        print("="*30,"\n")
        for subasta in self.subastas:
            if subasta.abierta:
                print("-"*30,"\n")
                print(subasta)
                print("-"*30,"\n")
    
    def mostrar_subastas_categoria(self, categoria: str):
        '''
        Muestra por pantalla las subastas filtradas por categoría
        '''
        print("="*30,"\n")
        print(f"\tSUBASTAS DE {categoria.upper()}\n")
        print("="*30,"\n")
        categoria = categoria.capitalize()
        for subasta in self.subastas:
            if subasta.producto.get_categoria() == categoria:
                print("-"*30,"\n")
                print(subasta)
                print("-"*30,"\n")