import sympy as sp

# Definir variables
t, s = sp.symbols('t s')


def calcular_laplace(funcion):
    F = sp.laplace_transform(funcion, t, s)
    return F[0]  # Solo la transformada

entrada = input("Introduce la función de t: ")
funcion = sp.sympify(entrada, locals={"t": t})
resultado = calcular_laplace(funcion)
print("La Transformada de Laplace es:")
print(resultado)