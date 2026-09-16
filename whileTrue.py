#La estrutura repetitiva whileTrue se usa cuando
#al menos una vez se debe ejecutar el ciclo, por ejemplo
#pediremos la edad de una persona, y repetiremos la petición mientras
#la edad no esté en un rango válido (1-120)
#whileTrue es igual a la estructura do-while de otros lenguajes

nombre=(input('Escribe tu nombre:'))

while True:
   edad=int(input('Escribe tu edad:'))
   if(edad>0) and (edad<=120):
      break
   print('Edad no válida, intenta de nuevo por favor...')

print(f'El nombre del usuario es: {nombre} y su edad: {edad}')  