# =============================================
#  CLASE ESTUDIANTE
# =============================================

class Estudiante:
    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre
        self.__edad   = edad
        self.__notas  = []

    def agregar_nota(self, nota: float):
        if not (0 <= nota <= 100):
            raise ValueError("La nota debe estar entre 0 y 100.")
        self.__notas.append(nota)

    def calcular_promedio(self) -> float:
        if not self.__notas:
            return 0.0
        return sum(self.__notas) / len(self.__notas)

    def consultar_nombre(self) -> str:
        return self.__nombre

    def consultar_edad(self) -> int:
        return self.__edad


# =============================================
#  INGRESAR ESTUDIANTES Y NOTAS
# =============================================

estudiantes = []

print("=" * 45)
print("       REGISTRO DE ESTUDIANTES")
print("=" * 45)
print("Escribe 'listo' para terminar\n")

while True:
    nombre = input("Nombre del estudiante: ").strip()
    if nombre.lower() == "listo":
        break

    while True:
        try:
            edad = int(input(f"  Edad de '{nombre}': "))
            if edad <= 0:
                print("  La edad debe ser mayor que cero.")
            else:
                break
        except ValueError:
            print("  Escribe un numero entero. Ejemplo: 18")

    e = Estudiante(nombre, edad)

    print(f"  Ingresa las notas de '{nombre}' (escribe 'listo' para terminar):")
    while True:
        entrada = input("    Nota: ").strip()
        if entrada.lower() == "listo":
            break
        try:
            nota = float(entrada)
            e.agregar_nota(nota)
            print(f"    Nota {nota} agregada!")
        except ValueError:
            print("    La nota debe estar entre 0 y 100.")

    estudiantes.append(e)
    print(f"  '{nombre}' registrado!\n")

if not estudiantes:
    print("\nNo ingresaste ningun estudiante. Hasta luego!")
    exit()

# =============================================
#  MOSTRAR RESULTADOS
# =============================================

print("\n" + "=" * 50)
print(f"  {'Nombre':<18} {'Edad':>5} {'Promedio':>10} {'Estado':>12}")
print("-" * 50)

for e in estudiantes:
    promedio = e.calcular_promedio()
    if promedio >= 90:
        estado = "Excelente"
    elif promedio >= 70:
        estado = "Aprobado"
    elif promedio >= 60:
        estado = "Regular"
    else:
        estado = "Reprobado"

    print(f"  {e.consultar_nombre():<18} {e.consultar_edad():>5} {promedio:>10.2f} {estado:>12}")

print("=" * 50)
