print('Bienvenido a mi programa de Operaciones')

def main():
    while True:
        print('---MENU---'
              '\n1. Suma'
              '\n2. Resta'
              '\n3. Multiplicacion'
              '\n4. Salir')

        opcion = input('Elige la opcion (1-4): ')
        
        if opcion in ['1','2','3']:
            a=float(input('Ingresa el primer numero: '))
            b=float(input('Ingresa el segundo numero: '))
            
            if opcion=='1':
                print(f'Resultado: {a}+{b}={a+b}')
                
            if opcion=='2':
                print(f'Resultado: {a}-{b}={a-b}')

            if opcion=='3':
                print(f'Resultado: {a}*{b}={a*b}')
                
        else:
            opcion=['4']
            break 


        
# Ejecutar
main()
