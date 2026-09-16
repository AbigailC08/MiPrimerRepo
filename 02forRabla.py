#el programa debe pedir un numero al usuario
#y mostrar la tabla de dicho numero

numero=int(input('De cuál número quieres la tabla?:'))
for contador in range(11):
    resultado=numero*contador
    print(f'{numero} * {contador}={resultado}')

print('Fin de la tabla...')    