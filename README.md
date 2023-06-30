#Sockets

## Ejercicio 1
Escribir un programa **Servidor**:
- Que escuche en el puerto 80XX (XX = 00 a 99, elegir uno).
- Que cuando reciba una conexión de cliente
  - imprima localmente un mensaje idenficando al cliente (direccion y puerto)
  - le envía al cliente un mensaje con el nombre del servidor.
- Mientras esté conectado
  - Imprima localmente todos los mensajes recidos desde el cliente
  - Si recibe el mensaje "#chau" terminará la conexión y se quedará esperando a otro cliente.

Escribir un programa **Cliente**:
- Que se conecte con el Servidor en el mismo puerto
- Que envíe al servidor 4 mensajes de texto, siendo el último la cadena "#chau"

## Ejercicio 2
Modificar el programa Servidor:
- Que indique al imprimir los mensajes del cliente, una identificación del cliente que lo envió.
- Que permita multiples conexiones de cliente concurrentes.

## Ejercicio 3
Modificar el programa Cliente:
- En lugar de enviar mensajes fijos, que corra un bucle donde solicite al usuario un mensaje y lo envie al servidor.
- Que al enviar el mensaje #chau el programa termine

## Ejercicio 4
Modificar los programas Cliente y Servidor:
- El servidor re envíe a todos los clientes conectados todos los mensajes recibidos indicando de que cliente provinieron.
- El cliente debe mostrar los mensajes del servidor al tiempo de seguir reciendo mensajes por el teclado.
- Los mensajes no deben ser reenviados al cliente que los originó, solo a todos los demás. 


## Ejercicio 5
Modificar los programas Cliente y Servidor:
- El Cliente solicite al usuario que ingrese su nombre (nick)
- El Servidor identifique a los clientes por su nombre y lo incluya en los mensajes de modo de identicar de quien pesrovienen.
- El Servidor imprima localmente un mensaje identificando al hilo que está controlando.
