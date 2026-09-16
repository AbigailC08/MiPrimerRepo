
import os
import time
import mysql.connector

mybd=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='tiendaITSJRC'
)

#creamos el cusor para ejecutar comandos en la BD
mycursor=mybd.cursor()
#crearemos el menu que me da el usuario 
#nuestro pequeño front end 

while True:
    print('---MENU DEL SISTEMA---'
          '\n1. Insertar un producto'
          '\n2. Eliminar un producto'
          '\n3. Buscar un producto'
          '\n4. Modfificar un producto'
          '\n5. Mostrar el catalogo de productos'
          '\n6. Salir del sistema')
    
    opcion=int(input('Elige una opción: '))
    if opcion==1: #create 
        clave=input('Ingresa la clave del producto: ')
        nombre=input('Ingresa el nombre: ')
        precio=float(input('Ingresa el precio: '))
        #creamos la instruccion SQL para insertar 
        sql='INSERT INTO productos (clave, nombre, precio) VALUES (%s,%s,%s)'
        #creamos la tupla para insertar
        val=(clave,nombre,precio)
        #preparamos los datos para insertar 
        mycursor.execute(sql,val)
        #insertamos 
        mybd.commit()
        #avisamos que ya se guardo la info
        print('Produto agregado al sistema ')
        time.sleep(2)
        os.system('clear') #clear

    if opcion==2: #Delete (eliminar un producto)
        clave=input('Ingresa el producto a eliminar: ')
        sql='DELETE FROM productos WHERE clave=%s'
        val=(clave,)
        mycursor.execute(sql,val)
        mybd.commit()
        print(mycursor.rowcount, 'Registro eliminado')
        time.sleep(2)
        os.system('clear')

    elif opcion==3: #Read (leer o buscar algo de la base de datos)
        clave=input('Ingresa el producto a buscar: ')
        sql='SELECT * FROM productos WHERE clave=%s'
        val=(clave,)
        mycursor.execute(sql,val)
        myresult=mycursor.fetchall()
        if myresult: #si hay resultados en la variable 
            print('El producto si está en la base de datos')
        else:
            print('El producto no está en la base de datos')
        time.sleep(2)
        os.system('Clear')
    elif opcion==4: #update (actualizar un registro de una table de la base
        claveAnterior=input('Ingresa el producto a actualizar: ')
        claveNuevo=input('Ingresa la clave nueva: ')
        sql='UPDATE productos WHERE clave=%s'
        val=(claveNuevo,claveAnterior)
        mycursor.execute(sql,val)
        mybd.commit()        
        print('El productos se ha modificado correctamente')
        time.sleep(2)
        os.system('Clear') 

    elif opcion==5:
        mycursor.execute('SELECT * FROM productos')
        myresult=mycursor.fetchall()
        print('Lista de productos: ')
        for x in myresult:
            print(x)
        time.sleep(10)   
        os.system('Clear')     

    elif opcion==6: #salir del sistema
        respuesta=input('Estás seguro? (s/n): ')
        if respuesta.upper()=='S':
            print('Saliendo del sistema...')           
            time.sleep(2)
            os.system('Clear')
            break 
        time.sleep(2)#en caso que la respuesta no sea 5
        os.system('Clear')

    # mybd.close()
