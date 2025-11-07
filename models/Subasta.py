from models.Producto import *
from models.Puja import Puja
from models.Usuario import Usuario, Pujador, Administrador
from Services.Puja_Service import PujaService
import uuid
from datetime import datetime

class Subasta:
    def __init__(self, producto: Producto, administrador: Administrador):
        self.producto = producto
        self.administrador = administrador
        self.id = uuid.uuid4()
        self.precio_inicial = producto.get_precio_inicial()
        self.fecha_inicio = datetime.now()
        self.puja_service = PujaService()
        self.abierta = True
    
    def puja_mas_alta(self) -> Puja:
        '''
        Método que devuelve la puja más alta de la lista de pujas
        '''
        if not self.puja_service.lista_pujas:
            raise ValueError(f"Aún no hay pujas en esta subasta")
        else:
            return max(self.puja_service.lista_pujas, key=lambda x: x.cantidad)

    def cerrar_subasta(self) -> None:
        '''
        Método que da por cerrada la subasta, modificando el valor de abierta a False
        '''
        if self.abierta:
            self.abierta = False
        else:
            raise ValueError(f"La subasta ya está cerrada")
    
    def __str__(self):
        estado = "Abierta" if self.abierta else "Cerrada"
        try:
            puja_alta = f"{self.puja_mas_alta().cantidad}€"
        except ValueError:
            puja_alta = "Sin pujas"
        return (f"Subasta de '{self.producto.get_nombre()}'\n"
                f"Administrador: {self.administrador.nombre}\n"
                f"Precio inicial: {self.precio_inicial}€\n"
                f"Fecha de inicio: {self.fecha_inicio.strftime('%d/%m/%Y %H:%M:%S')}\n"
                f"Cantidad de pujas: {len(self.puja_service.lista_pujas)}\n"
                f"Puja más alta: {puja_alta}€\n"
                f"Estado: {estado}")