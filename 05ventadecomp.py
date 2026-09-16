#Este programa sumará los costos de cada 
# componente de una computadora,
# para posteriormente dar el costo total, y 
#las mensualidades a pagar.

gabinete=int(input('Escribe el costo del Gabinete:'))
motherboard=int(input('Escribe el costo de la Motherboard:'))
procesador=int(input('Escribe el costo del Procesador:'))
memoria_ram=int(input('Escribe el costo de la Memoria Ram:'))
disco_duro=int(input('Escribe el costo del Disco Duro:'))
teclado=int(input('Escribe el costo del Teclado:'))
mouse=int(input('Escribe el costo del Mouse:'))
fuente_poder=int(input('Escribe el costo de la Fuente de Poder:'))

total=gabinete+motherboard+procesador+memoria_ram+disco_duro+teclado+mouse+fuente_poder
print('Total a pagar:', total)

iva=total*.16
print('IVA: {:.2f}'.format(iva))

meses=int(input('¿A cuántos meses deseas pagar?:'))
mensualidades=total/meses

print('Pagarás al mes: {:.2f}'.format(mensualidades))