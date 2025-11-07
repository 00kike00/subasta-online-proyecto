# main.py
from models.Usuario import Pujador, Administrador
from Services.Usuario_Service import UsuarioService
from Services.Subasta_Service import SubastaService

def main():
    print("\n=== SISTEMA DE SUBASTAS ONLINE ===\n")

    # Crear servicios
    usuario_service = UsuarioService()
    subasta_service = SubastaService()

    # Crear usuarios
    admin = Administrador("Laura Gómez", "laura@example.com")
    pujador1 = Pujador("Carlos Pérez", "carlos@example.com", "36201")
    pujador2 = Pujador("Marta Ruiz", "marta@example.com", "28013")

    # Registrar usuarios
    usuario_service.registrar_usuario(admin)
    usuario_service.registrar_usuario(pujador1)
    usuario_service.registrar_usuario(pujador2)

    print("\n=== Usuarios registrados ===")
    for u in usuario_service.lista_usuarios:
        print(u)
    print()

    # Registrar un producto
    producto = subasta_service.registrar_producto(
        nombre="Reloj Rolex Submariner",
        categoria="Reloj",
        precio_inicial=7500.0,
        year=2018,
        marca="Rolex",
        material="Acero inoxidable",
        movimiento="Automático"
    )

    print("\n=== 🧾 Producto registrado ===")
    print(producto)

    # Abrir una subasta
    subasta = subasta_service.abrir_subasta(producto, admin)
    print("\n=== Subasta abierta ===")
    print(subasta)

    # Realizar pujas
    print("\n=== Realizando pujas ===")
    subasta_service.pujar(subasta, 8000.0, pujador1)
    subasta_service.pujar(subasta, 8500.0, pujador2)
    subasta_service.pujar(subasta, 9000.0, pujador1)

    # Mostrar subastas activas
    print("\n=== Subastas activas ===")
    subasta_service.mostrar_subastas_activas()

    # Cerrar subasta
    print("\n=== Cerrando subasta ===")
    subasta_service.cerrar_subasta(subasta, admin)

    print("\n=== Subasta cerrada ===")
    print(subasta)

if __name__ == "__main__":
    main()
