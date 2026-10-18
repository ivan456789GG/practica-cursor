import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el archivo CSV
df = pd.read_csv('datos.csv')

# 2. Calcular estadísticas básicas
print("--- ESTADÍSTICAS BÁSICAS ---")
print("\nMedia (Promedio):")
print(df.mean())

print("\nMediana:")
print(df.median())

print("\nDesviación Estándar:")
print(df.std())

# 3. Generar la gráfica de dispersión (Scatter Plot)
plt.figure(figsize=(8, 5))
plt.scatter(df['x'], df['y'], color='blue', label='Datos X vs Y')
plt.title('Gráfica de Dispersión: X vs Y')
plt.xlabel('Columna X')
plt.ylabel('Columna Y')
plt.grid(True)
plt.legend()

# 4. Mostrar la gráfica en pantalla
plt.show()



