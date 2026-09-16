
import os 
import time 
listaClientes=[] 
listaClaves=[]
listaCreditos=[]
 
while True:
 print('---MENU DE PRODUCTOS---'
       '\n1. Agregar Cliente'
       '\n2. Eliminar Cliente'
       '\n3. Buscar un Cliente'
       '\n4. Modificar un Cliente'
       '\n5. Mostrar lista de Clientes'
       '\n6. Salir del Sistema')
 opcion=int(input('Elige una opción: '))
 if opcion==1: #create (insertar)
     clave=input('Clave del Cliente: ')
     cliente=input('Nombre del Cliente: ')
     credito=float(input('Limite de Credito: '))
     listaClaves.append(clave)
     listaClientes.append(cliente)
     listaCreditos.append(credito)
     print('Cliente guardado en el sistema')
     time.sleep(2)
     os.system('Clear') 
 elif opcion==2: 
    nombre=input('Nombre del Cliente a eliminar: ')
    if cliente in listaClientes:
       indice=listaClientes.index(cliente)
       listaClientes.remove(cliente)
       for x in listaClaves:
          if x==indice:
             listaCreditos.pop()
       
       print('Cliente eliminado del sistema')
       time.sleep(2)
       os.system('clear')
 elif opcion==3: 
    nombre=input('Nombre del Cliente a buscar: ')
    if nombre in listaClientes:
       print('El cliente está en la posicion:'
             ,listaClientes.index(nombre)+1)
       time.sleep(2)
       os.system('clear')
    else:
       print('El cliente no se encuentra en el sistema')
       time.sleep(2)
       os.system('clear')   
 elif opcion==5: 
    print('El listado de Clientes es:')
    print(listaClaves)
    print(listaClientes)
    print(listaCreditos)
    time.sleep(4)
    os.system('clear')
 elif opcion==6:
   respuesta=input("Estas seguro? (Si/No) ")
   if respuesta.upper()=="Si":
      print("Saliendo del sistema")
      time.sleep(2)
      os.system("clear")
      break
   else:
      time.sleep(1)
      os.system("clear")
 #else:
  # print("Esa opcion no existe, intente de nuevo")
   #time.sleep(2)
   #os.system("clar")