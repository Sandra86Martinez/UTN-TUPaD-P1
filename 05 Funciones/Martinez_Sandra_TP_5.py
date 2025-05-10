# Ejercicio 1
# Inicializamos la variable con una lista vacía porque aun no tenemos el resultado de los numeros resultantes
lista_multiplos_4 = []

# El bucle for recorre los valores generados y con la funcion "range" determinamos los valores inciales (4, ya
# que es el primer numero positivo multiplo del mismo), finales (101 porque no toma el ultimo valor) y saltos (de 4 en 4)
for num in range(4, 101, 4):
    # Con la funcion ".append" añadimos los elementos a la lista antes creada
    lista_multiplos_4.append(num)

# Imprimir con la funcion "print" la lista para ver el resultado final los cuales contendrá solo los multiplos de 4
print(lista_multiplos_4)  # Esto muestra la lista con todos los múltiplos de 4

# Ejercicio 2
# Creamos una lista de 5 elementos. Elegí usar un string para los elementos de la misma
colores = ["rojo", "blanco", "azul", "rosa", "fucsia"]
# Traemos la lista correspondiente y con la indexación accedemos a un elemento específico dentro de una lista.
# En este caso, queremos mostrar el pénultimo elemento
print(colores[-2])


# Ejercicio 3
# Creamos una lista vacía que luego llenaremos con la función ".append"
lista_vacia = []
# Agregamos tres palabras (strings) a la lista usando ".append"
lista_vacia.append("Sandra")
lista_vacia.append("Dora")
lista_vacia.append("Susana")
# Mostramos por pantalla el resultado total de las adiciones
print(lista_vacia)


# Ejercicio 4
# Tomamos la lista del ejericio
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazamos el segundo valor (índice 1) con "loro" y el último valor (índice -1) con "oso"
animales[1] = "loro"
animales[-1] = "oso"

# Por ultimo, imprimimos por pantalla la lista actualizada. ['perro', 'loro', 'conejo', 'oso']
print(animales)


# Ejercicio 5
# Se presento una lista de numeros enteros
numeros = [8, 15, 3, 22, 7]
# Con la función "remove" eliminamos el primer elemento que se encuentra, con la condición que se pide.
# En este caso elimina el número mayor de la lista
numeros.remove(max(numeros))

# Con un print mostramos por pantalla la lista actualizada [8,15,3,7]
print(numeros)


# Ejercicio 6
# Creamos una lista vacía
lista_numeros = []

# El bucle for recorre los valores generados y con la funcion "range" determinamos los valores inciales (comienza desde el 10)
# finales (31 porque no toma el ultimo valor) y saltos (de 5 en 5)
for num in range(10, 31, 5):
    # Con la funcion ".append" añadimos los elementos a la lista antes creada donde se llenará con el resultado del bucle "for"
    lista_numeros.append(num)

# Creamos una variable para determinar por medio de "corchetes" que necesitamos extraer los dos primeros elementos
rango_lista = lista_numeros[0:2]
# Mostramos por pantalla el resultado de esos 2 elementos
print(rango_lista)


# Ejercicio 7
# Tomamos la lista del ejericio
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazamos el segundo y el tercer string (de los indices 1 y 2 con los valores que deseeamos
autos[1] = "rojo"
autos[2] = "azul"

# Por ultimo, imprimimos por pantalla la lista actualizada. ['sedan', 'rojo', 'azul', 'gol']
print(autos)


# Ejercicio 8
# Creamos una lista vacía
dobles = []

# Con la funcion ".append" vamos a agregar a la lista los resultados de las operaciones: el doble de los numeros 5, 10 y 15
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

# Mostramos por pantalla el resultado final de la lista actualizada
print(dobles)


# Ejercicio 9
# Tomando los valores descriptos en el ejercicio, creamos la lista "compras" que simula la compra de tres clientes
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# Primero, con la función ".append", agregamos un elemento a la lista del tercer cliente. Entre "corchetes"
# indicamos la lista deseada
compras[2].append("jugo")
# Para lista del segundo cliente debemos reemplazar el valor "fideos" por "tallarines"
compras[1][1] = "tallarines"
# En la primera lista, debemos eliminar el elemento "pan". Para ello utilizamos la función ".remove"
compras[0].remove("pan")
# Mostramos por pantalla los valores finales de la lista "compras": [['leche'], ['arroz', 'tallarines', 'salsa'], ['agua', 'jugo']]
print(compras)


# Ejericio 10
# Se crea la lista indicada en el ejercicio devolviendo en la misma los siguientes pasos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
# El resultado: En la posición 0 se encuentra el valor 15. El valor booleano True está en la posición 1.
# En la única lista anidada (posición 2) agregamos los valores: 25.5, 57.9 y 30.6. Finalmente,
# el valor booleano False se encuentra en la posición 3.
# Mostraremos por pantalla la lista anidada
print(lista_anidada)
