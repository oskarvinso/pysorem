import socket
import psutil
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 1234))
s.listen(3)
print ("Esperando conexión por parte de un cliente.....")
cli, dir = s.accept()
print(f"se conecto el cliente desde {dir}")
while True:
    CPU_val = str(psutil.cpu_percent(interval=1))
    cli.send(bytes(CPU_val,"utf-8"))
