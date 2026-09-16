#el programa debe imprimir en pantalla los
#numeros del 1 al 100 pero, solo debe sumar
#los numeros del 20 al 40 y del 60 al 80
#al finalizar, debe mostrar el mensaje:
#la suma de los numeros capturas es: xx
resultado=0

#import time
for contador in range(101):
    print(contador)
    #time.sleep(0.5)
    if (contador>20) and (contador<=40):
        resultado+=contador    

    if (contador>60) and (contador<=80):
        resultado+=contador

print('La suma de los numeros capturados es:',resultado)
