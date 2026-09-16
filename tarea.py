
import os
import time

clientes = {}

while True:
    print("---MENU DE CLIENTES---" 
          "\n1, Agregar clientes" 
          "\n2, Eliminar clientes" 
          "\n3, Buscar un cliente" 
          "\n4, Modificar un cliente" 
          "\n5, Mostrar lista de clientes" 
          "\n6, Salir del sistema")
    
    opcion=int(input("Elige una opcion: "))

    if opcion==1:
        clave=input("Ingrese la clave del cliente: ")
        nombre=input("Ingrese el nombre del cliente: ")
        limite_credito=float(input("Ingrese el límite de crédito del cliente: "))
        
        clientes[clave] = {"nombre": nombre, "limite_credito": limite_credito}
        
        print("Cliente agregado correctamente")
        time.sleep(2)
        os.system("clear")
        
    elif opcion==2:
        clave=input("Ingrese la clave del cliente a eliminar: ")
        
        if clave in clientes:
            del clientes[clave]
            print("Cliente eliminado correctamente")
            time.sleep(2)
            os.system("clear")
        else:
            print("Cliente no encontrado")
            time.sleep(2)
            os.system("clear")
            
    elif opcion==3:
        clave=input("Ingrese la clave del cliente a buscar: ")
        
        if clave in clientes:
            print("Cliente encontrado:")
            print("Nombre:", clientes[clave]["nombre"])
            print("Límite de crédito:", clientes[clave]["limite_credito"])
            time.sleep(4)
            os.system("clear")
        else:
            print("Cliente no encontrado")
            time.sleep(2)
            os.system("clear")
            
    elif opcion==4:
        clave=input("Ingrese la clave del cliente a modificar: ")
        
        if clave in clientes:
            nombre=input("Ingrese el nuevo nombre del cliente: ")
            limite_credito=float(input("Ingrese el nuevo límite de crédito del cliente: "))
            
            clientes[clave] = {"nombre": nombre, "limite_credito": limite_credito}
            
            print("Cliente modificado correctamente")
            time.sleep(2)
            os.system("clear")
        else:
            print("Cliente no encontrado")
            time.sleep(2)
            os.system("clear")
            
    elif opcion==5:
        print("Lista de clientes:")
        for clave, cliente in clientes.items():
            print("Clave:", clave)
            print("Nombre:", cliente["nombre"])
            print("Límite de crédito:", cliente["limite_credito"])
            print("------------------------")
        time.sleep(4)
        os.system("clear")
        
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