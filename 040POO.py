class Vehiculo:
    def __init__(self,marca,tipo,modelo,color):
        self.marca=marca
        self.tipo=tipo
        self.modelo=modelo
        self.color=color

    def ficha_tecnica(self):
        print('\n---FICHA TECNICA DEL VEHICULO---\n') 
        print('La marca es: ',self.marca)
        print('El tipo es: ',self.tipo)
        print('El modelo es: ',self.modelo)
        print('El color es: ',self.color)
+{´}