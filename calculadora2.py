import sympy as sp

# Definir variables
t, s = sp.symbols('t s')

# Función para calcular la Transformada de Laplace
def calcular_laplace(funcion):
    F = sp.laplace_transform(funcion, t, s)
    return F

# Ejemplo de ecuación diferencial
f = sp.exp(2*t)

# Calcular transformada
resultado = calcular_laplace(f)

print("La Transformada de Laplace es:")
print(resultado)