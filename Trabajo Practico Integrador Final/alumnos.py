
# Calculamos el promedio de una lista de notas
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# Cargamos los datos de los alumnos desde el teclado
def ingresar_alumnos():
    alumnos = []
    cantidad = int(input("¿Cuántos alumnos vas a ingresar?: "))

    for i in range(cantidad):
        print("\nIngresá los siguientes datos:")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        dni = input("DNI: ")
        notas = []

        for j in range(3):  # Pedimos 3 notas por alumno
            nota = float(input(f"Ingresá la nota del parcial nº {j + 1}: "))
            notas.append(nota)

        alumno = {
            "nombre": nombre,
            "apellido": apellido,
            "dni": dni,
            "notas": notas
        }
        alumnos.append(alumno)
    
    return alumnos 


# BÚSQUEDA SECUENCIAL

def buscar_alumno(clave, lista_alumnos):
    for alumno in lista_alumnos:
        if (alumno["nombre"].lower() == clave.lower() or
            alumno["apellido"].lower() == clave.lower() or
            alumno["dni"] == clave):
            return alumno
    return None


# ORDENAMIENTO BURBUJA

def ordenar_por_promedio(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if calcular_promedio(lista[j]["notas"]) < calcular_promedio(lista[j + 1]["notas"]):
                # Intercambia si el siguiente promedio es mayor
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def mostrar_alumnos_ordenados_por_promedio(alumnos):
    print("\n📋 Lista de alumnos ordenada por promedio (mayor a menor):")
    for alumno in alumnos:
        promedio = calcular_promedio(alumno["notas"])
        print(f"{alumno['apellido']}, {alumno['nombre']} - Promedio: {promedio:.2f}")

def busqueda_interactiva(alumnos):
    while True:
        print("\n🔍 Búsqueda de alumno")
        clave = input("Ingresá nombre, apellido o DNI (o escribí 'salir' para terminar): ")
        if clave.lower() == "salir":
            break

        resultado = buscar_alumno(clave, alumnos)

        if resultado:
            promedio = calcular_promedio(resultado["notas"])
            estado = "APROBADO ✅" if promedio >= 6 else "DESAPROBADO ❌"
            print(f"\n✅ Alumno encontrado:")
            print(f"Nombre: {resultado['nombre']} {resultado['apellido']}")
            print(f"DNI: {resultado['dni']}")
            print(f"Notas: {resultado['notas']}")
            print(f"Promedio: {promedio:.2f}")
            print(f"Estado: {estado}")
        else:
            print("❌ Alumno no encontrado.")
# PROGRAMA PRINCIPAL

# 1. Ingreso de datos
alumnos = ingresar_alumnos()

# 2. Ordenamiento por promedio descendente
ordenar_por_promedio(alumnos)

# 3. Mostrar alumnos ordenados
mostrar_alumnos_ordenados_por_promedio(alumnos)

# 4. Búsqueda interactiva
busqueda_interactiva(alumnos)
