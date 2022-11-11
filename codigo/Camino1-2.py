from ensurepip import version
from platform import node
from tkinter import font
import pandas as pd
import geopandas as gpd
import networkx as nx
import matplotlib.pyplot as plt
import time as t
from shapely import wkt
import pyogrio as ogrio

#importamos los datos y los convertimos en un dataframe
df = pd.read_csv('calles_de_medellin_con_acoso.csv', sep=';')
#Generemos la grafica a partir del dataframe con los datos
G = nx.from_pandas_edgelist(df, 'origin', 'destination',edge_attr=['length','harassmentRisk'],create_using=nx.DiGraph())

G.nodes()
G.edges()
G.order()
# for x in G.nodes():
#     if G.in_degree(x) > 4:n
#         print(x)
#obtener un producto entre el riesgo de acoso y la distancia 
#para obtener el peso de cada arista
df['weight'] = df['length'] * df['harassmentRisk']
#convertimos el dataframe en un diccionario
dict = df.set_index('origin')['weight'].to_dict()
#agregamos el diccionario como atributo de los nodos
nx.set_node_attributes(G, dict, 'weight')
#obtenemos el camino mas corto
djk_path = nx.dijkstra_path(G, source = '(-75.5715105, 6.2063061)' ,target = '(-75.5656961, 6.2096595)', weight = 'weight')
print("El camino mas corto y con menos acoso es:")
print(djk_path)
ruta1=G.subgraph(djk_path)
pos = nx.spring_layout(ruta1)
nx.draw(ruta1, pos, with_labels=True, node_size=700, node_color='lightgreen', font_size=9, font_color='black', font_weight='bold', width=2, edge_color='dodgerblue')
plt.show() 
inicio = t.time()
t.sleep(1)
fin = t.time()
print("El tiempo de ejecucion fue de: ", fin - inicio, "segundos")
 

#Complejidad temporal en terminos de V y E:
#V es el numero de vertices y E el numero de aristas
#O(V^2) + O(E) = O(V^2)
#Complejidad de la memoria en terminos de V y E
#O(V) + O(E) = O(V)
 




#Ruta alternativa 2
 
#eliminamos el nodo que se encuentra en la mitad del camino
G.remove_node('(-75.5681218, 6.2063043)')

#obtenemos el camino mas corto
djk_path2 = nx.dijkstra_path(G, source = '(-75.5715105, 6.2063061)' ,target = '(-75.5656961, 6.2096595)', weight = 'weight')
print("Segunda Ruta alternativa :")
print(djk_path2)
ruta2 = G.subgraph(djk_path2)
pos = nx.spring_layout(ruta2)
nx.draw(ruta2, pos, with_labels=True, node_size=700, node_color='lightgreen', font_size=9, font_color='black', font_weight='bold', width=2, edge_color='dodgerblue')
plt.show()
inicio2 = t.time()
t.sleep(1)
fin2 = t.time()
print("El tiempo de ejecucion del segundo algoritmo  fue de: ", fin2 - inicio2, "segundos")


 

