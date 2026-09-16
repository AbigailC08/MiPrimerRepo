
import sympy as sp


t, s = sp.symbols('t s')


def calcular_laplace(funcion):
    F = sp.laplace_transform(funcion, t, s)
    return F[0]  # Solo la transformada simbólica


entrada = input("Introduce la función de t (por ejemplo: exp(2*t), sin comillas): ")
try:
    funcion = sp.sympify(entrada, locals={"t": t, "exp": sp.exp, "sin": sp.sin, "cos": sp.cos, "ln": sp.ln})
    resultado = calcular_laplace(funcion)
    print("La Transformada de Laplace es:")
    print(resultado)
except Exception as e:
    print("Error al interpretar la función:", e)