#una lista es una etsructura de datos que, en python permite
#gaurdar informacion de diferente tipo, por ejemplo una misma
#lista puede guardar: numeros, texto, hasta objetos

#Realiza un porgrama que pida, usando listas, el nombre
#y el costo de 5 productos
#en una lista llamada IVA se debe guardar el IVA  a pagar 
#de  cada producto. Se debe crear una lista a pagar

nombres=[]
costos=[]
iva=[]
totales=[]
for x in range (3):
    nombre=input('Escribe el nombre del producto:')
    costo=float(input('Escribe el costo del producto:'))
    nombres.append(nombre)
    costos.append(costo)
for y in range (3):
    ivaprod=costos[y]*.16
    iva.append(ivaprod)
    print('El IVA del producto',y+1,'es:',ivaprod)
    
for r in range (3):
    total=costos[r]+iva[r]
    totales.append(total)

print()
for g in range(3):
    print()
    print(f'El producto es: {nombres [g]} Cuesta:{costos [g]} Iva:{iva [g]} Total:{totales [g]}' )
  