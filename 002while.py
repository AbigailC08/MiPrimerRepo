#el porgrama pedirá números y los irá sumando
#en una variable, para mostrar el total al final
#debe finalizar al recibir un 0

suma=0
numero=1
while numero !=0: #mientras numero no sea igual a 0
    numero=int(input('Ingresa un número para sumarlo (0) para salir):'))
    suma+=numero
    
print('La suma es:',suma)
