# Ejercicio 1

# Utilizamos un bucle for para iterar sobre los números generados por range.
# La función range(0, 101) genera números desde el 0 hasta el 100.
# El valor final del rango (101) no se incluye en la secuencia generada.
# Imprimimos cada número en una nueva línea gracias a la función print.

import random
for x in range(0, 101):
    # Imprimimos cada número en una nueva línea gracias a la función print.
    print(x)


# Ejercicio 2
# Se solicita al usuario por medio de un mensaje mediante la funcion "print" que ingrese un numero entero
print("Ingrese un numero entero")
# Al numero que ingresa el usuario se lo convierte a entero y se guarda en la variable "numero"
numero = int(input())

# Con la funcion "len" contamos la cantidad de digitos. Luego convertimos ese dato en texto con un string y por ultimo con
# la funcion "abs" eliminamos el signo negativo si ha sido ingresado así

cantidad_digitos = len(str(abs(numero)))

# Con un print mostramos el numero por pantalla
print("La cantidad de dígitos es:", cantidad_digitos)

# Ejercicio 3
# Solicitamos al usaurio que ingrese dos numeros por medio de un mensaje a traves de un print
print("Ingrese el primer numero entero: ")
# El numero ingresado se guarda en la variable "num1"
num1 = int(input())
print("Ingrese el segundo numero entero: ")
# El numero ingresado se guarda en la variable "num2"
num2 = int(input())

# En caso de que el primer numero ingresado sea el mayor, le pedimos al codigo que lo cambie de orden
if num1 > num2:
    num1,  num2 = num2, num1

# Inicializamos la variable que va a almacenar la suma en 0
suma = 0

# Usamos un bucle for para sumar los números entre num1 y num2, excluyendo los extremos
for i in range(num1 + 1, num2):
    # Realizamos la suma del iterador
    suma += i

# Por mensaje devolvemos el resultado
print("La suma de los números entre", num1, "y", num2, "es:", suma)

# Ejercicio 4
# Se inicializa la variable sumatoria en 0
sumatoria = 0

# Solcitamos al usuario el primer numero
num = int(input("Ingrese un número (0 para detenerse): "))

# Usamos un bucle while para seguir pidiendo números hasta que el número ingresado sea 0
while num != 0:
    # Sumamos el número a la variable sumatoria
    sumatoria += num

    # Le solicitamos otro número al usuario
    num = int(input("Ingrese un número (0 para detenerse): "))

# Mostramos el resultado final por medio de un mensaje
print("La suma total acumulada es:", sumatoria)


# Ejercicio 5
# Importamos la librería random para generar números aleatorios

# Generamos un número aleatorio entre 0 y 9 con la función ".randint"
numero_aleatorio = random.randint(0, 9)

# Inicializamos la variable "intentos" en 0
intentos = 0

# Declaramos la variable "acierto" con la función booleana "False"
acierto = False

# Cada vez que no adivina el número, se solicita al usuario otro
while not acierto:  # Usamos 'not acierto' para hacerlo más conciso
    # Solicitamos al usuario que ingrese un número por teclado y lo convertimos en entero
    intento = int(input("Adivina el número entre 0 y 9: "))

    # Aumentamos el contador de intentos en 1
    intentos += 1

    # Comparando la variable intento con el número aleatorio
    if intento == numero_aleatorio:
        acierto = True
        # Se termina de ejecutar el programa si acierta
        print(f"¡Adivinaste el número! Lo hiciste en {intentos} intentos.")
    else:
        # De lo contrario, se solicita otro intento
        print("Intenta nuevamente.")

# Ejercicio 6
# Usamos un bucle for con range para recorrer los números del 100 al 0, de dos en dos (asegurando que sean pares)
# Comenzamos desde el 100 porque está incluido, y terminamos en -1 para que también abarque el 0
for x in range(100, -1, -2):
    # Imprimimos cada número par en una misma columna (uno debajo del otro)
    print(x)


# Ejercicio 7
# Solicitamos al usuario que ingrese un número entero positivo
print("Ingrese un número entero positivo:")
# AL valor ingresado lo guardamos en la variable num y lo convertimos en entero con la funcion int
num = int(input())

# Inicializamos la variable sumatoria en 0
sumatoria = 0

# Usamos un bucle for para recorrer desde 0 hasta el número ingresado (inclusive)
for i in range(0, num + 1):
    # Sumamos cada valor del rango a la variable sumatoria
    sumatoria += i

# Con la funcion print mostramos el resultado por pantalla
print("La suma de los números entre 0 y", num, "es:", sumatoria)


# Ejercicio 8
# Definimos la cantidad de números que el usuario debe ingresar (valor que puede modificarse según la consigna)
cant = 10

# Inicializamos los contadores en 0
pares = 0
impares = 0
positivos = 0
negativos = 0

# Usamos un bucle for para pedir los números uno por uno
# range(1, cant + 1) incluye desde el 1 hasta el valor ingresado
for i in range(1, cant + 1):
    # Solicitamos al usuario que ingrese un número y lo convertimos en entero con int
    print("Ingrese el número", i, ":")
    numero = int(input())

    # Verificamos si es par o impar usando el operador %. Es par si el resto es 0, impar si no lo es
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Verificamos si es positivo o negativo comparando con 0
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

# Mostramos por pantalla los resultados de los conteos
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)

# Definimos la cantidad de números que el usuario debe ingresar (valor que puede modificarse según la consigna)
cant = 10

# Inicializamos las variables para la suma de los números y el contador
suma = 0

# Usamos un bucle para pedir los números al usuario
# Recorre desde 1 hasta 'cant' (en este caso hasta 10)
for i in range(1, cant + 1):
    # Muestra un mensaje solicitando el número (en la primera vuelta será "Ingrese el número 1", y así sucesivamente)
    print(f"Ingrese el número {i}:")
# Toma el valor ingresado por el usuario y lo convierte en entero
    numero = int(input())
# Acumula el número ingresado en la variable "suma"
    suma += numero

# Calculamos la media dividiendo la suma entre la cantidad de números
# La media es la suma total dividida por la cantidad de números que pedimos
media = suma / cant

# Por medio de la funcion "print" mostramos un mensaje por pantalla mostrando el resultado de la operacion
print(f"La media de los números ingresados es: {media}")

# Ejercicio 10
# Solicitamos al usuario que ingrese un número por medio de un mensaje con la funcion "print"
print("Ingrese un número:")
# Guardamos el valor ingresado por el usuario en la variable "numero".
numero = input()

# Invertimos la cadena de texto del número
# '[::-1]' es una forma en Python de invertir una cadena de texto.
# significa que estamos seleccionando todos los caracteres de la cadena, pero en orden inverso.
# Resolvemos que la variable esté asignada al numero ingresado por el usuario de forma invertida
numero_invertido = numero[::-1]

# Por pantalla mostramos el resultado
print(f"El número invertido es: {numero_invertido}")
