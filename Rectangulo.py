# =============================================
#  CLASE RECTANGULO
# =============================================

class Rectangulo:
    def __init__(self, largo: float, ancho: float):
        if largo <= 0 or ancho <= 0:
            raise ValueError("El largo y el ancho deben ser mayores que cero.")
        self.__largo = largo
        self.__ancho = ancho

    def cambiar_dimensiones(self, nuevo_largo: float, nuevo_ancho: float):
        if nuevo_largo <= 0 or nuevo_ancho <= 0:
            raise ValueError("El largo y el ancho deben ser mayores que cero.")
        self.__largo = nuevo_largo
        self.__ancho = nuevo_ancho

    def calcular_area(self) -> float:
        return self.__largo * self.__ancho

    def calcular_perimetro(self) -> float:
        return 2 * (self.__largo + self.__ancho)

    def consultar_dimensiones(self):
        return self.__largo, self.__ancho


# =============================================
#  PEDIR DIMENSIONES AL USUARIO
# =============================================

print("=" * 40)
print("     CALCULADORA DE RECTANGULOS")
print("=" * 40)

rectangulos = []
print("Ingresa tus rectangulos (escribe 'listo' para terminar)\n")

while True:
    nombre = input("Nombre del rectangulo (ej: Sala, Cuarto): ").strip()
    if nombre.lower() == "listo":
        break

    while True:
        try:
            largo = float(input(f"  Largo de '{nombre}': "))
            if largo <= 0:
                print("  El largo debe ser mayor que cero.")
            else:
                break
        except ValueError:
            print("  Escribe solo numeros. Ejemplo: 5.5")

    while True:
        try:
            ancho = float(input(f"  Ancho de '{nombre}': "))
            if ancho <= 0:
                print("  El ancho debe ser mayor que cero.")
            else:
                break
        except ValueError:
            print("  Escribe solo numeros. Ejemplo: 3.0")

    r = Rectangulo(largo, ancho)
    rectangulos.append((nombre, r))
    print(f"  '{nombre}' agregado!\n")

if not rectangulos:
    print("\nNo ingresaste ningun rectangulo. Hasta luego!")
    exit()

# =============================================
#  MOSTRAR RESULTADOS
# =============================================

print("\n" + "=" * 55)
print(f"  {'Nombre':<15} {'Largo':>7} {'Ancho':>7} {'Area':>10} {'Perimetro':>10}")
print("-" * 55)

for nombre, r in rectangulos:
    largo, ancho = r.consultar_dimensiones()
    area         = r.calcular_area()
    perimetro    = r.calcular_perimetro()
    print(f"  {nombre:<15} {largo:>7.2f} {ancho:>7.2f} {area:>10.2f} {perimetro:>10.2f}")

print("=" * 55)
print(f"  {'':15} {'m':>7} {'m':>7} {'m²':>10} {'m':>10}")
print("=" * 55)
