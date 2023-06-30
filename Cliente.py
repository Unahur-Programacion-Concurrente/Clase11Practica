import socket
import time

# Cliente "Genérico"

# Función que maneja la recepción de mensajes
def receive_message():
    try:
        message = client.recv(1024).decode('utf-8')
        print(message)
    except:
        print("Ha ocurrido un error al recibir el mensaje.")
        client.close()

# Función que maneja la transmisión de mensajes
def send_messages():
        client.send(mensaje.encode('utf-8'))

# Función que arranca el cliente.
def start_client():
    host = '127.0.0.1'  # Dirección IP del servidor
    port = 8090  # Puerto para la conexión

    global client, mensaje
    #Crea el socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Inicia la conexion
    client.connect((host, port))

    #Recibe mensajes
    receive_message()
    #Transmite mensajes
    send_messages()

#Arranca el cliente
start_client()
