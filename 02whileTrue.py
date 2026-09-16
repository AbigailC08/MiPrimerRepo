#El programa pedirá una edad y revisará que sea válida
edad=0
while True: #al menos una vez se debe ejecutar el ciclo
    edad=int(input('Escribe tu edad: '))
    if(edad>0) and (edad<120):
        break #salimos del ciclo
    print('Edad no válida, intenta de nuevo por favor...') 

print('La edad correcta es:', edad) 
   
