# =============================================
#  CLASE BASE: CuentaBancaria
# =============================================

class CuentaBancaria:
    def __init__(self, titular: str, saldo: float):
        if saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        self.__titular = titular
        self.__saldo   = saldo

    def depositar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor que cero.")
        self.__saldo += monto

    def retirar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor que cero.")
        if monto > self.__saldo:
            raise ValueError("Saldo insuficiente.")
        self.__saldo -= monto

    def consultar_saldo(self) -> float:
        return self.__saldo

    def consultar_titular(self) -> str:
        return self.__titular

    # Método protegido para que CuentaAhorro pueda modificar el saldo
    def _set_saldo(self, nuevo_saldo: float):
        self.__saldo = nuevo_saldo


# =============================================
#  CLASE HIJA: CuentaAhorro
# =============================================

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular: str, saldo: float, interes_anual: float):
        super().__init__(titular, saldo)
        if not (0 < interes_anual <= 100):
            raise ValueError("El interes anual debe estar entre 0 y 100.")
        self.__interes_anual = interes_anual

    def aplicar_interes(self):
        interes = self.consultar_saldo() * (self.__interes_anual / 100)
        self._set_saldo(self.consultar_saldo() + interes)
        return interes

    def consultar_interes(self) -> float:
        return self.__interes_anual


# =============================================
#  INGRESAR CUENTAS
# =============================================

cuentas = []

print("=" * 45)
print("      REGISTRO DE CUENTAS DE AHORRO")
print("=" * 45)
print("Escribe 'listo' para terminar\n")

while True:
    titular = input("Nombre del titular: ").strip()
    if titular.lower() == "listo":
        break

    while True:
        try:
            saldo = float(input(f"  Saldo inicial de '{titular}': $"))
            if saldo < 0:
                print("  El saldo no puede ser negativo.")
            else:
                break
        except ValueError:
            print("  Escribe solo numeros. Ejemplo: 1000.00")

    while True:
        try:
            interes = float(input(f"  Porcentaje de interes anual (%): "))
            if not (0 < interes <= 100):
                print("  El interes debe estar entre 0 y 100.")
            else:
                break
        except ValueError:
            print("  Escribe solo numeros. Ejemplo: 5.5")

    cuenta = CuentaAhorro(titular, saldo, interes)
    cuentas.append(cuenta)
    print(f"  Cuenta de '{titular}' creada!\n")

if not cuentas:
    print("\nNo ingresaste ninguna cuenta. Hasta luego!")
    exit()

# =============================================
#  MOSTRAR ESTADO INICIAL
# =============================================

print("\n" + "=" * 52)
print(f"  {'Titular':<18} {'Saldo inicial':>14} {'Interes':>8}")
print("-" * 52)

for c in cuentas:
    print(f"  {c.consultar_titular():<18} ${c.consultar_saldo():>13.2f} {c.consultar_interes():>7.1f}%")

# =============================================
#  APLICAR INTERÉS
# =============================================

print("\n" + "=" * 52)
print("       DESPUES DE APLICAR EL INTERES ANUAL")
print("=" * 52)
print(f"  {'Titular':<18} {'Interes ganado':>14} {'Saldo final':>12}")
print("-" * 52)

for c in cuentas:
    saldo_antes = c.consultar_saldo()
    ganado      = c.aplicar_interes()
    print(f"  {c.consultar_titular():<18} ${ganado:>13.2f} ${c.consultar_saldo():>11.2f}")

print("=" * 52)
