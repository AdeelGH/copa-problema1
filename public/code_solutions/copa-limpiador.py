# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 20:09:46 2021

@author: adeel
"""
import pandas as pd
import itertools
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO

# Funcion para extraer el dia
def extraer_dia(row):
    if re.search('[a-zA-Z]', row['Col1']):
        val = row['Col1'][0:12]
    else:
        val = np.nan
    return val

# Funcion para extraer la hora de la fecha larga
def extraer_hora(row):
    if "Jan" in row['Col1']: 
        val = row['Col1'][12:21]
    else:
        val = row['Col1'][0:8]
    return val

# Leer linea por linea, reemplazar los separadores de lineas
with open(r'.\INRANGE_sample.txt', 'r') as file:
    for line in itertools.islice(file, 10, None):
        contents = file.read().replace('\n\n\n', ';')
        contents = contents.replace('\n', '')
        contents = contents.replace(';', '\n')
        
# Asignar los nombres de columnas       
contents = 'Col1\tCol2\tCol3\tCol4\tNoVuelo\tCol6\tCol7\tCol8\tCol9\tCol10\tCol11\tCol12\n' + contents;

# Leer contenido en un dataframe, delimitado por tab
df = pd.read_csv(StringIO(contents), sep='\t')

# Aplicar funciones para obtener dia y hora de primera columna
df['Dia'] = df.apply(extraer_dia, axis=1)
df['Hora1'] = df.apply(extraer_hora, axis=1)

# Rellenar el dia en las demas filas
df['Dia'].fillna(method='ffill', inplace=True)

# Convertir fecha larga en corta
df['Fecha'] = pd.to_datetime(df['Dia'], format='%b. %d, %Y').dt.date

# Remover punto de Matricula
patron_punto = re.compile(r'^\.')
df['Matricula'] = [patron_punto.sub('', x) for x in df['Col4']]

# Obtener dia (int)
df['Dia(int)'] = df['Col12'].str.extract(r'(\d\d)ARR')

# Obtener hora2
df['Hora_temp'] = df['Col12'].str.extract(r'\d\dARRIVING[A-Z]{4}(\d\d\d\d)')
df.Hora_temp = df.Hora_temp.astype(str)
df.Hora_temp = df.Hora_temp.str[:2] + ':' + df.Hora_temp.str[2:]
df['Hora2'] = pd.to_datetime(df['Hora_temp'],format= '%H:%M' ).dt.time

# Obtener Codigo de Aeropuerto
df['CodigoAeropuerto'] = df['Col12'].str.extract(r'\d\dARRIVING([A-Z][A-Z][A-Z][A-Z])')

# Obtener dia y hora
df['Fecha y hora'] = pd.to_datetime(df['Dia'] + ' ' + df['Hora_temp'])

# Armar Cuadro final
df = df[['Fecha','Hora1','NoVuelo','Matricula','Dia(int)','CodigoAeropuerto','Hora2','Fecha y hora']]

sns.set(font_scale=1.4)
df['Fecha'].value_counts().plot(kind='bar', figsize=(7, 6), rot=0)
plt.xlabel("Dia", labelpad=14)
plt.ylabel("Cantidad de Vuelos", labelpad=14)
plt.title("Cantidad de Vuelos por Dia", y=1.02);
plt.show()

sns.set(font_scale=1.4)
df['Dia(int)'].value_counts().plot(kind='bar', figsize=(7, 6), rot=0)
plt.xlabel("Dia (int)", labelpad=14)
plt.ylabel("Cantidad de Vuelos", labelpad=14)
plt.title("Cantidad de Vuelos por Dia (int)", y=1.02);
plt.show()

# Escribir a csv
df.to_csv(r'.\INRANGE_CLEAN.csv', sep='\t', encoding='utf-8', index=False)

