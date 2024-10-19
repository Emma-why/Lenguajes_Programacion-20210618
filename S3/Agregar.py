import pandas as pd

def agregar_columna_mayor_de_edad():
    data = {'Nombre': ['Ana', 'Juan', 'Maria', 'Pedro'], 'Edad': [25, 17, 30, 19]}
    df = pd.DataFrame(data)
    
    def es_mayor_de_edad(edad):
        return "si" if edad >= 18 else "no"
    
    df['Mayor_de_edad'] = df['Edad'].map(es_mayor_de_edad)
    
    print(df)

agregar_columna_mayor_de_edad()
