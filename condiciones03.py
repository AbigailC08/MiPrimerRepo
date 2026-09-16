#el programa debe pedir la estatura de una persona
#si es menor que 1.60, debe mostrar: Eres chaparrito
#si es mayor o igual a 1.60 pero menor que 1.75
#debe mostrar: Tienes estatura mediana
#si es mayor que 1.75 debe mostrar: Eres alto

estatura=float(input('Escribe tu estatura:'))
if(estatura<1.60):
    print('Eres chaparrito')

if(estatura>=1.60) and (estatura<1.75):
    print('Tienes estatura mediana')

if(estatura>1.75):
    print('Eres alto')