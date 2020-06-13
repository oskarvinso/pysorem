import socket #se importa la libreria socket
import psutil

EncBuff = 10
#AF_INET hace referencia a IPv4 SOCK_STREAM es TCP/import ipdb; ipdb.set_trace()
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.bind(('localhost', 7777)) #se define el host y el puerto
s1.listen(3)  #cantidad de clientes que puede escuchar al tiempo 3 este caso
while True: # bucle para que quede en escucha
    msg = ("Este es el porcentaje de uso de la CPU: 0%")
    msg = (f'{len(msg):<{EncBuff}}'+msg)
    clientesocket, direccion = s1.accept() #Almacenamos el socket y la direccion del cliente
    clientesocket.send(bytes(msg, "utf-8"))#Envia datos al cliente
    print(f"se ha conectado el cliente desde {direccion} \n enviando Información del procesador ....")

    while True:
        Cpu_info = psutil.cpu_percent(interval=1)
        msg = f"Este es el porcentaje de uso de la CPU: {Cpu_info}%"
        msg = (f'{len(msg):<{EncBuff}}'+msg)
        clientesocket.send(bytes(msg, "utf-8"))
