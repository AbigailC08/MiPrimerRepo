#el porgrama debe pedir numeros, pero solo debe sumar
#los que sean entre 20 y 40, cuando encuentre un numero 
#fuera de este rango, debe imprimir ESTE NUMERO NO SE SUMARA
#se debe salir del programa cuando el usuario introduzca el numero 99

suma=0

while True:
    numero=int(input('Escribe un número a sumar (99 para salir):'))
    if (numero==99):
        break 

    if(numero>=20 and numero<=40):
        suma+=numero

    else:
        print('ESTE NUMERO NO SE SUMARA')

print('La suma de los numeros es:', suma)        
 