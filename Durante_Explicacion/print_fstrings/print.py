#Declarando las variables que voy a mostrar por pantalla
hola = "Hola, mundo!"
nombre = "Juan"
edad = 30

# Usando comas para imprimir múltiples variables
print('---- Usando comas ----')
print(hola)
print(hola,"mi nombre es", nombre)
print(hola,"mi nombre es", nombre,"y tengo", edad,"años.")

# Usando f-strings para imprimir múltiples variables
print('---- Usando f-strings ----')
print(f"{hola}")
print(f"{hola} mi nombre es {nombre}")
print(f"{hola} mi nombre es {nombre} y tengo {edad} años.")