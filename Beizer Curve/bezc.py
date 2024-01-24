import matplotlib.pyplot as plt


def factorial(n):
    if n:
        return n * factorial(n - 1)
    else:
        return 1


def nCr(n, i):
    return factorial(n) / float(factorial(i) * factorial(n - i))


def BEZ(i, n, u):
    return nCr(n, i) * (u ** i) * ((1 - u) ** (n - i))


def bezierCurve(x_control_points, y_control_points):
    n = len(x_control_points) - 1
    eps = 0.01
    x_curve_points = []
    y_curve_points = []
    u = 0

    while u < 1.01:
        x, y = 0, 0
        for i in range(0, len(x_control_points)):
            bez = BEZ(i, n, u)
            x += x_control_points[i] * bez
            y += y_control_points[i] * bez
        x_curve_points.append(x)
        y_curve_points.append(y)
        u += eps

        plt.clf()
        plt.title("Bezier Curve")
        plt.plot(x_control_points, y_control_points, label="Control Graph")
        plt.plot(x_curve_points, y_curve_points, label="Bezier Curve")
        plt.legend()
        plt.grid()
        plt.pause(0.001)

    plt.show()


def main():
    x_control_points = [1, 7, 15, 21, 25]
    y_control_points = [5, 10, 5, -10, 3]

    bezierCurve(x_control_points, y_control_points)


if __name__ == "__main__":
    main()