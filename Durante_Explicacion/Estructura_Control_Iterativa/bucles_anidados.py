#Los bucles tambien pueden estar anidados, es decir, un bucle dentro de otro.
print("---- Tablas de multiplicar ----")
for i in range(1, 13):
    print("Tabla del", i)
    for j in range(1, 11):
        print(i, "*", j, "=", i * j)


