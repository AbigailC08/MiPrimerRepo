#Realiza un programa que pida números para promediarlos 
#el programa debe dejar de pedir números cuando se introduzca un cero
#al finalizar, debe mostrar la suma total de números, el promedio de estos 
#y cuantos números se introdujeron sin contar el cero.

contador=0 # 2
suma=0 # 20
while True:
  numero=float(input('Escribe un número (0 para salir):')) #mayor que 0, ejecuta 12 y 13
  if numero==0.0: #si el numero introducido es cero
    break #usamos break para salir del ciclo
  contador+=1 
  suma+=numero

#afuera del ciclo
if contador>0: #si metieron numeros validos 
  promedio=suma/contador
  print('La suma de los números es:', suma)
  print('El total de números introducidos es:',contador)
  print('El promedio de números ingresados es:',promedio)

else:
  print('Los números ingresados son inválidos, vuelve a intentar...') 
