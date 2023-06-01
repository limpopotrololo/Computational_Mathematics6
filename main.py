import math

import numpy as np

from methods import *
import matplotlib.pyplot as plt

def plot_function(f, x_min, x_max, points_x, points_y):
    x = np.linspace(x_min, x_max, 1000)
    y = f(x)

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График жирафик')
    plt.grid(True)
    if points_x and points_y:
        plt.scatter(points_x, points_y, color='red', label='Points')

    plt.show()



func1 = lambda x, y: 2 * x * y
func2 = lambda x, y: np.cos(x) - y
func3 = lambda x, y: 2 * x ** 2 * y

ans1 = lambda x: np.exp(x ** 2)
ans2 = lambda x: (np.sin(x) + np.cos(x))/2
ans3 = lambda x: np.exp((2 * x ** 3) / 3)

des1 = "1)y\' = 2xy, [1.5;2], y0 = 9.4"
des2 = "2)y\' = cos(x)-y, [0;2], y0 = 0.5"
des3 = "3)y\' = 2x^2*y, [0;2], y0 = 0"

y1 = 9.4
y2 = 0.5
y3 = 1

a1 = 1.5
b1 = 2
a2 = 0
b2 = 3
a3 = 0
b3 = 2

print("Выбирите уравнение")
print(des1)
print(des2)
print(des3)
varf = int(input(""))
if varf == 1:
    func = func1
elif varf == 2:
    func = func2
elif varf == 3:
    func = func3
else:
    raise ValueError("invalid input")
step = float(input("Введите шаг\n"))
eps = float(input("Введите точность\n"))
print("1) Метод Эйлера")
print("2) Усовершенствованный метод Эйлера")
print("3) Метод Милна")
var = int(input(""))
if var == 1:
    if varf == 1:
        dots = euler_method(func, a1, b1, y1, step, eps)
        plot_function(ans1, a1, b1, dots[0], dots[1])
    elif varf == 2:
        dots = euler_method(func, a2, b2, y2, step, eps)
        plot_function(ans2, a2, b2, dots[0], dots[1])
    else:
        dots = euler_method(func, a3, b3, y3, step, eps)
        plot_function(ans3, a3, b3, dots[0], dots[1])
elif var == 2:
    if varf == 1:
        dots = modern_euler_method(func, a1, b1, y1, step, eps)
        plot_function(ans1, a1, b1, dots[0], dots[1])
    elif varf == 2:
        dots = modern_euler_method(func, a2, b2, y2, step, eps)
        plot_function(ans2, a2, b2, dots[0], dots[1])
    else:
        dots = modern_euler_method(func, a3, b3, y3, step, eps)
        plot_function(ans3, a3, b3, dots[0], dots[1])

elif var == 3:
    if varf == 1:
        dots = miln(func, a1, b1, y1, step, eps)
        plot_function(ans1, a1, b1, dots[0], dots[1])
    elif varf == 2:
        dots = miln(func, a2, b2, y2, step, eps)
        plot_function(ans2, a2, b2, dots[0], dots[1])
    else:
        dots = miln(func, a3, b3, y3, step, eps)
        plot_function(ans3, a3, b3, dots[0], dots[1])

print(dots[0])