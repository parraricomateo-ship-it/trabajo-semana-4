# =============================================
#  CLASE LIBRO
# =============================================

class Libro:
    def __init__(self, titulo: str, autor: str, num_paginas: int):
        self.__titulo      = titulo
        self.__autor       = autor
        self.__num_paginas = num_paginas
        self.__pagina_actual = 1

    def avanzar_paginas(self, cantidad: int):
        nueva_pagina = self.__pagina_actual + cantidad
        if nueva_pagina > self.__num_paginas:
            raise ValueError(
                f"No puedes pasar de la pagina {self.__num_paginas}. "
                f"Actualmente estas en la pagina {self.__pagina_actual}."
            )
        self.__pagina_actual = nueva_pagina

    def retroceder_paginas(self, cantidad: int):
        nueva_pagina = self.__pagina_actual - cantidad
        if nueva_pagina < 1:
            raise ValueError(
                f"No puedes retroceder mas alla de la pagina 1. "
                f"Actualmente estas en la pagina {self.__pagina_actual}."
            )
        self.__pagina_actual = nueva_pagina

    def consultar_pagina_actual(self) -> int:
        return self.__pagina_actual

    def consultar_autor(self) -> str:
        return self.__autor

    def obtener_info(self) -> str:
        return (
            f"Titulo:        {self.__titulo}\n"
            f"Autor:         {self.__autor}\n"
            f"Paginas:       {self.__num_paginas}\n"
            f"Pagina actual: {self.__pagina_actual}"
        )


# =============================================
#  INGRESAR LIBROS
# =============================================

libros = []

print("=" * 45)
print("        BIBLIOTECA PERSONAL")
print("=" * 45)
print("Escribe 'listo' para terminar\n")

while True:
    titulo = input("Titulo del libro: ").strip()
    if titulo.lower() == "listo":
        break

    autor = input(f"  Autor de '{titulo}': ").strip()

    while True:
        try:
            paginas = int(input(f"  Numero de paginas: "))
            if paginas <= 0:
                print("  Debe tener al menos 1 pagina.")
            else:
                break
        except ValueError:
            print("  Escribe un numero entero. Ejemplo: 300")

    libro = Libro(titulo, autor, paginas)
    libros.append(libro)
    print(f"  '{titulo}' agregado!\n")

if not libros:
    print("\nNo ingresaste ningun libro. Hasta luego!")
    exit()

# =============================================
#  SIMULAR LECTURA
# =============================================

print("\n" + "=" * 45)
print("          SIMULAR LECTURA")
print("=" * 45)

for libro in libros:
    print(f"\n--- {libro.consultar_autor()} ---")
    print(libro.obtener_info())
    print()

    while True:
        print(f"  Pagina actual: {libro.consultar_pagina_actual()}")
        print("  [a] Avanzar paginas")
        print("  [r] Retroceder paginas")
        print("  [s] Saltar al siguiente libro")
        opcion = input("  Elige una opcion: ").strip().lower()

        if opcion == "s":
            break
        elif opcion == "a":
            try:
                cant = int(input("  Cuantas paginas avanzar: "))
                libro.avanzar_paginas(cant)
                print(f"  Ahora estas en la pagina {libro.consultar_pagina_actual()}.")
            except ValueError as e:
                print(f"  Error: {e}")
        elif opcion == "r":
            try:
                cant = int(input("  Cuantas paginas retroceder: "))
                libro.retroceder_paginas(cant)
                print(f"  Ahora estas en la pagina {libro.consultar_pagina_actual()}.")
            except ValueError as e:
                print(f"  Error: {e}")
        else:
            print("  Opcion no valida.")
        print()

# =============================================
#  RESUMEN FINAL
# =============================================

print("\n" + "=" * 45)
print("          RESUMEN FINAL")
print("=" * 45)

for libro in libros:
    print()
    print(libro.obtener_info())

print("\n" + "=" * 45)
