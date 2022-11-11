import gmplot
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
# Cargamos los datos
data = pd.read_csv('poligono_de_medellin.csv', sep=';')

# Creamos el mapa
gmap = gmplot.GoogleMapPlotter(6.244203, -75.581211, 13)
  
# Creamos el poligono
gmap.polygon(data['lat'], data['lon'], 'cornflowerblue', edge_width=10)
 
# Dibujamos el mapa
gmap.draw("mapa.html")
  
# Mostramos el mapa
from IPython.display import IFrame
IFrame(src='mapa.html', width=700, height=600)
 
  


 
  
