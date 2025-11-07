from datetime import datetime
from models.Usuario import Pujador

import uuid

class Puja:
    def __init__(self, id_pujador: uuid, cantidad: float):
        if cantidad < 0 or type(cantidad) != float:
            raise ValueError("Valor de cantidad no válido")
        self.id_pujador = id_pujador
        self.cantidad = round(cantidad,2)
        self.fecha_hora = datetime.now()

    def __str__(self):
        return f"Puja con valor de {self.cantidad}€ realizada por {self.id_pujador} con fecha: {self.fecha_hora}"
