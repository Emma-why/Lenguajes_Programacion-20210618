def segunda_palabra_mas_larga(cadena):
    palabras = cadena.split()
    palabras_ordenadas = sorted(palabras, key=lambda x: len(x))
    if len(palabras_ordenadas) >= 2:
        return palabras_ordenadas[1]
    return palabras_ordenadas[0]

print(segunda_palabra_mas_larga("Palabras Oracion manzanasez cascodemaco"))