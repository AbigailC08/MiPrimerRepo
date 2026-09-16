#El programa simula la compra de un vehículo, pide el precio y los meses
#para pagar, y muestra el costo de cada mensualidad.

#entrada de datos
costo=float(input('Cuánto cuesta el coche que vas a comprar:'))
meses=int(input('A cuántos meses los vas a pagar:'))
mensualidades=costo/meses
print('Pagarás cada mes:',mensualidades)
