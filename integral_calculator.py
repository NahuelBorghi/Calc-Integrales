# integral_calculator.py
from scipy.integrate import quad
from sympy import lambdify, symbols, sympify, integrate

class IntegralCalculator:
    def __init__(self):
        pass  # Puedes inicializar variables o configuraciones aquí si es necesario

    def calculate_integral(self, function_str, lower_limit_str, upper_limit_str):
        try:
            # Convertir la función a una función lambda para evaluarla numéricamente
            x = symbols('x')
            function = lambdify(x, sympify(function_str), 'numpy')
            # Definir las tolerancias absoluta y relativa (ajústalas según sea necesario)
            epsabs = 1e-6
            epsrel = 1e-6

            # Calcular la integral definida y estimar el error utilizando quad
            result, error = quad(function, float(lower_limit_str), float(upper_limit_str), epsabs=epsabs, epsrel=epsrel)

            # Calcular el área bajo la curva numéricamente
            area = integrate(sympify(function_str), (x, float(lower_limit_str), float(upper_limit_str))).evalf()

            return result, area, error

        except Exception as e:
            # Manejar errores de entrada o cálculos
            print(f"Error en el cálculo: {e}")
            return None, None, None
