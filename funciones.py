#en la mayoria de los lenguajes de programacion se pueden
#crear pequeños bloques de codigo que realizen pocas tareas 
#estos bloques se llaman funciones (si devulven algun valor)
#o metodos (si no devuelven ningun valor)
#estos bloques de codigo normalmente estan antes del codigo
#principal del programa pero son llamdos solo desde el
#codigo principal o desde otra funcion o metodo

#crearemos un programa que pida dos numeros y 
#muestre un menu, realize las operaciones 
#arirtmeticas basicas usando funciones
import os
import time

def sumar (n1,n2):
    resultado=n1+n2
    return resultado
def restar (n1,n2):
    resultado=n1-n2
    return resultado
def multiplicacion (n1,n2):
    resultado=n1*n2
    return resultado
def division (n1,n2):
    resultado=n1/n2
    return resultado

while True:

 n1=float(input('Escribe el primer dato: '))
 n2=float(input('Escribe el segundo dato: '))

 opcion=int(input('Elige la posicion a realizar'
                    '\n1.Sumar'
                    '\n2.Restar'
                    '\n3.Multiplicacion'
                    '\n4.Division: '))


 if opcion==1:
    print('El resultado de la suma es: ', sumar (n1,n2))
    time.sleep(2)
    os.system('Clear') 
        
 if opcion==2:
    print('El resultado de la resta es: ', restar (n1,n2))
    time.sleep(2)
    os.system('clear')

 if opcion==3:
    print('El reesultado de la multiplicacion es: ', multiplicacion (n1,n2))
    time.sleep(2)
    os.system('clear')
        

 if opcion==4:
    print('El reesultado de la divison es: ' , division (n1,n2))
    time.sleep(2)
    os.system('clear')