"""Implementación del método de Euler para resolver un PVI."""

# Bibliotecas
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  # Corrige el backend para evitar errores en PyCharm

def plot_results(t_values, w_values, a, b, y0, n):
    """Grafica la solución numérica y la solución exacta."""
    t_exact = np.linspace(a, b, 200)
    y_exact = exact_solution(t_exact)

    plt.figure(figsize=(8, 5))
    plt.plot(t_values, w_values, 'bo-', label='Método de Euler')
    plt.plot(t_exact, y_exact, 'r-', label='Solución exacta')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.title("Comparación entre solución numérica y exacta")
    plt.grid()
    plt.show()

def euler_method(f, a, b, y0, n):
    """Método de Euler para resolver ecuaciones diferenciales."""
    h = (b - a) / n
    t_values = np.linspace(a, b, n + 1)
    w_values = np.zeros(n + 1)
    w_values[0] = y0

    for i in range(1, n + 1):
        w_values[i] = w_values[i - 1] + h * f(t_values[i - 1], w_values[i - 1])

    return t_values, w_values


def exact_solution(t):
    """Solución exacta del PVI."""
    return (4/3) * np.exp(-t) + t - 1/3


def f(t, y):
    """Función de la ecuación diferencial y' = -y + t."""
    return -y + t


def plot_results(t_values, w_values, a, b, y0, n):
    """Grafica la solución numérica y la solución exacta."""
    t_exact = np.linspace(a, b, 200)
    y_exact = exact_solution(t_exact)

    plt.figure(figsize=(8, 5))
    plt.plot(t_values, w_values, 'bo-', label='Método de Euler')
    plt.plot(t_exact, y_exact, 'r-', label='Solución exacta')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.title("Comparación entre solución numérica y exacta")
    plt.grid()
    plt.show()


def get_user_input():
    """Solicita valores al usuario con validación."""
    while True:
        try:
            a = float(input("Ingrese el valor de a (límite inferior): "))
            b = float(input("Ingrese el valor de b (límite superior): "))
            if a >= b:
                print("Error: 'a' debe ser menor que 'b'. Intente nuevamente.")
                continue
            y0 = float(input("Ingrese el valor inicial y0: "))
            n = int(input("Ingrese el número de pasos n (entero positivo): "))
            if n <= 0:
                print("Error: 'n' debe ser un entero positivo. Intente nuevamente.")
                continue
            return a, b, y0, n
        except ValueError:
            print("Entrada no válida. Asegúrese de ingresar valores numéricos.")


def main():
    """MAIN"""
    a, b, y0, n = get_user_input()
    t_values, w_values = euler_method(f, a, b, y0, n)
    plot_results(t_values, w_values, a, b, y0, n)


if __name__ == "__main__":
    main()
