#El programa pedirá el costo de 5 productos, los 
#sumará y mostrará el total a pagar, usando la estructura de prog.
#secuencial 

producto1=int(input('Escribe el costo del primer producto:'))
producto2=int(input('Escribe el costo del segundo producto:'))
producto3=int(input('Escribe el costo del tercer producto:'))
producto4=int(input('Escribe el costo del cuarto producto:'))
producto5=int(input('Escribe el costo del quinto producto:'))

total=producto1+producto2+producto3+producto4+producto5
print('Total de los 5 productos:',total)
#este es un comentario para mostrar el IVA a pagar
iva=total*.16 
print('El IVA a pagar es:',iva)