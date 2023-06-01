def calculate_n(a, b, h):
    return int((b - a) / h)

def miln(f, a, b, y0, step, ans):
    dots = [(a, y0)]
    approx_values = [(a, y0)]  # Список с приближенными значениями

    n = calculate_n(a, b, step)

    x_i = a
    y_i = y0

    for i in range(3):
        k1 = step * f(x_i, y_i)
        k2 = step * f(x_i + step / 2, y_i + k1 / 2)
        k3 = step * f(x_i + step / 2, y_i + k2 / 2)
        k4 = step * f(x_i + step, y_i + k3)

        y_i_1 = y_i + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_i += step
        y_i = y_i_1
        dots.append((x_i, y_i))
        approx_values.append((x_i, y_i))  # Добавляем приближенное значение

    for i in range(3, n):
        x_i = dots[-4][0] + step
        y_pred = dots[-1][1] + (4 * step / 3) * (2 * f(dots[-1][0], dots[-1][1]) -
                                                 f(dots[-2][0], dots[-2][1]) +
                                                 2 * f(dots[-3][0], dots[-3][1]))

        y_i = dots[-2][1] + (step / 3) * (f(x_i, y_pred) + 4 * f(dots[-2][0], dots[-2][1]) +
                                          f(dots[-3][0], dots[-3][1]))

        dots.append((x_i, y_i))
        approx_values.append((x_i, y_i))  # Добавляем приближенное значение

        if x_i >= b:
            break

    function_values = [(x, f(x, y)) for x, y in dots]
    ans_values = [(x, ans(x)) for x, y in dots]

    return dots, function_values, n, ans_values, approx_values
