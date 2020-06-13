import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import psutil
from itertools import count

plt.style.use('fivethirtyeight')
plt.title ('Uso de la CPU del computador remoto')
plt.xlabel ('Tiempo')
plt.ylabel ('Porcentaje uso de CPU')
val_x, val_y = [], []

index = count()

def animate(i):
    val_x.append(next(index))
    val_y.append(int(psutil.cpu_percent(interval=1)))
    plt.plot(val_x, val_y)

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
