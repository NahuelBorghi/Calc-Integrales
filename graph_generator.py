# graph_generator.py

import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, lambdify

class GraphGenerator:
    def __init__(self):
        pass  # Puedes inicializar variables o configuraciones aquí si es necesario

    def generate_graph(self, function_str, lower_limit_str, upper_limit_str):
        try:
            # Convertir la función a una función lambda para evaluarla numéricamente
            x = symbols('x')
            function = lambdify(x, function_str, 'numpy')

            # Crear un conjunto de puntos para el gráfico
            x_values = np.linspace(float(lower_limit_str), float(upper_limit_str), 1000)
            y_values = function(x_values)

            # Graficar la función y la integral definida
            plt.plot(x_values, y_values, label='Función Original')
            plt.fill_between(x_values, 0, y_values, alpha=0.3, color='gray', label='Área bajo la curva')
            plt.legend()
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Gráfico de la Función y su Integral Definida')
            plt.show()

        except Exception as e:
            # Manejar errores al generar el gráfico
            print(f"Error al generar el gráfico: {e}")
