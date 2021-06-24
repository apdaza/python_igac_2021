import pandas as pd
from random import randint, choice

nombres_ciudades = ['Bogotá', 'Cali', 'Chía', 'Bucaramanga', 'Cajica', 'Pereira',
             'Tulua', 'Medellin', 'Zipaquira', 'Cartagena']

tipos_generos = ['M', 'F']

nombres = []
edades = []
generos = []
ciudades = []
hijos = []
mascotas = []

for i in range(1000):
    nombres.append("persona_" + str(i))
    edades.append(randint(20, 70))
    generos.append(choice(tipos_generos))
    ciudades.append(choice(nombres_ciudades))
    hijos.append(randint(0,10))
    mascotas.append(randint(0,5))

data = {'nombres': nombres,
        'edades': edades,
        'generos': generos,
        'ciudades': ciudades,
        'hijos': hijos,
        'mascotas': mascotas}

data_set = pd.DataFrame(data, columns = ['nombres','edades','generos',
                                         'ciudades','hijos','mascotas'])

data_set.to_csv('info.csv')
