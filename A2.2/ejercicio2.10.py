# Frase
frase = "Hola mundo, esto es una frase de prueba"


# Usar split() por defecto (divide por espacios)
palabras_espacios = frase.split()
print(palabras_espacios)

frecuenciaPalab = [frase.count(w) for w in frase]

print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
