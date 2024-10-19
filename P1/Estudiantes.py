import pandas as pd
import numpy as np
from pprint import pprint
from typing import Tuple

def analizar_rendimiento(archivo: str) -> Tuple[int, int, pd.DataFrame]:
    try:
        estudiantes_df = pd.read_csv(archivo)
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{archivo}' no fue encontrado.")
    except pd.errors.EmptyDataError:
        raise ValueError("El archivo esta vacio.")
    
    try:
        if not all(col in estudiantes_df.columns for col in ['Matematicas', 'Ciencias', 'Historia']):
            raise KeyError("Faltan columnas necesarias: 'Matematicas', 'Ciencias', 'Historia'.")

        estudiantes_df['Promedio'] = estudiantes_df[['Matematicas', 'Ciencias', 'Historia']].mean(axis=1)

        estudiantes_df['Estado'] = np.where(estudiantes_df['Promedio'] >= 60, 'Aprobado', 'Reprobado')

        aprobados = estudiantes_df[estudiantes_df['Estado'] == 'Aprobado'].shape[0]
        reprobados = estudiantes_df[estudiantes_df['Estado'] == 'Reprobado'].shape[0]

        estudiantes_aprobados = estudiantes_df[(estudiantes_df['Matematicas'] >= 70) & 
                                               (estudiantes_df['Ciencias'] >= 70) & 
                                               (estudiantes_df['Historia'] >= 70)]

    except KeyError as e:
        raise KeyError(f"Error de clave: {e}")
    except Exception as e:
        raise RuntimeError(f"Error inesperado durante el analisis del rendimiento académico: {e}")

    return aprobados, reprobados, estudiantes_aprobados

try:
    aprobados, reprobados, estudiantes_aprobados = analizar_rendimiento('P1/estudiantes.csv')
    print("Numero de aprobados:", aprobados)
    print("Numero de reprobados:", reprobados)
    print("\nEstudiantes que aprobaron todas las materias con calificacion >= 70:")
    pprint(estudiantes_aprobados)
except Exception as e:
    print(e)
