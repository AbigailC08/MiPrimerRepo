import time

contador=10
print('Inicia el conteo regresivo')
while (contador>0): #mientras contador sea mayor que 0 
 print(contador)
 time.sleep(1) #se dormirá un segundo
 contador-=1#le quitamos uno al valor de contador
print('El cohete ha despegado con éxito...') 

