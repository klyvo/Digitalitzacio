# Frase
a = input("Diga la frase para contar la frecuencia de palabras: ")


# Usar split() por defecto (divide por espacios)
palabras_espacios = a.split()

diccionario_cuento={}

for palabra in palabras_espacios:
    if palabra in diccionario_cuento:
        diccionario_cuento[palabra] = diccionario_cuento[palabra]+1
    else: diccionario_cuento[palabra] = 1

print("Cuento ", diccionario_cuento)

