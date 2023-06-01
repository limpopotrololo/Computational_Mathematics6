import math
import numpy as np
import matplotlib.pyplot as plt

from methods import euler_method, modern_euler_method, miln

# Определение функций и точных решений
func1 = lambda x, y: 2 * x * y
ans1 = lambda x: math.exp(x ** 2)

func2 = lambda x, y: math.sin(x) * y
ans2 = lambda x: math.exp(-math.cos(x))

func3 = lambda x, y: 2 * x ** 2 * y
ans3 = lambda x: math.exp((2 * x ** 3) / 3)

# Заданные значения
descriptions = [
    "1) y' = 2xy, [1.5;3], y0 = 9.4",
    "2) y' = sin(x)y, [2;3], y0 = 0.4",
    "3) y' = 2x^2*y, [0;1.5], y0 = 1"
]
y_values = [9.4, 0.4, 1]
a_values = [1.5, 2, 0]
b_values = [3, 3, 1.5]
func_values = [func1, func2, func3]
ans_values = [ans1, ans2, ans3]

# Вывод описаний и выбор уравнения
for desc in descriptions:
    print(desc)
var = int(input("Выберите уравнение: ")) - 1
if var < 0 or var >= len(descriptions):
    raise ValueError("Некорректный ввод")

# Ввод шага и точности
step = float(input("Введите шаг: "))
eps = float(input("Введите точность: "))

# Выбор метода и вычисление значений
methods = [
    ('Метод Эйлера', euler_method),
    ('Усовершенствованный метод Эйлера', modern_euler_method),
    ('Метод Милна', miln)
]
for i, method in enumerate(methods, 1):
    print(f"{i}) {method[0]}")
method_var = int(input("Выберите метод решения: ")) - 1
if method_var < 0 or method_var >= len(methods):
    raise ValueError("Некорректный ввод")
method_name, method_func = methods[method_var]

# Вычисление значений и точных решений
func = func_values[var]
ans_func = ans_values[var]

a = a_values[var]
b = b_values[var]
y0 = y_values[var]

dots = method_func(func, a, b, y0, step, eps)
cur_dots = [(x, ans_func(x)) for x in np.arange(a, b + step, step)]

print(cur_dots)
print(dots[1])

# Построение графика
x_exact = np.linspace(a, b)
y_exact = np.vectorize(ans_func)(x_exact)

x_approx = [point[0] for point in dots[0]]
y_approx = [point[1] for point in dots[0]]

plt.plot(x_exact, y_exact, 'blue', label=f"Точное решение: y = {ans_values[var].__name__}")
plt.plot(x_approx, y_approx, 'ro', label=method_name)
plt.xlabel('x')
plt.ylabel('y')
plt.title(f"y' = {func.__name__}")
plt.legend()
plt.show()
