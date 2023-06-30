import socket
import threading

def handle_client(client_socket, address, port):
    mensajeInicial = f'Hola {address}, soy el servidor {socket.gethostname()} en port {port}'
    client_socket.send(mensajeInicial.encode('utf-8'))
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message != "#chau":
                print(f'Cliente {address} envio: {message}')
            else:
                print(f"Cliente {address} terminó")
                client_socket.close()
                break
        except:
            print(f"Cliente {address} desconectado")
            break


def start_server():
    host = '127.0.0.1'  # Dirección IP del servidor
    port = 8090  # Puerto para la conexión

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print("El servidor está escuchando en el puerto", port)

    # Bucle principal
    while True:
        client_socket, address = server.accept()
        print(f"Cliente {address} conectado.")
        thread = threading.Thread(target=handle_client, args=(client_socket, address, port))
        thread.start()

start_server()
