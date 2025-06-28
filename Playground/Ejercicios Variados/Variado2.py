"""
Enunciado:

Implemente un programa que determine el porcentaje de efectividad de la función random.shuffle. Para esto:

Genere una lista de 40 números aleatorios únicos (sin repetidos) entre 1 y 200.

Repita los siguientes pasos 100 veces:

i. Desordene la lista original usando random.shuffle.

ii. Cuente cuántos elementos han cambiado de posición entre la lista original y la lista resultante (después de mezclarla). Llamemos a este valor X.

iii. Calcule el porcentaje de efectividad de la iteración actual:

    efectividad_iteracion = X * 100 / len(lista)

Calcule y muestre por pantalla el porcentaje de efectividad final, que es el promedio de los porcentajes de efectividad de las 100 repeticiones.
(Es decir, debe dividir la suma de todos los porcentajes de efectividad de las repeticiones entre 100).

Sample
"""
