import uuid

class Usuario:
    def __init__(self, nombre, correo):
        self.id_usuario = uuid.uuid4()
        self.nombre = nombre
        self.correo = correo

    def is_admin(self):
        """
        Devuelve False por defecto, ya que un usuario normal no es administrador.
        """
        return False

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario}, Email: {self.correo})"


class Pujador(Usuario):
    def __init__(self, nombre, correo, codigo_postal):
        super().__init__(nombre, correo)
        self.codigo_postal = codigo_postal

    def __str__(self):
        return f"Pujador: {self.nombre} (ID: {self.id_usuario}, CP: {self.codigo_postal})"


class Administrador(Usuario):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)

    def is_admin(self):
        """
        Sobrescribe el método para indicar que el usuario es administrador.
        """
        return True

    def __str__(self):
        return f"Administrador: {self.nombre} (ID: {self.id_usuario})"