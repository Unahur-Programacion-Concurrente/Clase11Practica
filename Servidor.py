import socket
import threading
# Servidor Genérico

# Función que maneja comunicacionescon el cliente
def handle_client(client_socket, address, port):
    try:
        message = client_socket.recv(1024).decode('utf-8')
        print(message)
    except:
        print(f"Cliente {address} desconectado")

#Funcion del servidor
def start_server():
    host = '127.0.0.1'  # Dirección IP del servidor
    port = 8090  # Puerto para la conexión

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()


    # Bucle principal
    while True:
        client_socket, address = server.accept()
        handle_client(client_socket, address, port)

#Arranca el servidor
start_server()
