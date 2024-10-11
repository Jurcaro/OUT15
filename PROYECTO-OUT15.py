import pandas as pd  
import re
import os


def eliminar_primer_15(numero):
    numero_str = str(numero) 
   
    nuevo_numero = re.sub(r'15', '', numero_str, count=1)
    return nuevo_numero


def procesar_excel(ruta_archivo):
    
    df = pd.read_excel(ruta_archivo)

   
    df['numeros_linea_procesado'] = df['numeros_linea'].apply(eliminar_primer_15)

   
    ruta_salida = 'C:/Users/Usuario/PROYECTOS.GS/OUT15/output/archivo_procesado.xlsx'

   
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)

   
    df = df.iloc[:, 1:]

   
    df.to_excel(ruta_salida, index=False)
    print(f"Archivo procesado guardado como '{ruta_salida}'")


ruta_archivo = 'C:/Users/Usuario/PROYECTOS.GS/OUT15/input/OUT15.xlsx'  
procesar_excel(ruta_archivo)
