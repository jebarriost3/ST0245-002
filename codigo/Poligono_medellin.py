import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely import wkt
#leer poligono_de_medellin.csv
df = pd.read_csv('poligono_de_medellin.csv',sep=';')
#crear un geodataframe a partir del dataframe
df['geometry'] = df['geometry'].apply(wkt.loads) #convertir la columna geometry a shapely
df = gpd.GeoDataFrame(df) #crear un geodataframe a partir del dataframe
plt.figure(figsize=(12,8)) #crear una figura
df.plot() #graficar el poligono
plt.title("Poligono de Medellín") #poner un titulo
plt.tight_layout() #ajustar el layout
plt.savefig("poligono-de-medellin.png") #guardar la figura
plt.show() #mostrar la figura
