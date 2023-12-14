# ui_elements.py

import tkinter as tk
from tkinter import ttk

class UIElements:
    def __init__(self, root, calculate_callback, graph_callback):
        self.root = root
        self.calculate_callback = calculate_callback
        self.graph_callback = graph_callback

        # Variables de entrada
        self.function_entry = None
        self.lower_limit_entry = None
        self.upper_limit_entry = None

        # Configuración de la interfaz
        self.create_input_fields()

    def create_input_fields(self):
        # Etiquetas y campos de entrada
        ttk.Label(self.root, text="Función:").grid(row=0, column=0, pady=5)
        self.function_entry = ttk.Entry(self.root, width=30)
        self.function_entry.grid(row=0, column=1, pady=5)

        ttk.Label(self.root, text="Límite inferior:").grid(row=1, column=0, pady=5)
        self.lower_limit_entry = ttk.Entry(self.root, width=10)
        self.lower_limit_entry.grid(row=1, column=1, pady=5)

        ttk.Label(self.root, text="Límite superior:").grid(row=2, column=0, pady=5)
        self.upper_limit_entry = ttk.Entry(self.root, width=10)
        self.upper_limit_entry.grid(row=2, column=1, pady=5)

        # Botones
        calculate_button = ttk.Button(self.root, text="Calcular", command=self.calculate_callback)
        calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

        graph_button = ttk.Button(self.root, text="Mostrar Gráfico", command=self.graph_callback)
        graph_button.grid(row=4, column=0, columnspan=2, pady=10)

    def show_results(self, result, area, error):
        # Mostrar resultados en la interfaz (puedes personalizar según tus necesidades)
        result_str = f"Resultado: {result}"
        area_str = f"Área: {area}"
        error_str = f"Error: {error}"

        result_label = ttk.Label(self.root, text=result_str)
        area_label = ttk.Label(self.root, text=area_str)
        error_label = ttk.Label(self.root, text=error_str)

        result_label.grid(row=5, column=0, pady=5)
        area_label.grid(row=6, column=0, pady=5)
        error_label.grid(row=7, column=0, pady=5)
