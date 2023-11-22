import pandas as pd

nombre_archivo_csv = 'empleadosbuf.csv'
df = pd.read_csv(nombre_archivo_csv, sep=';', encoding='ISO-8859-1')
df.rename(columns={'A�os': 'Años'}, inplace=True)

# Mostrar las primeras filas del DataFrame para verificar la carga
print("Primeras filas del DataFrame:")
print(df.head())

# 1. Suma de la columna 'Años'
suma_anios = df['Años'].sum()
print(f"\nSuma de Años: {suma_anios}")

# 2. Promedio de la columna 'Años'
promedio_anios = df['Años'].mean()
print(f"Promedio de Años: {promedio_anios}")

# 3. Máximo valor en la columna 'Años'
max_anios = df['Años'].max()
print(f"Máximo de Años: {max_anios}")

# 4. Mínimo valor en la columna 'Años'
min_anios = df['Años'].min()
print(f"Mínimo de Años: {min_anios}")

# 5. Suma de la columna 'IdEmpleado'
suma_id = df['IdEmpleado'].sum()
print(f"\nSuma de IdEmpleado: {suma_id}")

# 6. Promedio de la columna 'IdEmpleado'
promedio_id = df['IdEmpleado'].mean()
print(f"Promedio de IdEmpleado: {promedio_id}")

# 7. Máximo valor en la columna 'IdEmpleado'
max_id = df['IdEmpleado'].max()
print(f"Máximo de IdEmpleado: {max_id}")

# 8. Mínimo valor en la columna 'IdEmpleado'
min_id = df['IdEmpleado'].min()
print(f"Mínimo de IdEmpleado: {min_id}")

# 9. Obtener el empleado más joven
empleado_joven = df[df['Años'] == df['Años'].min()]
print("\nEmpleado más joven:\n", empleado_joven)

# 10. Obtener el empleado con el salario máximo
empleado_max_salario = df[df['Salario'] == df['Salario'].max()]
print("\nEmpleado con salario máximo:\n", empleado_max_salario)

# Ajustar los puestos según los ID y nombres
df['IdEmpleado'] = df.index + 1  
df['Nombre'] = df['Nombre'].str.capitalize()  
df['Apellido'] = df['Apellido'].str.capitalize() 

# Mostrar el DataFrame después de ajustar los puestos
print("\nDataFrame después de ajustar los puestos:")
print(df)