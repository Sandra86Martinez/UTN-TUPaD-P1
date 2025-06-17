#1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

# El primer paso es definir el diccionario llamado precios_frutas con la info descripta en la consigna
precios_frutas = {
    "Banana": 1200, 
    "Ananá": 2500,
    "Melón": 3000, 
    "Uva": 1450
    }
#A continuación, añadimos las frutas que nos piden en el trabajo
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# Imprimimos por pantalla el resultado final de la lista modificada
print(precios_frutas)

#**************************************************************************************************************************#

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

# Definimos el diccionario inicial con los datos propuestos
precios_frutas = {
    "Banana": 1200,
    "Ananá": 2500,
    "Melón": 3000,
    "Uva": 1450
}

# Añadimos las frutas nuevas con sus respectivos precios
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# Actualizamos los precios de algunas frutas según la consigna
# Cambiamos el precio de Banana a 1330
precios_frutas["Banana"] = 1330 
# Cambiamos el precio de Manzana a 1700   
precios_frutas["Manzana"] = 1700
# Cambiamos el precio de Melón a 2800 
precios_frutas["Melón"] = 2800     

# Imprimimos el diccionario final para ver todos los cambios reflejados
print(precios_frutas)

#************************************************************************************************************************#

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el códigodesarrollado en el punto anterior, 
# crear una lista que contenga únicamente las frutas sin los precios.



# Partimos del diccionario precios_frutas del punto anterior con todas las modificaciones
precios_frutas = {
    "Banana": 1330,
    "Ananá": 2500,
    "Melón": 2800,
    "Uva": 1450,
    "Naranja": 1200,
    "Manzana": 1700,
    "Pera": 2300
}

# Armamos una lista con solo las frutas (las "llaves" del diccionario)
lista_frutas = list(precios_frutas.keys())

# Imprimimos la lista de frutas con un mensaje descriptivo
print("Frutas de la lista:", lista_frutas)

#*****************************************************************************************************************************#

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe


# Creamos un diccionario vacío para guardar los contactos
contactos = {}

# Le solicitamos al usuario que ingrese 5 contactos (nombre y número).
# Usamos la función range(5) que genera una secuencia de números del 0 al 4,#
# para repetir la acción 5 veces.
for i in range(5):
    # Usamos i+1 para mostrar en el mensaje que es el contacto 1, 2, ..., 5
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input("Ingrese el número de teléfono: ")
    # Guardamos el nombre y número en el diccionario
    contactos[nombre] = numero

# Pedimos el nombre del contacto que quiere consultar el usuario mediante un mensaje por pantalla
nombre_consulta = input("Ingrese el nombre del contacto para consultar su número: ")

# Revisamos si el nombre está en el diccionario con un condicional 
if nombre_consulta in contactos:
    # Si está, mostramos el número asociado
    print(f"El número de {nombre_consulta} es: {contactos[nombre_consulta]}")
else:
    # Si no está, avisamos que no se encontró el contacto
    print(f"El nombre {nombre_consulta} no se encuentra en la base de datos.")
    
    #*****************************************************************************************************#

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra




# Solicitamos al usuario que ingrese una frase
frase = input("Ingresá una frase: ")

# Separamos la frase en palabras usando split, que divide la frase en partes usando espacios como separador
palabras = frase.split()

# Creamos un set con las palabras para obtener las únicas,
# ya que el set elimina automáticamente los elementos repetidos
palabras_unicas = set(palabras)

# Creamos un diccionario vacío para contar la cantidad de veces que aparece cada palabra
recuento = {}

# Recorremos cada palabra en la lista original con la funcion "for"
for palabra in palabras:
    # Si la palabra ya está en el diccionario, sumamos 1 a su contador
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        # Si no está, la agregamos con valor 1
        recuento[palabra] = 1

# Imprimimos el set de palabras únicas
print("Palabras únicas:", palabras_unicas)

# Imprimimos el diccionario con el recuento de palabras
print("Recuento:", recuento)

#*********************************************************************************************************************#

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.Luego, mostrá el promedio de cada alumno.

# Creamos un diccionario vacío para guardar los datos de alumnos y notas
alumnos = {}

# Solicitamos al usuario ingresar los datos de 3 alumnos. Por uso usé un range, para limitar el ingreso de datos
for i in range(3):
    # Ingrese el nombre del alumno i+1 para que se vea de 1 a 3 en el mensaje
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    
    # Ingrese las 3 notas que pide la consigna
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))
    
    # Creamos una tupla con las 3 notas, que es una estructura inmutable para agrupar datos
    notas = (nota1, nota2, nota3)
    
    # Guardamos el nombre y la tupla de notas en el diccionario "alumnos"
    alumnos[nombre] = notas

# Recorremos el diccionar"io "alumnos" con otro for,
# donde "nombre" y "notas" son cada clave y valor del diccionario respectivamente
for nombre, notas in alumnos.items():
    # Calculamos el promedio con la función sum (suma todos los elementos de la tupla)
    # y len que cuenta cuántos elementos tiene la tupla
    promedio = sum(notas) / len(notas)  
    
    # Imprimimos el resultado con un mensaje claro, mostrando el promedio con 2 decimales
    print(f"El promedio de {nombre} es: {promedio:.2f}")
    
#*****************************************************************************************************************#

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).



# Definimos dos sets con números de estudiantes que aprobaron el Parcial 1 y el Parcial 2
parcial1 = {7, 8, 9, 3, 2}
parcial2 = {10, 9, 7, 6, 5} 

# Estudiantes que aprobaron ambos parciales (intersección)
# intersection() devuelve los elementos que están en ambos sets
ambos = parcial1.intersection(parcial2)

# Estudiantes que aprobaron solo uno de los dos parciales (diferencia simétrica)
# symmetric_difference() devuelve los elementos que están en uno u otro set, pero no en ambos
solo_uno = parcial1.symmetric_difference(parcial2)

# Lista total de estudiantes que aprobaron al menos un parcial (unión)
# union() devuelve todos los elementos de ambos sets, sin repeticiones
todos = parcial1.union(parcial2)

# Imprimimos los resultados con mensajes claros
print("Estudiantes que aprobaron ambos parciales:", ambos)
print("Estudiantes que aprobaron solo uno de los parciales:", solo_uno)
print("Estudiantes que aprobaron al menos un parcial:", todos)

#***************************************************************************************************************************#

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.



# Diccionario inicial con productos y su stock
stock = {
    "Banana": 1330,
    "Ananá": 2500,
    "Melón": 2800,
    "Uva": 1450,
    "Naranja": 1200,
    "Manzana": 1700,
    "Pera": 2300
}

# Solicitamos al usuario que ingrese el nombre del producto para consultar o modificar
producto = input("Por favor, ingrese el nombre del producto: ")

# Verificamos si el producto ya se encuentra en el diccionario
if producto in stock:
    # Si existe, mostramos el stock actual
    print(f"El stock actual de {producto} es: {stock[producto]}")
    # Consultamos si desea agregar unidades al stock
    agregar = input("¿Desea agregar unidades a este producto? (s/n): ")
    if agregar == "s" or agregar == "S":
        # Solicitamos la cantidad a agregar (convertimos a entero)
        cantidad = int(input("Por favor, ingrese la cantidad a agregar: "))
        # Sumamos la cantidad al stock actual
        stock[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock[producto]}")
    else:
        print("No se modificó el stock.")
else:
    # Si no existe, informamos y consultamos si desea agregarlo
    print(f"El producto {producto} no se encuentra en el stock.")
    crear = input("¿Desea agregar este producto? (s/n): ")
    if crear == "s" or crear == "S":
        # Solicitamos la cantidad inicial para el nuevo producto
        cantidad = int(input("Por favor, ingrese la cantidad inicial: "))
        # Creamos la nueva entrada en el diccionario
        stock[producto] = cantidad
        print(f"Producto {producto} agregado con stock {cantidad}.")
    else:
        print("No se agregó el producto.")

# Finalmente, mostramos el diccionario actualizado
print("\nStock final actualizado:")
print(stock)

#*******************************************************************************************************************************#

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.

# Creamos la agenda como un diccionario.
# Cada clave es una tupla con (día, hora) y el valor es la actividad que hay en ese momento.
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:30"): "Consulta médica",
    ("viernes", "18:00"): "Gimnasio"
}

# Solicitamos al usuario que ingrese el día y la hora que desea consultar lo mas puntual posible para evitar errores
dia = input("Ingrese el día que desea consultar (en minúscula, por ejemplo \"lunes\"): ")
hora = input("Ingrese la hora en formato HH:MM (por ejemplo \"10:00\"): ")

# "Creamos la tupla con los datos ingresados por el usuario"
consulta = (dia, hora)

# "Verificamos si existe esa combinación en la agenda"
if consulta in agenda:
    # "Si existe, mostramos la actividad correspondiente"
    print(f"Actividad programada: {agenda[consulta]}")
else:
    # "Si no existe, informamos que no hay actividad registrada"
    print("No hay ninguna actividad registrada para ese día y hora.")


#*************************************************************************************************************#
#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

# Creamos el diccionario original donde las claves son países y los valores sus capitales
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "España": "Madrid",
    "Italia": "Roma"
}

# Creamos un nuevo diccionario vacío donde guardaremos los datos invertidos
invertido = {}

# Recorremos el diccionario original con un for que nos da cada país y su capital
# En cada vuelta, tomamos el país como clave y la capital como valor
for pais, capital in original.items():
    # En el nuevo diccionario, guardamos la capital como clave y el país como valor
    invertido[capital] = pais

# Mostramos el diccionario invertido por pantalla
print("Diccionario invertido:", invertido)