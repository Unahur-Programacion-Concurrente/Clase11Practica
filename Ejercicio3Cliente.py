import socket
import time


def receive_message():
    try:
        message = client.recv(1024).decode('utf-8')
        print(message)
    except:
        print("Ha ocurrido un error al recibir el mensaje.")
        client.close()


def send_messages():
    while True:
        mensaje = input()
        client.send(mensaje.encode('utf-8'))
        if mensaje == "#chau":
            client.close()
            break

def start_client():
    host = '127.0.0.1'  # Dirección IP del servidor
    port = 8090  # Puerto para la conexión

    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    receive_message()
    send_messages()


start_client()
