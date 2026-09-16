from graphviz import Digraph

# Crear el mapa mental
mapa = Digraph(format='png')
mapa.attr(rankdir='TB', size='8,8')

# Tema central
mapa.node('A', 'Ethernet')

# Subtemas principales
mapa.node('B', 'Concepto')
mapa.node('C', 'Tipos')
mapa.node('D', 'Ventajas')
mapa.node('E', 'Desventajas')
mapa.node('F', 'Funcionamiento')

# Conexiones principales
mapa.edges(['AB', 'AC', 'AD', 'AE', 'AF'])

# Subtemas secundarios
mapa.node('B1', 'Red cableada')
mapa.node('B2', 'Transmisión de datos')

mapa.node('C1', 'Fast Ethernet')
mapa.node('C2', 'Gigabit Ethernet')

mapa.node('D1', 'Alta velocidad')
mapa.node('D2', 'Seguridad')

mapa.node('E1', 'Uso de cables')
mapa.node('E2', 'Costo instalación')

mapa.node('F1', 'Tramas')
mapa.node('F2', 'Direcciones MAC')

# Conexiones secundarias
mapa.edges([
    ('B', 'B1'), ('B', 'B2'),
    ('C', 'C1'), ('C', 'C2'),
    ('D', 'D1'), ('D', 'D2'),
    ('E', 'E1'), ('E', 'E2'),
    ('F', 'F1'), ('F', 'F2')
])

# Guardar y mostrar
mapa.render('mapa_mental_ethernet', view=True)