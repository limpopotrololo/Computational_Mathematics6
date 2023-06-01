

def modern_euler_method(f, a, b, y0, step, eps, ans):
    dots = [(a, y0)]
    n = calculate_n(a, b, step, eps)
    h = step

    error = 0.0

    for i in range(0, n):
        x_i = dots[i][0]
        y_i = dots[i][1]

        # Метод Рунге: вычисляем y_i_r
        y_i_r = y_i + h * f(x_i, y_i)
        y_i_1_r = y_i + (h / 2) * (f(x_i, y_i) + f(x_i + h, y_i_r))
        y_i_1 = y_i + h * f(x_i, y_i)  # Присваиваем значение 'y_i_1' до вычисления ошибки

        # Оценка точности
        error = abs(y_i_1_r - y_i_1)
        while error > eps:
            h = h / 2

            # Метод Рунге: пересчитываем y_i_r и y_i_1_r с новым шагом
            y_i_r = y_i + h * f(x_i, y_i)
            y_i_1_r = y_i + (h / 2) * (f(x_i, y_i) + f(x_i + h, y_i_r))

            # Оценка точности
            error = abs(y_i_1_r - y_i_1)

        # Обновляем значения точки и шага
        x_i_1 = x_i + h
        y_i_1 = y_i + h * f(x_i, y_i)
        dots.append((x_i_1, y_i_1))

        if x_i_1 >= b:
            break

    function_values = [(x, f(x, y)) for x, y in dots]
    ans_values = [(x, ans(x)) for x, y in dots]
    return dots, function_values, error, n, ans_values


def euler_method(f, a, b, y0, step, ans):
    dots = [(a, y0)]
    n = calculate_n(a, b, step)
    h = step

    y_i = y0

    for i in range(0, n):
        x_i = dots[i][0]
        y_i = dots[i][1]

        y_i_1 = y_i + h * f(x_i, y_i)

        x_i_1 = x_i + h
        dots.append((x_i_1, y_i_1))

        if x_i_1 >= b:
            break

    function_values = [(x, f(x, y)) for x, y in dots]
    ans_values = [(x, ans(x)) for x, y in dots]
    return dots, function_values, n, ans_values


def miln(f, a, b, y0, step, ans):
    dots = [(a, y0)]
    n = calculate_n(a, b, step)

    x_i = a
    y_i = y0

    for _ in range(3):
        k1 = step * f(x_i, y_i)
        k2 = step * f(x_i + step / 2, y_i + k1 / 2)
        k3 = step * f(x_i + step / 2, y_i + k2 / 2)
        k4 = step * f(x_i + step, y_i + k3)

        y_i_1 = y_i + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_i += step
        y_i = y_i_1
        dots.append((x_i, y_i))

    for _ in range(3, n):
        x_i = dots[-4][0] + step
        y_pred = dots[-1][1] + (4 * step / 3) * (2 * f(dots[-1][0], dots[-1][1]) -
                                                 f(dots[-2][0], dots[-2][1]) +
                                                 2 * f(dots[-3][0], dots[-3][1]))

        y_i = dots[-2][1] + (step / 3) * (f(x_i, y_pred) + 4 * f(dots[-2][0], dots[-2][1]) +
                                          f(dots[-3][0], dots[-3][1]))

        dots.append((x_i, y_i))

        if x_i >= b:
            break

    function_values = [(x, f(x, y)) for x, y in dots]
    ans_values = [(x, ans(x)) for x, y in dots]
    return dots, function_values, n, ans_values


def calculate_n(a, b, h):
    return int((b - a) / h)
