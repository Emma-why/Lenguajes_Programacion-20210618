import pandas as pd

def calcular_promedios():
    data = {
        'Estudiante': ['juan', 'pedro', 'enmanuel', 'jose'],
        'Matematicas': [85, 92, 78, 95],
        'Naturales': [90, 88, 92, 89],
        'Sociales': [75, 80, 85, 90]
    }
    
    df = pd.DataFrame(data)
    df['Promedio'] = df[['Matematicas', 'Naturales', 'Sociales']].mean(axis=1)
    
    print(df)

calcular_promedios()
