#crearemos la clase Triangulo, con un metodo para calcular su area
class Triangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def area (self): #estoy definiendo la funcion area
        return(self.base*self.altura)/2
    
base=float(input('Escribe la base del triangulo: '))
altura=float(input('Escribe la altura del triangulo: '))

triangulo=Triangulo(base,altura)
print('El área del triangulo es: ',triangulo.area())