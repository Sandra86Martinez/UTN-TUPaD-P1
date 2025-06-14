# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje:

# Definimos la función solicitada con la palabra "def". Los paréntesis vacíos indican que no se requieren parámetros externos.
import math


def imprimir_hola_mundo():
    # Informamos por pantalla el mensaje que deseamos
    print("Hola Mundo")


# Realizamos la llamada a la función
imprimir_hola_mundo()

# **********************************************************************************************#

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.

# Definimos la función solicitada con la palabra "def". Dentro de los paréntesis llamaremos al valor "nombre".


def saludar_usuario(nombre):
    # Mostramos por pantalla un saludo personalizado con el nombre recibido
    print(f"Hola {nombre}")


# Solicitamos al usuario que ingrese su nombre
nombre_ingresado = input("Ingresá tu nombre: ")

# Realizamos la llamada a la función usando el nombre que ingresó el usuario
saludar_usuario(nombre_ingresado)

# **********************************************************************************************#

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Definimos la función solicitada con la palabra "def". Dentro de los paréntesis llamaremos a los valores solicitados.


def informacion_personal(nombre, apellido, edad, residencia):
    # Mostramos por pantalla un saludo personalizado con el nombre recibido
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# Solicitamos al usuario que ingrese sus datos personales
nombre_ingresado = input("Ingresá tu nombre: ")
apellido_ingresado = input("Ingresá tu apellido: ")
edad_ingresada = input("Ingresá tu edad: ")
residencia_ingresada = input("Lugar de residencia: ")

# Realizamos la llamada a la función usando los datos que ingresó el usuario
informacion_personal(nombre_ingresado, apellido_ingresado,
                     edad_ingresada, residencia_ingresada)

# ****************************************************************************************************************************#

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y
# llamar ambas funciones para mostrar los resultados.

# Importamos math para usar pi

# Definimos la función que calcula el área del círculo segun lo solicitado


def calcular_area_circulo(radio):
    # Calculamos el área usando la fórmula: π * radio^2
    area = math.pi * (radio ** 2)
    # Devolvemos el valor calculado
    return area

# Definimos la función que calcula el perímetro del círculo


def calcular_perimetro_circulo(radio):
    # Calculamos el perímetro usando la fórmula: 2 * π * radio
    perimetro = 2 * math.pi * radio
    return perimetro  # Devolvemos el valor calculado


# Solicitamos al usuario que ingrese el radio, lo convertimos a float para permitir decimales
radio_ingresado = float(input("Ingresá el radio del círculo: "))

# Llamamos a las funciones y guardamos los resultados
area_circulo = calcular_area_circulo(radio_ingresado)
perimetro_circulo = calcular_perimetro_circulo(radio_ingresado)

# Mostramos los resultados al usuario mediante dos prints
print(f"El área del círculo es: {area_circulo:.2f}")
print(f"El perímetro del círculo es: {perimetro_circulo:.2f}")

# *********************************************************************************************************************************#


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# Definimos la función que convierte segundos a horas segun lo solicitado
def segundos_a_horas(segundos):
    # Se realiza una operacion con el dato de los segundos para opbetenr las horas
    horas = segundos / 3600
    # Devolvemos la cantidad de horas
    return horas  # Devolvemos la cantidad de horas


# Solicitamos al usuario que ingrese la cantidad de segundos
segundos_ingresados = int(input("Ingresá la cantidad de segundos: "))

# Llamamos a la función con el valor ingresado y guardamos el resultado
horas_resultado = segundos_a_horas(segundos_ingresados)

# Mostramos el resultado al usuario, con dos decimales
print(f"{segundos_ingresados} segundos equivalen a {horas_resultado:.2f} horas.")

# ******************************************************************************************************************#

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10.

# Definimos la función que recibe un número como parámetro y muestra su tabla de multiplicar


def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")

    # Recorremos los números del 1 al 10 para multiplicar
    for i in range(1, 11):
        # Multiplicamos el número recibido por el valor actual de i
        resultado = numero * i
        # Imprimimos la operación y el resultado con formato claro
        print(f"{numero} x {i} = {resultado}")


# Pedimos al usuario que ingrese un número entero
numero_usuario = int(
    input("Ingresá un número para ver su tabla de multiplicar: "))

# Llamamos a la función con el número ingresado
tabla_multiplicar(numero_usuario)

# *****************************************************************************************************************#
# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.
# Mostrar los resultados de forma clara.


# Definimos la función que recibe dos números y devuelve una tupla con las 4 operaciones básicas (Una tupla es una colección ordenada e inmutable de elementos.)
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    # Para la división, chequeamos que b no sea cero para evitar error
    if b != 0:
        division = a / b
    else:
        division = "Incorrecto"
    # Devolvemos los resultados en una tupla
    return (suma, resta, multiplicacion, division)


# Pedimos al usuario que ingrese dos números
num1 = float(input("Ingresá el primer número: "))
num2 = float(input("Ingresá el segundo número: "))

# Llamamos a la función con los números ingresados
resultados = operaciones_basicas(num1, num2)

# Mostramos los resultados de forma clara
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
if resultados[3] is not "Incorrecto":
    print(f"División: {resultados[3]:.2f}")
else:
    print("División: No se puede dividir por cero.")

# **************************************************************************************************************************************#

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.


# Definimos la función con la palabra "def". Dentro de los paréntesis ponemos los parámetros peso y altura.
def calcular_imc(peso, altura):
    # Calculamos el IMC aplicando la fórmula: peso dividido por la altura al cuadrado.
    imc = peso / (altura ** 2)
    # Devolvemos el valor calculado para poder usarlo fuera de la función.
    return imc


# Pedimos al usuario que ingrese su peso y convertimos el dato a float para permitir decimales.
peso_usuario = float(input("Ingrese su peso en kilogramos: "))

# Pedimos al usuario que ingrese su altura en metros, también convertido a float.
altura_usuario = float(input("Ingrese su altura en metros: "))

# Llamamos a la función calcular_imc con los datos ingresados y guardamos el resultado en una variable.
imc_resultado = calcular_imc(peso_usuario, altura_usuario)

# Mostramos el resultado formateado con dos decimales para que sea más legible.
print(f"Su índice de masa corporal (IMC) es: {imc_resultado:.2f}")

# ***********************************************************************************************************************************#

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# Definimos la función que convierte grados Celsius a Fahrenheit


def celsius_a_fahrenheit(celsius):
    # Aplicamos la fórmula para convertir: (Celsius * 9/5) + 32
    fahrenheit = (celsius * 9 / 5) + 32
    # Devolvemos el resultado para poder usarlo fuera de la función
    return fahrenheit


# Pedimos al usuario que ingrese la temperatura en grados Celsius
temperatura_celsius = float(
    input("Ingresá la temperatura en grados Celsius: "))

# Llamamos a la función con el valor ingresado y guardamos el resultado
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)

# Mostramos el resultado con dos decimales para que quede claro y prolijo
print(f"{temperatura_celsius}°C equivalen a {temperatura_fahrenheit:.2f}°F")

# *********************************************************************************************************************************************#
# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.


# Definimos la función que recibe tres números y calcula su promedio
def calcular_promedio(a, b, c):
    # Sumamos los tres números y dividimos por 3 para obtener el promedio
    promedio = (a + b + c) / 3
    # Devolvemos el promedio calculado
    return promedio


# Solicitamos al usuario que ingrese tres números, convirtiéndolos a float para permitir decimales
num1 = float(input("Ingresá el primer número: "))
num2 = float(input("Ingresá el segundo número: "))
num3 = float(input("Ingresá el tercer número: "))

# Llamamos a la función con los valores ingresados y guardamos el resultado
resultado_promedio = calcular_promedio(num1, num2, num3)

# Mostramos el promedio al usuario con dos decimales
print(f"El promedio de los números ingresados es: {resultado_promedio:.2f}")
