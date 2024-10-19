import pandas as pd

def filtrar_ventas_mayores_a_500(archivo_csv):
    df = pd.read_csv(archivo_csv)
    ventas_mayores_500 = df[df['Ventas'] > 500]
    
    print(ventas_mayores_500)

filtrar_ventas_mayores_a_500('S3/Enmanuel.csv')
