# Importar Tkinter
import tkinter as tk
from tkinter import ttk, messagebox

# Crear ventana principal
root = tk.Tk()
root.title("Web Quest Matemática")
root.geometry("600x400")

# Crear notebook (pestañas)
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Pestañas
frame_calculadora = ttk.Frame(notebook)
frame_ecuaciones = ttk.Frame(notebook)
frame_fourier = ttk.Frame(notebook)

notebook.add(frame_calculadora, text="Calculadora")
notebook.add(frame_ecuaciones, text="Ecuaciones")
notebook.add(frame_fourier, text="Serie de Fourier")

# --- Calculadora básica ---
def calcular():
	try:
		resultado = eval(entry_calculadora.get())
		label_resultado.config(text=f"Resultado: {resultado}")
	except Exception as e:
		label_resultado.config(text="Error")

entry_calculadora = tk.Entry(frame_calculadora, font=("Arial", 16), width=30)
entry_calculadora.pack(pady=10)

btn_calcular = tk.Button(frame_calculadora, text="Calcular", command=calcular)
btn_calcular.pack(pady=5)

label_resultado = tk.Label(frame_calculadora, text="Resultado: ", font=("Arial", 14))
label_resultado.pack(pady=10)

# --- Conversor de ecuaciones ---
import sympy as sp

def convertir_ecuacion():
	ecuacion = entry_ecuacion.get()
	try:
		expr = sp.sympify(ecuacion)
		pasos = sp.simplify(expr)
		label_ecuacion_resultado.config(text=f"Operación sencilla: {pasos}")
	except Exception as e:
		label_ecuacion_resultado.config(text="Error en la ecuación")

entry_ecuacion = tk.Entry(frame_ecuaciones, font=("Arial", 16), width=30)
entry_ecuacion.pack(pady=10)

btn_convertir = tk.Button(frame_ecuaciones, text="Convertir", command=convertir_ecuacion)
btn_convertir.pack(pady=5)

label_ecuacion_resultado = tk.Label(frame_ecuaciones, text="Operación sencilla: ", font=("Arial", 14))
label_ecuacion_resultado.pack(pady=10)

# --- Serie de Fourier ---
fourier_info = """
La serie de Fourier permite expresar funciones periódicas como suma de senos y cosenos.

Ejemplo:
f(x) = a0/2 + Σ [an*cos(n*x) + bn*sin(n*x)]

Puedes calcular los coeficientes para funciones simples.
"""

label_fourier = tk.Label(frame_fourier, text=fourier_info, font=("Arial", 12), justify="left")
label_fourier.pack(pady=10)

def calcular_fourier():
	funcion = entry_fourier.get()
	try:
		x = sp.symbols('x')
		serie = sp.fourier_series(sp.sympify(funcion), (x, 0, 2*sp.pi))
		label_fourier_resultado.config(text=f"Serie de Fourier:\n{serie}")
	except Exception as e:
		label_fourier_resultado.config(text="Error en la función")

entry_fourier = tk.Entry(frame_fourier, font=("Arial", 16), width=30)
entry_fourier.pack(pady=10)

btn_fourier = tk.Button(frame_fourier, text="Calcular serie de Fourier", command=calcular_fourier)
btn_fourier.pack(pady=5)

label_fourier_resultado = tk.Label(frame_fourier, text="Serie de Fourier: ", font=("Arial", 12), justify="left")
label_fourier_resultado.pack(pady=10)

# Ejecutar ventana
root.mainloop()
