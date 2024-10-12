def sumar_submatrices(matriz):
    n = len(matriz)  # Suponemos que la matriz es cuadrada
    sumas = []
    for tam in range(1, n + 1):
        for i in range(n - tam + 1):
            for j in range(n - tam + 1):
                suma = 0
                for x in range(i, i + tam):
                    for y in range(j, j + tam):
                        suma += matriz[x][y]
                sumas.append(suma)
    
    return sumas