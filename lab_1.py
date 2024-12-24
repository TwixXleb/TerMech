import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Функции для r и fi
def r(t):
    return 1 + np.sin(t)

def fi(t):
    return t

# Создаем массив значений t
t_values = np.linspace(0, 2 * np.pi, 100)

# Создаем фигуру и оси
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
line, = ax.plot([], [], lw=2)

# Инициализация анимации
def init():
    ax.set_rmax(2)  # Устанавливаем максимальное значение радиуса
    line.set_data([], [])
    return line,

# Функция анимации
def animate(i):
    t = t_values[:i+1]  # Используем i+1, чтобы включить текущий элемент
    r_vals = r(t)
    fi_vals = fi(t)
    line.set_data(fi_vals, r_vals)
    return line,

# Создаем анимацию
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(t_values), interval=50, blit=True)

# Показываем анимацию
plt.show()