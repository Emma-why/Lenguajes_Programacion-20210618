import numpy as np

def multiplicar_promedio():
    array = np.arange(1, 11)
    array *= 2
    promedio = np.mean(array)
    
    print(array)
    print(promedio)

multiplicar_promedio()
