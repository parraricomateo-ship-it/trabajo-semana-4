# =============================================
#  CLASE TARJETA DE CREDITO
# =============================================

class TarjetaCredito:

    def __init__(self, numero: str):
        # Guardamos solo los digitos, sin espacios ni guiones
        self.__numero = numero.replace(" ", "").replace("-", "")

    def consultar_numero(self) -> str:
        # Mostrar con formato: **** **** **** 1234
        n = self.__numero
        oculto = "*" * (len(n) - 4) + n[-4:]
        return " ".join(oculto[i:i+4] for i in range(0, len(oculto), 4))

    def es_valida(self) -> bool:
        return TarjetaCredito.validar_tarjeta(self.__numero)

    # -----------------------------------------------
    #  METODO ESTATICO: Algoritmo de Luhn
    # -----------------------------------------------
    @staticmethod
    def validar_tarjeta(numero: str) -> bool:
        """
        Algoritmo de Luhn:
        1. Partir del ultimo digito hacia la izquierda.
        2. Duplicar cada segundo digito (posiciones pares desde la derecha).
        3. Si el resultado de duplicar es >= 10, restar 9.
        4. Sumar todos los digitos.
        5. Si la suma es divisible entre 10 → tarjeta valida.
        """
        digitos = numero.replace(" ", "").replace("-", "")

        if not digitos.isdigit():
            return False

        total = 0
        invertido = digitos[::-1]   # Recorrer de derecha a izquierda

        for i, d in enumerate(invertido):
            n = int(d)
            if i % 2 == 1:          # Posiciones pares desde la derecha (0-indexado)
                n *= 2
                if n >= 10:
                    n -= 9
            total += n

        return total % 10 == 0


# =============================================
#  PROGRAMA INTERACTIVO
# =============================================

print("=" * 48)
print("     VALIDADOR DE TARJETAS DE CREDITO")
print("=" * 48)
print("Puedes ingresar el numero con o sin espacios.")
print("Escribe 'salir' para terminar.\n")

while True:
    entrada = input("Numero de tarjeta: ").strip()
    if entrada.lower() == "salir":
        break

    solo_digitos = entrada.replace(" ", "").replace("-", "")

    if not solo_digitos.isdigit():
        print("  Solo se permiten numeros, espacios o guiones.\n")
        continue

    if len(solo_digitos) < 13 or len(solo_digitos) > 19:
        print("  Una tarjeta debe tener entre 13 y 19 digitos.\n")
        continue

    tarjeta = TarjetaCredito(entrada)

    print(f"  Numero:    {tarjeta.consultar_numero()}")

    if tarjeta.es_valida():
        print("  Resultado: VALIDA\n")
    else:
        print("  Resultado: NO VALIDA\n")

print("\nHasta luego!")
