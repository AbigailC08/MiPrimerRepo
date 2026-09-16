#el programa debe pedir el costo de productos 
#y debe avisar que (escriba 0 para salir)
#al final debe mostrar el total a pagar y la cantidad 
#de productos comprados
total=0
productos=0

#while True:
    #producto=int(input('Escribe el costo de producto (0 para salir):'))
    #if producto==0:
        #break
    #productos+=1
    #total+=producto

#print('Total a pagar:',total)
#print('Total de productos comprados:',productos)


total=0
productos=0

for x in range(10001):
    producto=int(input('Escribe el costo de producto (0 para salir):'))
    if producto==0:
        break
    productos+=1
    total+=producto

print('Total a pagar:',total)
print('Total de productos comprados:',productos)
