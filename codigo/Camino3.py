import matplotlib
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import time as t

#importamos los datos y los convertimos en un dataframe
df = pd.read_csv('calles_de_medellin_con_acoso.csv', sep=';')
df.set_index([ 'origin'], inplace=True)
df.head()
df.loc['(-75.5715105, 6.2063061)']
df.describe()
df['weight'] = df['length'] * df['harassmentRisk']
DG = nx.DiGraph()
for row in df.iterrows():
    DG.add_edge(row[0], row[1]['destination'], weight=row[1]['weight'])
Camino = nx.dijkstra_path(DG, source = '(-75.5715105, 6.2063061)' ,target = '(-75.5656961, 6.2096595)', weight = 'weight')
print("Segunda Ruta mas corta: ")
print(Camino)
ruta1=DG.subgraph(Camino)
pos = nx.spring_layout(ruta1)
nx.draw(ruta1, pos, with_labels=True, node_size=700, node_color='lightgreen', font_size=9, font_color='black', font_weight='bold', width=2, edge_color='dodgerblue')
plt.show()

inicio = t.time()
t.sleep(1)
fin = t.time()
print("El tiempo de ejecucion del tercer algoritmo fue de: ", fin - inicio, "segundos")
#Complejidad temporal en terminos de V y E 
#V es el numero de vertices y E el numero de aristas
#O(V^2) + O(E) = O(V^2)
#Complejidad de la memoria en terminos de V y E
#O(V) + O(E) = O(V)

