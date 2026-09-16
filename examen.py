#Ejercicio 1. Crear un programa que pida el costo de 3 productos 
#(producto1, producto2, producto3), después debe sumarlos, si el total 
#es mayor que 500 pesos, debe avisar al
#usuario: '  Felicidades, ganaste un premio', en caso contrario debe 
#avisar: 'Sigue comprando para obtener un premio'

#Ejercicio 2. Crear un programa que pida el nombre y la edad de una persona 
#si su edad es menor que 11 años debe avisar, 'eres u niño'
#si la edad es mayor o igual a 11 pero menor que 19 debe avisar: 'Eres adolescente'
#si la edad es mayor o igual a 19 pero menor que 30 debe avisar: 'Eres joven'
#si la edad es mayor o igual a 30 pero menor que 45 debe avisar: 'Eres adulto'
#en cualquier otro caso debe avisar 'Eres adulto mayor'.

#Ejercicio 3. Se debe pedir la estatura de 3 personas (persona1, persona2, persona3)
#calcular el promedio y si es mayor que 1.70 debe avisar 'Son de buena estatura', en 
#cualquuier otro caso debe avisar 'Son de estatura baja'


cemento=int(input('Escribe el costo del Cemento:'))
varilla=int(input('Escribe el costo de la Varilla:'))
armex=int(input('Escribe el costo del Armex:'))

total=cemento+varilla+armex
print('Total a pagar:',total)

if total>500:
    print('Felicidades, ganaste un premio')
else:
    print('Sigue comprando para obtener un premio')
    