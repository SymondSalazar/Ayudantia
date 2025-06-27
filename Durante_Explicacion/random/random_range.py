#Primero se importa el modulo random
import random as rd
#rd es un alias para el modulo random
print("---- Modulo random --")
#Generar un numero aleatorio entre 0 y 1 
numero_aleatorio = rd.random()
print("---- Numero aleatorio entre 0 y 1 --")
print(numero_aleatorio)

#Generar un numero aleatorio entre 1 y 10
numero_aleatorio = rd.randint(1, 10)
print("---- Numero aleatorio entre 1 y 10 --")
print(numero_aleatorio)

#Generar un numero aleatorio entre 0 y 10 con un paso de 2
numero_aleatorio = rd.randrange(0, 10, 2)
print("---- Numero aleatorio entre 0 y 10 con paso de 2 --")
print(numero_aleatorio)



####Range
print("---- Range ----")
#Genera una lista de numeros entre 0 y b-1
numeros = list(range(0, 10))
print("---- Lista de numeros entre 0 y 9 --")
print(numeros)

#Genera una lista de numeros entre 4,10
numeros = list(range(4, 11))
print("---- Lista de numeros entre 4 y 10 --")
print(numeros)

#Genera una lista de numeros entre 0,10 con un paso de 2
numeros = list(range(0, 11, 2))
print("---- Lista de numeros entre 0 y 10 con paso de 2 --")
print(numeros)