
from statistics import mode, median, mean
import random

# Ejercicio 1
# Solicito al usuario que ingrese su edad por medio de un mensaje y guardo ese valor en la variable "edad"
edad = int(input("Ingrese su edad: "))
# Por medio del uso de la estructura if-else se decidirá si cumple la condición establecida devolviendo un mensaje según corresponda
if edad >= 18:
    # Al cumplir con la edad mínima, se devuelve un mensaje afirmando que es mayor de edad
    print("Es mayor de edad")
else:
    # Al NO cumplir con la edad mínima, se devuelve un mensaje informando que no cumple la mayoría de edad
    print("No es mayor de edad")

# Ejercicio 2
# Solicito al usuario que ingrese una nota númerica por medio de un mensaje y guardo ese valor en la variable "nota"
nota = int(input("Ingrese su nota"))
# Por medio del uso de la estructura if-else se decidirá si cumple la condición establecida devolviendo un mensaje según corresponda
if nota >= 6:
    # Si la nota ingresada es mayor igual a 6,  devuelve un mensaje de "Aprobado"
    print("Aprobado")
# Si la nota ingresada es menor a 6,  devuelve un mensaje de "Desaprobado"
else:
    print("Desaprobado")


# Ejercicio 3
# Solicito al usuario que ingrese un numero por medio de un mensaje y guardo ese valor en la variable "numero"
numero = int(input("Ingrese un numero: "))
# Uso la estructura if-else para verificar si el número es par,utilizando el operador módulo (%) que nos devuelve el residuo
# de la división
if numero % 2 == 0:
    # Si el residuo de dividir el número por 2 es "0", el número es par y lo informamos en un mensaje
    print("Ha ingresado un numero par")
else:
    # Por el contrario, si el residuo de dividir el número por 2 es diferente a "0", el número es impar y lo informamos en un mensaje
    print("Por favor, ingrese un  número par")


# Ejercicio 4
# Solicito al usuario que ingrese su edad por medio de un mensaje y guardo ese valor en la variable "edad"
edad = int(input("Ingrese su edad: "))
# Utilizando la estructura if-elif-else se decidirá a cuál categoría etárea corresponde. Con esta estructura comenzamos el código
# con if luego pasa por la condiciones elif y por ultimo si no cumplió con las anteriores, devuelve el resultado del else
if edad < 12:
    # Si la edad es menor que 12, se define como "Niño/a"
    print("Niño/a")
elif edad >= 12 and edad < 18:
    # Si la edad es mayor o igual que 12 y menor que 18, se define como "Adolescente"
    print("Adolescente")
elif edad >= 18 and edad < 30:
    # Si la edad es mayor o igual que 18 y menor que 30, se define como "Adulto/a joven"
    print("Adulto/a joven")
# De lo contrario, se establece que la persona es "Adulto/a"
else:
    print("Adulto/a")


# Ejercicio 5
# Se pide al usuario que ingrese una contraseña por medio de un mensaje y guardo ese valor en la variable "password"
password = input("Ingrese su contraseña: ")
# Con la función len() obtengo la cantidad de caracteres que tiene la contraseña ingresada
# Por medio del uso de la estructura if-else se decidirá si cumple la condición establecida devolviendo un mensaje según corresponda
if 8 <= len(password) <= 14:
    # Si la contraseña ingresada contiene entre 8 y 14 caracteres inclusive, se establece que la contraseña es correcta
    print("Ha ingresado una contraseña correcta")
else:
    # De lo contrario, se solicita ingresar una contraseña que cumpla con los requisitos
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# Ejercicio 6
# Para calcular la moda, mediana y media, primero hay que exportar el paquete "statistics". Esta función lo que hace es tomar una lista
# de numeros calculando parámetros estádisticos para predecir la forma de una distribución normal con ciertos criterios
# Para generar numeros aleatorios, importo le modulo: random

# Con la función "random.randint()" genero un número entero aleatorio entre 1 y 100.
# Luego, mediante un bucle for que se repite 50 veces, genero una lista con 50 valores distintos.
# La variable "i" actúa como contador del bucle, permitiendo que se repita la acción varias veces.
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculo la moda (valor que más se repite en la lista)
moda = mode(numeros_aleatorios)
# Calculo la mediana (valores que quedan en el medio cuando ya obtengo el orden de los números)
mediana = median(numeros_aleatorios)
# Calculo la moda (promedio de todos los números de la lista)
media = mean(numeros_aleatorios)

# Imprimo en pantalla la lista de números generados y los resultados de los tres cálculos: moda, mediana y media
print(f"Lista de números analizados: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

# Uso las estructuras if, elif y else para comparar la media, mediana y moda, y así determinar el tipo de sesgo de la distribución
if media > mediana > moda:
    # Si la media es mayor que la mediana, y esta a su vez mayor que la moda, el sesgo es positivo
    print("Sesgo positivo")
elif media < mediana < moda:
    # Si la media es menor que la mediana, y esta a su vez menor que la moda, el sesgo es negativo
    print("Sesgo negativo")
else:
    # El no cumplimiento de las relaciones anterior indica que no hay sesgo
    print("No hay sesgo")


# Ejecicio 7
# Por medio de un input, le solicito al usuario que ingrese una frase o palabra para guardarla en la variable "dato"
dato = input("Ingrese una frase o palabra: ")
# Con la estructura if-else comenzamos a analizar las condiciones.
# Para ello verificamos si la ultima letra de la cadena es una vocal. Tambien usamos la función ".lower()" para convertir en
# minúscula la ultima letra ingresada si es que el usuario coloca una vocal mayúscula.
if dato[-1].lower() in 'aeiou':
    # Si la última letra es una vocal, agregamos un signo de exclamación al final de la cadena.
    dato += "!"
# Por pantalla mostramos un mensaje con la frase o palabra ingresada con el agregado de dicho signo
    print(dato)
else:
    # Caso contrario, devuelve por pantalla la frase o palabra tal cual se ingresó
    print(dato)


# Ejercicio 8
# Solicito al usuario que ingrese su nombre y guardo el valor en la variable "nombre"
nombre = input("Ingrese su nombre: ")
# Luego, le pido que ingrese una opción para la acción que desea realizar con el nombre
opcion = input(
    "Ingrese una opción (1 = mayúsculas, 2 = minúsculas, 3 = primera letra mayúscula): ")
# Utilizando la estructura if-elif-else se decidirá la acción a realizarse según la opción elegida por el usuario
if opcion == "1":
    # Si la opción es 1, la función ".upper()" convierte el nombre a mayúsculas
    print(nombre.upper())
# Si la opción es 2, la función ".lower()" convierte el nombre a minúsculas
elif opcion == "2":
    print(nombre.lower())
# Si la opción es 3, la función ".title()" convierte la primera letra de cada palabra en mayúsculas, dejando el resto en minúsculas
elif opcion == "3":
    print(nombre.title())
else:
    # Si ingresa una opción no valida como un número, muestra un mensaje de error
    print("Opción inválida")


# Ejercicio 9
# Se le pide al usuario que ingrese un valor de escala para evaluar la magnitud del terremoto, y ese valor se guarda en la variable
# "magnitud"
magnitud = float(input("Ingrese un valor: "))
# Utilizando la estructura if-elif-else se decidirá qué magnitud condice con el valor
if magnitud < 3:
    # Si el valor ingresado es menor a 3, se muestra un mensaje que informa que es "Muy leve"
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    # Si el valor ingresado es mayor o igual a 3 y menor a 4, se muestra un mensaje que informa que es "Leve"
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    # Si el valor ingresado es mayor o igual a 4 y menor a 5, se muestra un mensaje que informa que es "Moderado"
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    # Si el valor ingresado es mayor o igual a 5 y menor a 6, se muestra un mensaje que informa que es "Fuerte"
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    # Si el valor ingresado es mayor o igual a 6 y menor a 7, se muestra un mensaje que informa que es "Muy Fuerte"
    print("Muy Fuerte (puede causar daños significativos)")
else:
    # Si el valor es diferente al resto de las escalas, entonces se muestra un mensaje que informa al terremoto como "Extremo"
    print("Extremo (puede causar graves daños a gran escala)")


# Ejercicio 10
# Se comienza el código solicitando al ususario tres datos: en cuál hemisferio se encuentr y el mes y el día actual.
# Luego, cada valor ingresado se guarda en las variables: "hemisferio", "mes" y "dia".
# Se utiliza la opción ".lower()" para convertir la letra que ingrese en minúsculas evitando errores si ingresa mayúsculas
hemisferio = input("¿En qué hemisferio te encuentras N/S?: ").lower()
mes = input("¿Qué mes es?: ").lower()
dia = int(input("¿Qué día es?: "))
# Utilizando la estructura if-elif-else, analizamos los datos ingresados para determinar la estación del año correspondiente.
# Las fechas utilizadas para determinar las estaciones del año fueron tomadas del trabajo práctico provisto
if hemisferio == 'n':
    # Para asignar la estación, usamos "==" para comparar el mes, y operadores relacionales (>= y <=) para verificar el rango de días.
    if mes == 'diciembre' and dia >= 21 or mes == 'enero' or mes == 'febrero' or mes == 'marzo' and dia <= 20:
        estacion = 'Invierno'
    elif mes == 'marzo' and dia >= 21 or mes == 'abril' or mes == 'mayo' or mes == 'junio' and dia <= 20:
        estacion = 'Primavera'
    elif mes == 'junio' and dia >= 21 or mes == 'julio' or mes == 'agosto' or mes == 'septiembre' and dia <= 20:
        estacion = 'Verano'
    else:
        estacion = 'Otoño'

elif hemisferio == 's':
    # Para asignar la estación, usamos "==" para comparar el mes, y operadores relacionales (>= y <=) para verificar el rango de días.
    if mes == 'diciembre' and dia >= 21 or mes == 'enero' or mes == 'febrero' or mes == 'marzo' and dia <= 20:
        estacion = 'Verano'
    elif mes == 'marzo' and dia >= 21 or mes == 'abril' or mes == 'mayo' or mes == 'junio' and dia <= 20:
        estacion = 'Otoño'
    elif mes == 'junio' and dia >= 21 or mes == 'julio' or mes == 'agosto' or mes == 'septiembre' and dia <= 20:
        estacion = 'Invierno'
    else:
        estacion = 'Primavera'
else:
    # Si el hemisferio no es 'n' ni 's', el hemisferio es inválido.
    estacion = 'Hemisferio inválido'
# Al final del código, se muestra el mensaje que informa en qué estacion del año se encuentra
print(f"La estación es: {estacion}")
