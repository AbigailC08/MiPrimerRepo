#simularemos el conteo regresivo para el
#despegue de un cohete 

import time #importaremos la libreria time
contador=10

print('Inicia el conteo regresivo...')
while(contador>0): #mientras contador sea > cero
    print(contador)
    time.sleep (1)
    contador-=1
print('El cohete ha despegado con éxito...')    