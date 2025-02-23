"""""
 @author Atom Alexander Munoz Nava
 @brief Implementación del método de Euler para resolver un PVI.
 @date 23/02/2025
"""""

# Bibliotecas
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

def desplegar_res(t_values, w_values, a, b, y0, n):
    """
    @brief Grafica la solución numérica y la solución exacta.
    @param t_values Valores de t generados por el método de Euler.
    @param w_values Valores de y aproximados por el método de Euler.
    @param a Límite inferior del intervalo.
    @param b Límite superior del intervalo.
    @param y0 Valor inicial del problema de valor inicial.
    @param n Número de pasos utilizados en la discretización.
    """
    t_exact = np.linspace(a, b, 200)
    y_exact = sol_exacta(t_exact)

    plt.figure(figsize=(8, 5))
    plt.plot(t_values, w_values, 'bo-', label='Método de Euler')
    plt.plot(t_exact, y_exact, 'r-', label='Solución exacta')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.title("Comparación entre solución numérica y exacta")
    plt.grid()
    plt.show()

def metodo_euler(f, a, b, y0, n):
    """
    @brief Método de Euler para resolver EDOs.
    @param f Función que define la ecuación diferencial y' = f(t, y).
    @param a Límite inferior del intervalo.
    @param b Límite superior del intervalo.
    @param y0 Valor inicial del problema de valor inicial.
    @param n Número de pasos de la discretización.
    @return t_values Valores de t generados.
    @return w_values Valores de y aproximados.
    """
    h = (b - a) / n
    t_values = np.linspace(a, b, n + 1)
    w_values = np.zeros(n + 1)
    w_values[0] = y0

    for i in range(1, n + 1):
        w_values[i] = w_values[i - 1] + h * f(t_values[i - 1], w_values[i - 1])

    return t_values, w_values

def sol_exacta(t):
    """
    @brief Solución exacta del problema de valor inicial.
    @param t Valores de entrada para evaluar la solución exacta.
    @return Valores de la solución exacta.
    """
    return (4/3) * np.exp(-t) + t - 1/3

def f(t, y):
    """
    @brief Función de la ecuación diferencial y' = -y + t.
    @param t Variable independiente.
    @param y Variable dependiente.
    @return Evaluación de la ecuación diferencial.
    """
    return -y + t

def entrada_datos():
    """
    @brief Solicita valores al usuario con validación.
    @return a Límite inferior del intervalo.
    @return b Límite superior del intervalo.
    @return y0 Valor inicial del problema de valor inicial.
    @return n Número de pasos en la discretización.
    """
    while True:
        try:
            a = float(input("Ingrese el valor de a (límite inferior) = 1: "))
            b = float(input("Ingrese el valor de b (límite superior) = 3: "))
            if a >= b:
                print("Error: 'a' debe ser menor que 'b'. Intente nuevamente.")
                continue
            y0 = float(input("Ingrese el valor inicial y0 = 2: "))
            n = int(input("Ingrese el número de pasos n (entero positivo) = 100: "))
            if n <= 0:
                print("Error: 'n' debe ser un entero positivo. Intente d nuevo.")
                continue
            return a, b, y0, n
        except ValueError:
            print("Entrada no válida, intenta de nuevo")

def main():
    """
    @brief Función principal del programa.
    """
    a, b, y0, n = entrada_datos()
    t_values, w_values = metodo_euler(f, a, b, y0, n)
    desplegar_res(t_values, w_values, a, b, y0, n)

if __name__ == "__main__":
    main()
