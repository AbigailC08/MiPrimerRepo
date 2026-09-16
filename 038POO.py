#crearemos la clase persona
class Persona: #crearemos la clase persona
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def saludar(self):
        print(f'Hola mi nombre es: {self.nombre} y mi edad: {self.edad}') 


persona1=Persona('Abigail',22) 
persona2=Persona('Araceli',22)

print('Se construyeron dos objetos, persona1 y persona2\n')
#accederemos a los atributos de estos objetos

print('El nombre de la persona1 es: ',persona1.nombre)
print('La edad de persona1 es: ',persona1.edad)

print('El nombre de la persona2 es: ',persona2.nombre)
print('La edad de persona2 es: ',persona2.edad)
#accederemos a los métodos de los objetos
