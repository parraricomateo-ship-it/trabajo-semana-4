class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

rect = Rectangulo(5, 3)
print("Área:", rect.calcular_area())
