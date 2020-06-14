import socket
import os
import argparse
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count

parser = argparse.ArgumentParser(description='Monitor de CPU')
parser.add_argument('host', help="Escriba la direccion IP del computador remoto", type=str)
argu = parser.parse_args()
host = argu.host
print (f"intentando conectar con {host}....")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, 1235))

plt.style.use('fivethirtyeight')
plt.title (f"Uso de la CPU del computador remoto {host}")
plt.xlabel ('Tiempo')
plt.ylabel ('Porcentaje uso de CPU')
plt.tight_layout()
val_x, val_y = [], []

index = count()

def AnimoGrafica(i):
    CPU_val = s.recv(20)
    CPU_val = CPU_val.decode("utf-8")
    CPU_val = int(float(CPU_val))
    os.system("clear")
    print(f"El Porcentaje de uso de la CPU es: {CPU_val}%")
    val_x.append(next(index))
    val_y.append(CPU_val)
    plt.plot(val_x, val_y)

ani = FuncAnimation(plt.gcf(), AnimoGrafica, interval=1000)

plt.tight_layout()
plt.show()
