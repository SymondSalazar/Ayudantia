#Tenemos una cadena de caracteres y queremos extraer una parte de ella.
cadena = "Voy a aprobar el primer parcial de Fundamentos de Programacion"

#Slicing [inicio:fin]
print("---- Slicing del tipo [inicio:fin]----")
print(cadena[0:3])  # Imprime "Voy"

#Slicing [inicio: ]
print("---- Slicing del tipo [inicio:] ----")
print(cadena[4:])  # Imprime "a aprobar el primer parcial de Fundamentos de Programacion"

#Slicing [:fin]
print("---- Slicing del tipo [:fin] ----")
print(cadena[:3])  # Imprime "Voy"

#Slicing [inicio:fin:paso]
print("---- Slicing del tipo [inicio:fin:paso] ----")
print(cadena[0:5:2])  # Imprime "Vya "

#Slicing para invertir la cadena
print("---- Slicing para invertir la cadena [::-1] ----")
print(cadena[::-1])  # Imprime "noicargorP sodnematnuF ed laicrap remip el a ropava a oV"