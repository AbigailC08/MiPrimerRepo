#un CRUD es una rutina básica en un sistema
#computancional, normalmente opera sobre una
#base de datos, pero nosotros simulamos 
#usando una, lista, si en un sistema manipulas
#informacion de clientes, productos, empelados,
#etc, para cada una de estas entidades debes realizar
#un CRUD, es decir una rutina que te pemrita:
#create: (insertar un cliente por ejemplo)
#read: (leer informacion del cliente)
#update: (modificar infromacion de un cliente)
#delete: (eliminar informacion de un cliente)
#se debe hacer un CRUD por cada entidad que se detecte.

import os #permite usar instrucciones del S.O 
import time #permite pausar la ejecucion del programa 
listaNombres=[] 
listaPrecios=[]
listaMarcas=[]
 
while True:
 print('---MENU DE PRODUCTOS---'
       '\n1. Agregar Clientes'
       '\n2. Eliminar Clientes'
       '\n3. Buscar un Clientes'
       '\n4. Modificar un Clientes'
       '\n5. Mostrar lista de Clientes'
       '\n6. Salir del Sistema')
 opcion=int(input('Elige una opción: '))
 if opcion==1: #create (insertar)
     nombre=input('Nombre del Cliente: ')
     marca=input('Marca del Cliente: ')
     costo=float(input('Costo del Cliente: '))
     listaNombres.append(nombre)
     listaMarcas.append(marca)
     listaPrecios.append(costo)
     print('Producto guardado en el sistema')
     time.sleep(2)
     os.system('Clear') #clear screen
 elif opcion==2: #delete (eliminar)
    nombre=input('Nombre del producto a eliminar: ')
    if nombre in listaNombres:
       indice=listaNombres.index(nombre)
       listaNombres.remove(nombre)
       for x in listaMarcas:
          if x==indice:
             listaMarcas.pop()
       for x in listaPrecios:
          if x==indice:
             listaPrecios.pop()     
       #listaMarcas.remove(listaMarcas.index(indice))
       #listaPrecios.remove()
       print('Producto eliminado del sistema')
       time.sleep(2)
       os.system('clear')
 elif opcion==3: #read (buscar un producto)
    nombre=input('Nombre del producto a buscar: ')
    if nombre in listaNombres:
       print('El producto existe, en la posicion:'
             ,listaNombres.index(nombre)+1)
       time.sleep(2)
       os.system('clear')
    else:
       print('Elproducto esta agotado')
       time.sleep(2)
       os.system('clear')   
 elif opcion==5: #read(consulta general)
    print('El listado de productos es:')
    print(listaNombres)
    print(listaMarcas)
    print(listaPrecios)
    time.sleep(4)
    os.system('clear')
 elif opcion==6:
   respuesta=input("Estas seguro? (s/n) ")
   if respuesta.upper()=="S":
      print("Saliendo del sistema")
      time.sleep(2)
      os.system("clear")
      break
   else:
      time.sleep(1)
      os.system("clear")
 else:
   print("Esa opcion no existe, intente de nuevo")
   time.sleep(2)
   os.system("clar")

          
