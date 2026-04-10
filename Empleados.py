# =============================================
#  CLASE EMPLEADO
# =============================================

class Empleado:

    # Variable de clase: la comparten TODOS los empleados
    __contador = 0

    def __init__(self, nombre: str, salario: float):
        if salario < 0:
            raise ValueError("El salario no puede ser negativo.")
        self.__nombre  = nombre
        self.__salario = salario
        Empleado.__contador += 1   # Aumenta cada vez que se crea un empleado

    def consultar_nombre(self) -> str:
        return self.__nombre

    def consultar_salario(self) -> float:
        return self.__salario

    # Método de clase: pertenece a la clase, no a un objeto específico
    @classmethod
    def cantidad_empleados(cls) -> int:
        return cls.__contador


# =============================================
#  INGRESAR EMPLEADOS
# =============================================

empleados = []

print("=" * 45)
print("       REGISTRO DE EMPLEADOS")
print("=" * 45)
print("Escribe 'listo' para terminar\n")

while True:
    nombre = input("Nombre del empleado: ").strip()
    if nombre.lower() == "listo":
        break

    while True:
        try:
            salario = float(input(f"  Salario de '{nombre}': $"))
            if salario < 0:
                print("  El salario no puede ser negativo.")
            else:
                break
        except ValueError:
            print("  Escribe solo numeros. Ejemplo: 2500.00")

    emp = Empleado(nombre, salario)
    empleados.append(emp)
    print(f"  '{nombre}' registrado! Total empleados: {Empleado.cantidad_empleados()}\n")

if not empleados:
    print("\nNo ingresaste ningun empleado. Hasta luego!")
    exit()

# =============================================
#  MOSTRAR RESULTADOS
# =============================================

print("\n" + "=" * 42)
print(f"  {'#':<4} {'Nombre':<20} {'Salario':>12}")
print("-" * 42)

for i, e in enumerate(empleados, 1):
    print(f"  {i:<4} {e.consultar_nombre():<20} ${e.consultar_salario():>10.2f}")

print("-" * 42)

total_nomina = sum(e.consultar_salario() for e in empleados)
print(f"  {'Total empleados:':<25} {Empleado.cantidad_empleados():>5}")
print(f"  {'Nomina total:':<25} ${total_nomina:>10.2f}")
print("=" * 42)
