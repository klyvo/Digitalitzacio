# Pedir una frase al usuario
frase = input("Escribe una frase: ")

# Dividir la frase en palabras (por espacios)
palabras = frase.split()

# Invertir el orden de las palabras
palabras_invertidas = palabras[::-1]

# Unirlas de nuevo en una sola cadena
frase_invertida = " ".join(palabras_invertidas)

# Mostrar el resultado
print(frase_invertida)
