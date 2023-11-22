import pandas as pd
import matplotlib.pyplot as plt

# Cargar el DataFrame desde el archivo CSV
nombre_archivo_csv = 'empleadosbuf.csv'
df = pd.read_csv(nombre_archivo_csv, sep=';', encoding='ISO-8859-1')
df.rename(columns={'A�os': 'Años'}, inplace=True)

# Gráfico de barras para visualizar la distribución de cargos
plt.figure(figsize=(10, 6))
df['Cargo'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribución de Cargos de Empleados')
plt.xlabel('Cargo')
plt.ylabel('Cantidad de Empleados')
plt.xticks(rotation=45, ha='right')
plt.show()

'''plt.figure(figsize=(10, 6))
plt.scatter(df['Años'], df['Salario'], color='green', alpha=0.7)
plt.title('Relación entre Años y Salario de Empleados')
plt.xlabel('Años')
plt.ylabel('Salario')
plt.show()''' 

#Sacar de las '' el grafico que desees usar

'''plt.figure(figsize=(10, 6))
plt.hist(df['Años'], bins=20, color='orange', edgecolor='black')
plt.title('Distribución de Edades de Empleados')
plt.xlabel('Años')
plt.ylabel('Cantidad de Empleados')
plt.show()'''