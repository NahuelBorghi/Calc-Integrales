import tkinter as tk
from tkinter import ttk
from integral_calculator import IntegralCalculator
from graph_generator import GraphGenerator
from ui_elements import UIElements

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Integrales")

        # Inicializar clases
        self.calculator = IntegralCalculator()
        self.ui_elements = UIElements(self.root, self.calculate_integral, self.show_graph)
        self.graph_generator = GraphGenerator()
        
        # Configurar elementos de la interfaz
        self.ui_elements.create_input_fields()

    def calculate_integral(self):
        # Obtener datos de la interfaz
        function_str = self.ui_elements.function_entry.get()
        lower_limit_str = self.ui_elements.lower_limit_entry.get()
        upper_limit_str = self.ui_elements.upper_limit_entry.get()

        # Calcular integral
        result, area, error = self.calculator.calculate_integral(
            function_str, lower_limit_str, upper_limit_str
        )

        # Mostrar resultados en la interfaz
        self.ui_elements.show_results(result, area, error)

    def show_graph(self):
    # Llama al método generate_graph de GraphGenerator
        self.graph_generator.generate_graph(
            self.ui_elements.function_entry.get(),
            self.ui_elements.lower_limit_entry.get(),
            self.ui_elements.upper_limit_entry.get()
        )


# Crear la ventana principal
root = tk.Tk()
app = MainApplication(root)

# Iniciar el bucle de eventos
root.mainloop()
