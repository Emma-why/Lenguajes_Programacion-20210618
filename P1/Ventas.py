import pandas as pd
import numpy as np
from pprint import pprint
from typing import Tuple, Any

def analizar_ventas(archivo_ventas: str) -> Tuple[np.ndarray, float]:
    try:
        ventas_df = pd.read_csv(archivo_ventas)
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{archivo_ventas}' no fue encontrado.")
    except pd.errors.EmptyDataError:
        raise ValueError("El archivo está vacio.")
    
    try:
        ventas_df['Fecha'] = pd.to_datetime(ventas_df['Fecha'])

        if not all(col in ventas_df.columns for col in ['Cantidad', 'Precio', 'Descuento']):
            raise KeyError("Faltan columnas necesarias: 'Cantidad', 'Precio', 'Descuento'.")

        ventas_df['Venta total'] = ventas_df['Cantidad'] * ventas_df['Precio'] - ventas_df['Descuento']

        ventas_por_producto = ventas_df.groupby('Producto')['Venta total'].sum().sort_values(ascending=False)

        ventas_marzo = ventas_df[ventas_df['Fecha'].dt.month == 3]

        ventas_marzo_producto = ventas_marzo.groupby('Producto')['Venta total'].sum().values

        promedio_ventas_marzo = np.mean(ventas_marzo_producto)

    except KeyError as e:
        raise KeyError(f"Error de clave: {e}")
    except Exception as e:
        raise RuntimeError(f"Error inesperado durante el analisis de ventas: {e}")

    return ventas_por_producto, ventas_marzo_producto, promedio_ventas_marzo
try:
    ventas_por_producto, ventas_marzo_producto, promedio_ventas_marzo = analizar_ventas('P1/ventas.csv')
    print("Ventas por producto ordenadas:")
    pprint(ventas_por_producto)
    print("\nVentas en marzo por producto:")
    pprint(ventas_marzo_producto)
    print("\nPromedio de ventas en marzo:")
    print(promedio_ventas_marzo)
except Exception as e:
    print(e)
