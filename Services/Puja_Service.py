from models.Puja import Puja
from models.Usuario import Pujador

class PujaService:
    def __init__(self):
        self.lista_pujas=[]

    def obtener_ultima_puja(self):
        if not self.lista_pujas:
            return None
        return self.lista_pujas[-1]
        
    def crear_puja(self, pujador_obj, cantidad) -> Puja:
        if not isinstance(pujador_obj, Pujador):
            print("El pujador no es valido")
            return None
        try:
            cantidad_val=float(cantidad)
        except(ValueError, TypeError):
            print("La cantidad debe de ser un numero")
            return None
    

        ultima=self.obtener_ultima_puja()
        if ultima is not None and cantidad_val<=ultima.cantidad:
            print(f"Puja no aceptada. La cantidad de la puja debe superar ({ultima.cantidad}€)")



        nueva_puja=Puja(pujador_obj.id_usuario, cantidad_val)
        self.lista_pujas.append(nueva_puja)
        print(f"Puja aceptada {nueva_puja}")
        return nueva_puja