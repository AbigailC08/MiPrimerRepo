#El programa pide la edad del usuario y la evalua
#si es menor a 18 debe avisar que no puede votar
edad=int(input('Escribe tu edad:'))
if(edad<18): #si edad es menos que 18
    print('Lo sentimos, no puedes votar')

else: #en cualquier otro caso
    print('Felicitaciones, si puedes votar')