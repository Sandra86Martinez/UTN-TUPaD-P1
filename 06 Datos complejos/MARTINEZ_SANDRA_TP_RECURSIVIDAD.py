#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial 
# de todos los números enteros entre 1 y el número que indique el usuario

#Definimos la funcion factorial solicitada con el parametro "n"
def factorial(n):

    # Determinamos el caso base para que el codigo no sea infinito. 
    # Con un condicional: si n es 0 o 1, el factorial es 1 por definición.
    if n == 0 or n == 1:
        # Retorna 1 porque el factorial de 0 y 1 es 1, y sirve como caso base para detener la recursión.
        return 1
    
# Caso recursivo: para calcular el factorial de n, multiplicamos n por el factorial de n-1.
# Esto significa que la función se llama a sí misma con un número más pequeño,
# y así vamos descomponiendo el problema en partes más simples hasta llegar al caso base.
    return n * factorial(n - 1)


# Pedimos al usuario que ingrese por teclado un número entero positivo
numero_usuario = int(input("Ingrese un número entero positivo:"))

# Recorremos todos los números desde 1 hasta el número ingresado por el usuario (inclusive)
for i in range(1, numero_usuario + 1):
# i representa el número actual en la iteración
# Para cada número i, calculamos su factorial usando la función recursiva factorial()
    resultado = factorial(i)
    
    # Luego podemos mostrar el resultado con un print
    print(f"El factorial de {i} es: {resultado}")

#****************************************************************************************************************************#

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa 
# hasta la posición que el usuario especifique.

#Definimos la funcion solicitada (la tomé de un ejercicio de autoevaluacion)
def fibonacci_recursivo(pos):

    # Con un condicional, determinamos el caso base para que el codigo no sea infinito: si la posición es 0, devolvemos 0
    if pos == 0:
        return 0
    # Si la posición es 1, devolvemos 1
    elif pos == 1:
        return 1
    #Aqui comienzza el caso recursiovo: suma de los dos valores anteriores
    else:
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)

# Pedimos al usuario la posición hasta donde quiere ver la serie mediante un mensaje por pantalla
posicion_usuario = int(input("Ingrese la posición hasta la que quiere ver la serie de Fibonacci: "))

# Mostramos la serie completa desde la posición 0 hasta la ingresada por el usuario
print("Serie de Fibonacci completa hasta la posición", posicion_usuario, ":")

# Recorremos desde la posición 0 hasta la posición que indicó el usuario (inclusive)
for i in range(posicion_usuario + 1):
    # Calculamos el valor de Fibonacci en la posición i usando la función recursiva
    valor = fibonacci_recursivo(i)
    # Mostramos por pantalla la posición y el valor correspondiente mediante un print
    print(f"Posición {i}: {valor}")
    
    #*************************************************************************************************************#
    
    #3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1)
#Prueba esta función en un algoritmo general.


# Definimos la función recursiva para calcular la potencia
# base: el número que se va a elevar
# exponente: la potencia a la que se eleva la base (entero no negativo)
def potencia_recursiva(base, exponente):

    # Caso base para cortar la recursividad: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1

    # Caso recursivo: multiplicamos la base por la potencia con exponente reducido en 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

# Pedimos al usuario que ingrese la base por teclado (puede ser decimal)
base_usuario = float(input("Ingrese la base (número): "))

# Solicitamos al usuario que ingrese el exponente (entero no negativo)
exponente_usuario = int(input("Ingrese el exponente (entero no negativo): "))

# Validamos que el exponente sea un entero no negativo
if exponente_usuario < 0:
    print("Error: el exponente debe ser un entero no negativo.")
else:
    # Calculamos la potencia usando la función recursiva
    resultado = potencia_recursiva(base_usuario, exponente_usuario)
    # Mostramos el resultado por pantalla
    print(f"{base_usuario} elevado a la {exponente_usuario} es: {resultado}")
    
    #*********************************************************************************************************************************#
    #Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2. Para convertir un número decimal a 
# binario, se puede seguir este procedimiento:
#1. Dividir el número por 2.
#2. Guardar el resto (0 o 1).
#3. Repetir el proceso con el cociente hasta que llegue a 0.
#4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

# Definimos la función recursiva que convierte un número decimal a binario
# Recibe un número entero positivo y devuelve una cadena de texto con la representación binaria
def decimal_a_binario(numero):

    # Caso base: si el número es 0, devolvemos una cadena vacía para cortar la recursión
    if numero == 0:
        return ""

    # Caso recursivo:
    # Dividimos el número entre 2 y guardamos el resto (0 o 1)
    resto = numero % 2
    # Hacemos la llamada recursiva con el cociente de la división entera
    cociente = numero // 2

    # Construimos la cadena binaria llamando recursivamente con el cociente y
    # agregando el resto al final (que será el dígito binario menos significativo)
    return decimal_a_binario(cociente) + str(resto)

# Pedimos al usuario un número entero positivo
numero_usuario = int(input("Ingrese un número entero positivo en decimal: "))

# Si el número es 0, lo mostramos directamente para que no quede vacío
if numero_usuario == 0:
    print("El número en binario es: 0")
elif numero_usuario < 0:
    print("Error: debe ingresar un número entero positivo.")
else:
    # Calculamos la representación binaria usando la función recursiva
    binario = decimal_a_binario(numero_usuario)
    # Mostramos el resultado por pantalla
    print(f"El número {numero_usuario} en binario es: {binario}")
    
#***************************************************************************************************#

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba unacadena de texto sin espacios ni tildes, y devuelva True si 
# es un palíndromo o False si no lo es.
#Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed()

# Definimos la función recursiva que verifica si una palabra es palíndromo
# Recibe una cadena de texto (sin espacios ni tildes)
def es_palindromo(palabra):

    # len(palabra) devuelve la cantidad de caracteres que tiene la palabra
    # Caso base 1: si la palabra tiene 0 o 1 carácter, es palíndromo por definición
    if len(palabra) <= 1:
        return True  # Retornamos True porque una palabra vacía o con un solo carácter es palíndromo

    # palabra[0] es el primer carácter de la palabra
    # palabra[-1] es el último carácter de la palabra (índice negativo accede desde el final)
    # Caso base 2: si el primer y último carácter son diferentes, NO es palíndromo
    if palabra[0] != palabra[-1]:
        return False  # Retornamos False porque si no coinciden, no es palíndromo

    # Caso recursivo: si el primer y último carácter son iguales,
    # verificamos el resto de la palabra quitando esos dos caracteres
    # palabra[1:-1] devuelve una nueva cadena desde el segundo hasta el penúltimo carácter (excluyendo los extremos)
    return es_palindromo(palabra[1:-1])

# Pedimos al usuario que ingrese una palabra sin espacios ni tildes
# input() muestra el mensaje y espera que el usuario escriba algo y presione Enter
# .lower() convierte la palabra a minúsculas para evitar problemas con mayúsculas y minúsculas
palabra_usuario = input("Ingrese una palabra sin espacios ni tildes: ").lower()

# Llamamos a la función es_palindromo con la palabra ingresada y guardamos el resultado
resultado = es_palindromo(palabra_usuario)

# Mostramos el resultado por pantalla usando print()
if resultado:
    print(f"La palabra '{palabra_usuario}' es un palíndromo.")
else:
    print(f"La palabra '{palabra_usuario}' NO es un palíndromo.")
    
#****************************************************************************************************************#

#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
#Restricciones:
#No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión.
#Ejemplos:
#suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
#suma_digitos(9) → 9
#suma_digitos(305) → 8 (3 + 0 + 5)

# Definimos la función recursiva para sumar los dígitos de un número entero positivo
def suma_digitos(n):
    # Nuestro caso base: si el número es menor que 10 (es un solo dígito), devolvemos ese dígito
    if n < 10:
        return n
    else:
        # Bloque recursivo:
        # Obtenemos el último dígito usando el operador módulo %
        ultimo_digito = n % 10
        # Reducimos el número dividiéndolo por 10 (división entera //)
        resto_numero = n // 10
        # Retornamos la suma del último dígito más la suma de los dígitos del resto del número (recursión)
        return ultimo_digito + suma_digitos(resto_numero)

# Pedimos al usuario que ingrese un número entero positivo
numero_usuario = int(input("Ingrese un número entero positivo: "))

# Calculamos la suma de los dígitos usando la función recursiva
resultado = suma_digitos(numero_usuario)

# Mostramos el resultado por pantalla
print(f"La suma de los dígitos de {numero_usuario} es: {resultado}")

#****************************************************************************************************************************************#

#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así 
# sucesivamente hasta llegar al último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita 
# para construir toda la pirámide.
#Ejemplos:
#contar_bloques(1) → 1 (1)
#contar_bloques(2) → 3 (2 + 1)
#contar_bloques(4) → 10 (4 + 3 + 2 + 1)


# Definimos la función recursiva que calculará el total de bloques necesarios para la pirámide
def contar_bloques(n):
    # Caso base: si n es 1, solo hay un bloque, entonces devolvemos 1
    if n == 1:
        return 1
    
    # Parte recurisiva: sumamos los bloques del nivel actual (n) 
    # más el total de bloques necesarios para los niveles superiores (n-1)
    else:
        return n + contar_bloques(n - 1)

# Solicitamos al usuario que ingrese el número de bloques del nivel más bajo
nivel_bajo = int(input("Ingrese la cantidad de bloques en el nivel más bajo de la pirámide: "))

# Calculamos el total de bloques necesarios llamando a la función recursiva
total_bloques = contar_bloques(nivel_bajo)

# Mostramos el resultado al usuario
print(f"Para construir la pirámide con {nivel_bajo} bloques en la base, se necesitan {total_bloques} bloques en total.")

#**************************************************************************************************************#
#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un úmero entero positivo (numero) y un dígito (entre 0 y 9), y 
#y devuelva cuántas veces  aparece ese dígito dentro del número.
# Función recursiva que cuenta cuántas veces aparece un dígito en un número entero positivo
# numero: el número en el que buscamos el dígito
# digito: el dígito que queremos contar (de 0 a 9)
def contar_digito(numero, digito):
    # Caso base: cuando el número es 0, no quedan más dígitos que contar
    if numero == 0:
        return 0
    
    # Obtenemos el último dígito del número usando el operador módulo (%)
    ultimo_digito = numero % 10
    
    # Comparamos si el último dígito es igual al dígito que buscamos
    if ultimo_digito == digito:
        # Si son iguales, sumamos 1 y seguimos con el resto del número (dividido por 10)
        return 1 + contar_digito(numero // 10, digito)
    else:
        # Si no son iguales, no sumamos y seguimos con el resto del número
        return contar_digito(numero // 10, digito)

# Pedimos al usuario que ingrese el número entero positivo
numero_usuario = int(input("Ingrese un número entero positivo: "))

# Pedimos al usuario que ingrese el dígito que quiere contar
digito_usuario = int(input("Ingrese un dígito (entre 0 y 9) para contar en el número: "))

# Llamamos a la función contar_digito y guardamos el resultado
resultado = contar_digito(numero_usuario, digito_usuario)

# Mostramos el resultado
print(f"El dígito {digito_usuario} aparece {resultado} veces en el número {numero_usuario}.")