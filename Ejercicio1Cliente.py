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
    message = ["un mensaje\n", "otro mensaje\n", "mas mensajes\n", "#chau"]
    for mensaje in message:
        client.send(mensaje.encode('utf-8'))
        time.sleep(2)

def start_client():
    host = '127.0.0.1'  # Dirección IP del servidor
    port = 8090  # Puerto para la conexión

    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    receive_message()
    send_messages()


start_client()
