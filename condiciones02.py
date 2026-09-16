#El porgrama pedira el costo de un producto, si es mayor 
#que mil pesos, calculara el 20% de descuento y mostrara
#lo que iba a pagar, el descuento y lo que va a pagar ahora
#en caso contrario mostrara lo mismo pero con un 10% de descuento 

costo=float(input('Escribe el total del producto:'))
if(costo>=1000):
    descuento=costo*.20
    print('Ibas a pagar:',costo)
    print('Tu descuento es de:',descuento)
    totalReal=costo-descuento
    print('Ahora pagarás:',totalReal)
else:
    descuento=costo*.10
    print('Ibas a pagar:',costo) 
    print('Tu descuento es de:',descuento)   
    totalReal=costo-descuento
    print('Ahora pagarás:',totalReal)