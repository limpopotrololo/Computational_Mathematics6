def modern_euler_method(f, a, b, y0, step, eps):
    x_ans = []
    y_ans = []
    errors = []
    x = a
    y = y0

    x_ans.append(x)
    y_ans.append(y)

    while x < b:
        k1 = step * f(x, y)
        k2 = step * f(x + step, y + k1)
        y_next = y + 0.5 * (k1 + k2)

        x += step
        y = y_next

        x_ans.append(x)
        y_ans.append(y)

        k3 = step * f(x + step, y + k2)
        error = abs((k2 - k3) / 2)
        errors.append(error)

        if error <= eps:
            break

    return x_ans, y_ans, errors


def euler_method(f, a, b, y0, step, eps):
    points = [(a, y0)]
    errors = []
    n = cl_n(a, b, step)
    h = step

    y_i = y0

    for i in range(0, n):
        x_i = points[i][0]
        y_i = points[i][1]

        y_i_1 = y_i + h * f(x_i, y_i)

        x_i_1 = x_i + h
        points.append((x_i_1, y_i_1))

        k1 = h * f(x_i, y_i)
        k2 = h * f(x_i_1, y_i_1)
        error = abs((k2 - k1) / 2)
        errors.append(error)

        if error <= eps:
            break

        if x_i_1 >= b:
            break

    return [x for x, _ in points], [y for _, y in points], errors

def miln(f, a, b, y0, step,eps):
    points = [(a, y0)]
    approx_ans = [y0]

    n = cl_n(a, b, step)

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
        points.append((x_i, y_i))
        approx_ans.append(y_i)

    for i in range(3, n):
        x_i = points[-1][0] + step
        y_pred = points[-1][1] + (4 * step / 3) * (2 * f(points[-1][0], points[-1][1]) -
                                                 f(points[-2][0], points[-2][1]) +
                                                 2 * f(points[-3][0], points[-3][1]))

        y_i = points[-2][1] + (step / 3) * (f(x_i, y_pred) + 4 * f(points[-2][0], points[-2][1]) +
                                          f(points[-3][0], points[-3][1]))

        points.append((x_i, y_i))
        approx_ans.append(y_i)

        if x_i >= b:
            break

    return [x for x, _ in points], approx_ans

def cl_n(a, b, h):
    return int((b - a) / h)
