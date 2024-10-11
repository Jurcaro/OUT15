import pandas as pd  
import re
import os

# Función para eliminar el primer "15" de un número
def eliminar_primer_15(numero):
    numero_str = str(numero)  # Convertimos el número a string
    # Usar regex para eliminar el primer "15" encontrado
    nuevo_numero = re.sub(r'15', '', numero_str, count=1)
    return nuevo_numero

# Cargar el archivo Excel
def procesar_excel(ruta_archivo):
    # Lee el archivo Excel en un DataFrame
    df = pd.read_excel(ruta_archivo)

    # Suponiendo que los números de línea están en una columna llamada 'numeros_linea'
    # Si la columna tiene otro nombre, cámbialo en el código
    df['numeros_linea_procesado'] = df['numeros_linea'].apply(eliminar_primer_15)

    # Definir la ruta de salida en la carpeta OUTPUT
    ruta_salida = 'C:/Users/Usuario/PROYECTOS.GS/OUT15/output/archivo_procesado.xlsx'

    # Asegurarse de que la carpeta OUTPUT exista
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)

    # Eliminar la primera columna del DataFrame
    df = df.iloc[:, 1:]

    # Guardar el nuevo DataFrame en un nuevo archivo Excel
    df.to_excel(ruta_salida, index=False)
    print(f"Archivo procesado guardado como '{ruta_salida}'")

# Llamar a la función procesar_excel con la ruta del archivo
ruta_archivo = 'C:/Users/Usuario/PROYECTOS.GS/OUT15/input/OUT15.xlsx'  # Cambia esto a tu ruta
procesar_excel(ruta_archivo)
