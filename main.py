import math

import numpy as np

from methods import *
import matplotlib.pyplot as plt

def plot_solutions(exact_solution, approx_solution):
    # # Extract x and y values from the exact solution
    x_exact = [point[0] for point in exact_solution]
    y_exact = [point[1] for point in exact_solution]
    #
    # # Extract x and y values from the approximate solution
    x_approx = [point[0] for point in approx_solution]
    y_approx = [point[1] for point in approx_solution]
    #
    plt.xlim(min(min(x_exact), min(x_approx))-0.015, max(max(x_exact), max(x_approx))+0.015)
    plt.ylim(min(min(y_exact), min(y_approx))-0.5, max(max(y_exact), max(y_approx))+0.5)

    # Plot the exact solution as points and the approximate solution as a line
    plt.plot(x_exact, y_exact, linestyle='None', marker='o', label='Exact Solution')
    plt.plot(x_approx, y_approx, linestyle='-', label='Approximate Solution')


    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Comparison of Exact and Approximate Solutions')
    plt.legend()
    plt.grid(True)


    plt.show()


func1 = lambda x, y: 2 * x * y
func2 = lambda x, y: np.sin(x) - y
func3 = lambda x, y: 2 * x ** 2 * y

ans1 = lambda x: np.exp(x ** 2)
ans2 = lambda x: (np.sin(x) + np.cos(x))/2
ans3 = lambda x: np.exp((2 * x ** 3) / 3)

des1 = "1)y\' = 2xy, [1.5;3], y0 = 9.4"
des2 = "2)y\' = sin(x)-y, [0;5], y0 = 0.5"
des3 = "3)y\' = 2x^2*y, [0;1.5], y0 = 1"

y1 = 9.4
y2 = 0.5
y3 = 1

a1 = 1.5
b1 = 10
a2 = 0
b2 = 12
a3 = 0
b3 = 8

print("Выбирите уравнение")
print(des1)
print(des2)
print(des3)
var = int(input(""))
if var == 1:
    func = func1
elif var == 2:
    func = func2
elif var == 3:
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
    dots = euler_method(func, a1, b1, y1, step, ans1)
    cur_dots = [(x, ans1(x)) for x in np.arange(a1, b1 + step, step)]
elif var == 2:
     dots = modern_euler_method(func, a2, b2, y2, step,ans2)
     cur_dots = [(x, ans2(x)) for x in np.arange(a2, b2 + step, step)]
elif var == 3:
    dots = miln(func, a3, b3, y3, step,ans3)
    cur_dots = [(x, ans3(x)) for x in np.arange(a3, b3 + step, step)]

print(dots[3])
print(dots[0])
plot_solutions(dots[3],dots[0])
