import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import sympy as sp
from sympy import Function, dsolve, Eq, Derivative


# ==============================
# FUNCIONES PARA GRAFICAR
# ==============================

LISTA_FUNCIONES = [
    {"nombre": "x²", "funcion": lambda x: x**2},
    {"nombre": "3x - 5", "funcion": lambda x: 3*x - 5},
    {"nombre": "x³", "funcion": lambda x: x**3},
    {"nombre": "2x² + 4", "funcion": lambda x: 2*(x**2) + 4},
    {"nombre": "5x² - x", "funcion": lambda x: 5*(x**2) - x},
    {"nombre": "x² + 2x", "funcion": lambda x: (x**2) + 2*x},
    {"nombre": "cos(x)", "funcion": lambda x: np.cos(x)},
    {"nombre": "4x", "funcion": lambda x: 4*x},
]


# ==============================
# CLASE PRINCIPAL
# ==============================

class CalculadoraTotal:

    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Diferencial PRO MAX")
        self.root.geometry("1000x750")
        self.root.configure(bg="#eef1f5")

        style = ttk.Style()
        style.theme_use("clam")

        # ===== PANEL SUPERIOR =====
        panel = ttk.Frame(root, padding=15)
        panel.pack(fill="x")

        ttk.Label(panel, text="Función:").grid(row=0, column=0, padx=5)

        self.combo = ttk.Combobox(
            panel,
            values=[f["nombre"] for f in LISTA_FUNCIONES],
            state="readonly",
            width=20
        )
        self.combo.grid(row=0, column=1, padx=5)
        self.combo.current(0)

        ttk.Label(panel, text="x =").grid(row=0, column=2, padx=5)
        self.entry_x = ttk.Entry(panel, width=10)
        self.entry_x.insert(0, "2")
        self.entry_x.grid(row=0, column=3, padx=5)

        ttk.Label(panel, text="Δx =").grid(row=0, column=4, padx=5)
        self.entry_dx = ttk.Entry(panel, width=10)
        self.entry_dx.insert(0, "0.1")
        self.entry_dx.grid(row=0, column=5, padx=5)

        ttk.Button(panel, text="Calcular", command=self.calcular)\
            .grid(row=0, column=6, padx=15)

        # ===== SECCIÓN ECUACIONES DIFERENCIALES =====
        ttk.Separator(root).pack(fill="x", pady=5)

        panel_ed = ttk.Frame(root, padding=10)
        panel_ed.pack(fill="x")

        ttk.Label(panel_ed, text="Ecuación Diferencial (formato sympy):")\
            .grid(row=0, column=0, padx=5)

        self.entry_ecuacion = ttk.Entry(panel_ed, width=60)
        self.entry_ecuacion.grid(row=0, column=1, padx=5)

        ttk.Button(panel_ed, text="Resolver EDO",
                   command=self.resolver_ecuacion_diferencial)\
            .grid(row=0, column=2, padx=10)

        # ===== RESULTADO =====
        self.resultado = tk.Label(
            root,
            font=("Consolas", 11),
            bg="white",
            anchor="w",
            justify="left",
            padx=15,
            pady=10
        )
        self.resultado.pack(fill="x", padx=15, pady=10)

        # ===== GRÁFICA =====
        self.fig, self.ax = plt.subplots(figsize=(9, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=15, pady=10)

    # ==============================================
    # CALCULADORA DIFERENCIAL
    # ==============================================

    def calcular(self):
        try:
            func_data = LISTA_FUNCIONES[self.combo.current()]
            f = func_data["funcion"]

            x = float(self.entry_x.get())
            dx = float(self.entry_dx.get())

            x2 = x + dx
            fx = f(x)
            fx2 = f(x2)

            delta_f = fx2 - fx
            derivada_aprox = delta_f / dx

            texto = (
                f"Función: f(x) = {func_data['nombre']}\n"
                f"x = {x:.6f}\n"
                f"x + Δx = {x2:.6f}\n"
                f"f(x) = {fx:.6f}\n"
                f"f(x + Δx) = {fx2:.6f}\n"
                f"Δf = {delta_f:.6f}\n"
                f"Pendiente aproximada (Δf/Δx) ≈ {derivada_aprox:.6f}"
            )

            self.resultado.config(text=texto)

            # ===== GRÁFICA =====
            self.ax.clear()

            x_rango = np.linspace(x - 6, x + 6, 400)
            self.ax.plot(x_rango, f(x_rango), linewidth=2)

            self.ax.scatter([x, x2], [fx, fx2], s=80)
            self.ax.plot([x, x2], [fx, fx2], linestyle="--")

            self.ax.axvline(x, linestyle=":")
            self.ax.axvline(x2, linestyle=":")

            self.ax.grid(True)
            self.ax.set_title("Gráfica y Recta Secante")
            self.ax.set_xlabel("x")
            self.ax.set_ylabel("f(x)")

            self.canvas.draw()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ==============================================
    # RESOLVER ECUACIONES DIFERENCIALES
    # ==============================================

    def resolver_ecuacion_diferencial(self):
        try:
            ecuacion_texto = self.entry_ecuacion.get()

            x = sp.symbols('x')
            y = Function('y')

            ecuacion = sp.sympify(ecuacion_texto)

            solucion = dsolve(ecuacion)
            solucion_simplificada = sp.simplify(solucion)

            self.resultado.config(
                text=f"Solución simbólica:\n{sp.pretty(solucion_simplificada)}"
            )

        except Exception:
            messagebox.showerror(
                "Error",
                "No se pudo resolver.\nVerifica sintaxis tipo:\n"
                "Eq(Derivative(y(x), x) - 3*y(x), 0)"
            )


# ==============================
# EJECUCIÓN
# ==============================

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraTotal(root)
    root.mainloop()