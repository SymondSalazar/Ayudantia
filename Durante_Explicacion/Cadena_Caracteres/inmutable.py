# Ejemplo para demostrar la inmutabilidad de las cadenas en Python

# Se declara una variable con una cadena de caracteres
nombre = "Pedro"

# Mostramos el valor original
print("Valor original:", nombre)

# Intentamos cambiar el primer carácter de la cadena (esto dará error)
# nombre[0] = "M"  # Descomenta esta línea para ver el error: TypeError

# Para 'modificar' una cadena, debemos crear una nueva
nuevo_nombre = "M" + nombre[1:]
print("Nuevo valor (creando una nueva cadena):", nuevo_nombre)

# Comentario: Las cadenas son inmutables, no se pueden cambiar sus caracteres directamente.
