import pandas as pd
import numpy as np
from pprint import pprint
from typing import Tuple

def analizar_inventario(archivo: str) -> Tuple[np.ndarray, pd.DataFrame]:
    try:
        inventario_df = pd.read_csv(archivo)
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{archivo}' no fue encontrado.")
    except pd.errors.EmptyDataError:
        raise ValueError("El archivo está vacío.")
    
    try:

        if not all(col in inventario_df.columns for col in ['Cantidad', 'Precio unitario', 'Costo de reabastecimiento']):
            raise KeyError("Faltan columnas necesarias: 'Cantidad', 'Precio unitario', 'Costo de reabastecimiento'.")

        inventario_df['Valor total en inventario'] = inventario_df['Cantidad'] * inventario_df['Precio unitario']

        valores_inventario = inventario_df['Valor total en inventario'].values

        cantidad_reabastecer = 50 - inventario_df['Cantidad']
        inventario_df['Costo reabastecimiento'] = np.where(inventario_df['Cantidad'] < 20, cantidad_reabastecer * inventario_df['Costo de reabastecimiento'], 0)
        productos_reabastecer = inventario_df[inventario_df['Cantidad'] < 20].sort_values(by='Costo reabastecimiento', ascending=False)

    except KeyError as e:
        raise KeyError(f"Error de clave: {e}")
    except Exception as e:
        raise RuntimeError(f"Error inesperado durante el análisis del inventario: {e}")

    return valores_inventario, productos_reabastecer


# Uso de pprint en los resultados
try:
    valores_inventario, productos_reabastecer = analizar_inventario('P1/inventario.csv')
    print("Valores totales en inventario:")
    pprint(valores_inventario)
    print("\nProductos que necesitan reabastecimiento:")
    pprint(productos_reabastecer[['Producto', 'Cantidad', 'Costo reabastecimiento']])
except Exception as e:
    print(e)
