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
djk_path = nx.dijkstra_path(G, source = '(-75.5728593, 6.2115169)' ,target = '(-75.5681218, 6.2063043)', weight = 'weight')
print("El camino mas corto y con menos acoso es:")
print(djk_path)
ruta1=G.subgraph(djk_path)
pos = nx.spring_layout(ruta1)
nx.draw(ruta1, pos, with_labels=True, node_size=700, node_color='lightgreen', font_size=9, font_color='black', font_weight='bold', width=2, edge_color='dodgerblue')
plt.show() 
T = t.time()
print("Tiempo de ejecucion: ", T)