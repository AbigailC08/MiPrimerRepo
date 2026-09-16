#el programa contiene un numero secreto, el 
#usuario debe adivinar, tiene 3 oportunidades

numeroSecreto=9
adivinado=False
intentos=0
quedan=3

print('Solo tienes 3 intentos')
while not (adivinado) and (intentos<3):
    dato=int(input('Adivina el número (es menor que 10):'))
    if(dato==numeroSecreto): #si adivina
        print('Felicidades, adivinaste...')
        adivinado=True
    else: #si no adivina 
        intentos+=1 #lleva un intento mas
        if(intentos==3):
            print('Juego terminado...')    