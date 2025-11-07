from models.Usuario import Usuario, Pujador, Administrador

class UsuarioService:
    def __init__(self):
        self.lista_usuarios = []

    def registrar_usuario(self, usuario):
        """
        Registra un nuevo usuario (Administrador o Pujador) en el sistema.
        """
        self.lista_usuarios.append(usuario)
        print(f"Usuario registrado correctamente: {usuario.nombre}")

    def obtener_usuario_por_id(self, id_usuario) -> Usuario:
        """
        Devuelve un usuario por su identificador, si existe.
        """
        for usuario in self.lista_usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        raise ValueError("El id de usuario no existe")


# Ejemplo de uso del servicio
if __name__ == "__main__":
    usuario_service = UsuarioService()

    # Crear y registrar un pujador
    pujador1 = Pujador(1, "Carlos Pérez", "carlos@example.com", "36201")
    usuario_service.registrar_usuario(pujador1)

    # Crear y registrar un administrador
    admin1 = Administrador(2, "Laura Gómez", "laura@example.com")
    usuario_service.registrar_usuario(admin1)

    # Consultar usuarios por ID
    usuario = usuario_service.obtener_usuario_por_id(1)
    if usuario:
        print(usuario)

    admin = usuario_service.obtener_usuario_por_id(2)
    if admin:
        print(f"¿Es admin? {admin.is_admin()}")