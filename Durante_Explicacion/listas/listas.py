#Asi se crea una lista
Lista = [1, 2, 3, 4, 5]
#Imprimir la lista
print("---- Lista ----")
print(Lista)

#Puede contener cualquier tipo de dato
Lista = [1, 2.5, "Hola", True, [1, 2, 3]]
#Imprimir la lista
print("---- Lista con diferentes tipos de datos ----")
print(Lista)

#Mutabilidad de las listas
#Las listas son mutables, se pueden modificar
Lista = [1, 2, 3, 4, 5]
#Modificar el tercer elemento de la lista
Lista[2] = 10  # Cambia el tercer elemento (índice 2
#Imprimir la lista despues de modificar un elemento
print("---- Lista despues de modificar un elemento ----")
print(Lista)


#Unir dos listas
Lista1 = [1, 2, 3]
Lista2 = [4, 5, 6]
ListaUnida = Lista1 + Lista2
#Imprimir la lista unida
print("---- Lista unida ----")
print(ListaUnida)

#Borrar un elemento de la lista
Lista = [1, 2, 3, 4, 5]
del Lista[2]  # Elimina el tercer elemento (índice 2)
#Imprimir la lista despues de borrar un elemento
print("---- Lista despues de borrar un elemento ----")
print(Lista)

#Algunas funciones de random para listas
print("---- Funciones de random para listas ----")
import random as rd

#Elegir un elemento aleatorio de la lista
Lista = [1, 2, 3, 4, 5]
elemento_aleatorio = rd.choice(Lista)
#Imprimir el elemento aleatorio
print("---- Elemento aleatorio de la lista ----")
print(elemento_aleatorio)

#Mezclar los elementos de la lista
Lista = [1, 2, 3, 4, 5]
rd.shuffle(Lista)
#Imprimir la lista mezclada
print("---- Lista mezclada ----")
print(Lista)

#Elegir varios elementos aleatorios de la lista
Lista = [1, 2, 3, 4, 5]
elementos_aleatorios = rd.sample(Lista, 3)  # Elige 3 elementos aleatorios
#Imprimir los elementos aleatorios
print("---- Elementos aleatorios de la lista ----")
print(elementos_aleatorios)

#Funciones y metodos de listas
print("---- Funciones y metodos de listas ----")
#Obtener la longitud de la lista
Lista = [1, 2, 3, 4, 5]
longitud = len(Lista)
#Imprimir la longitud de la lista
print("---- Longitud de la lista ----")
print(longitud)

#Agregar un elemento al final de la lista
Lista = [1, 2, 3, 4, 5]
Lista.append(6)
#Imprimir la lista despues de agregar un elemento
print("---- Lista despues de agregar un elemento ----")
print(Lista)

#Insertar un elemento en una posicion especifica de la lista
Lista = [1, 2, 3, 4, 5]
Lista.insert(2, 2.5)  # Inserta 2.5 en
# la posicion 2 (tercer elemento)
#Imprimir la lista despues de insertar un elemento
print("---- Lista despues de insertar un elemento ----")
print(Lista)

#Eliminar el primer elemento de la lista
Lista = [1, 2, 3, 4, 5]
Lista.remove(3)  # Elimina el primer elemento con valor 3
#Imprimir la lista despues de eliminar un elemento
print("---- Lista despues de eliminar un elemento ----")
print(Lista)

#Eliminar el ultimo elemento de la lista
Lista = [1, 2, 3, 4, 5]
Lista.pop()  # Elimina el ultimo elemento y lo devuelve
#Imprimir la lista despues de eliminar el ultimo elemento
print("---- Lista despues de eliminar el ultimo elemento ----")
print(Lista)

#Ordenar los elementos de la lista
Lista = [5, 3, 1, 4, 2]
Lista.sort()  # Ordena la lista en orden ascendente
#Imprimir la lista ordenada
print("---- Lista ordenada ----")
print(Lista)

#Invertir el orden de los elementos de la lista
Lista = [1, 2, 3, 4, 5]
Lista.reverse()  # Invierte el orden de los elementos
#Imprimir la lista invertida
print("---- Lista invertida ----")
print(Lista)

#Contar el numero de veces que un elemento aparece en la lista
Lista = [1, 2, 3, 4, 5, 3]
contador = Lista.count(3)  # Cuenta cuantas veces aparece el numero 3
#Imprimir el contador
print("---- Contador de elementos ----")
print(contador)

#Encontrar el indice del primer elemento que coincide con un valor
Lista = [1, 2, 3, 4, 5]
indice = Lista.index(3)  # Encuentra el indice del primer elemento con valor 3
#Imprimir el indice
print("---- Indice del primer elemento que coincide con un valor ----")
print(indice)

#Limpiar la lista
Lista = [1, 2, 3, 4, 5]
Lista.clear()  # Elimina todos los elementos de la lista
#Imprimir la lista despues de limpiarla
print("---- Lista despues de limpiarla ----")
print(Lista)

#Obtener el valor maximo y minimo de la lista
Lista = [1, 2, 3, 4, 5]
maximo = max(Lista)  # Obtiene el valor maximo de la lista
minimo = min(Lista)  # Obtiene el valor minimo de la lista
#Imprimir el valor maximo y minimo de la lista
print("---- Valor maximo y minimo de la lista ----")
print("Maximo:", maximo)
print("Minimo:", minimo)

