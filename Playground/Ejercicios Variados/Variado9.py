"""
 Implemente la función verificar(cedula) que recibe un string con los 10 dígitos de un número de cédula
 ecuatoriana. La función debe retornar True si la cédula es válida o False en caso contrario. Para verificar la
 cédula, utilice el siguiente algoritmo:
 1. Se agrupan los nuevos (9) primeros dígitos en dos partes: los que están en índices pares y los que están
 en índices impares.
 2. Cada dígito en índice par se multiplica por dos (2). Solo si el resultado de esa multiplicación es mayor a
 nueve, se le resta nueve (9).
 3. Los dígitos en índices impares se mantienen inalterados.
 4. Se suman los dígitos del paso 2 y 3.
 5. Se toma el dígito más a la derecha del resultado de la suma del paso 4.
6. Si el resultado obtenido en el paso 5 es cero, entonces el dígito verificador es cero. En caso contrario, el
 dígito verificador será el número 10 menos el dígito del paso 5.
 7. Si el dígito verificador es igual al último dígito de la cédula, la cédula es válida.
 Ejemplo:
 Cédula => 1713175071
 Dígitos en índices pares => 1, 1, 1, 5, 7
 Multiplicados por 2 => 2, 2, 2, 10, 14
 Restados 9 => 2, 2, 2, 1, 5
 Dígitos en índices impares => 7, 3, 7, 0
 Suma de los nuevos dígitos => 29
 Último dígito de la suma => 9
 Dígito verificador => 10 - 9 = 1
 El dígito verificado es igual al último dígito de la cédula, entonces la función retorna True.
"""