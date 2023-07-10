class Vehículo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehículo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

mi_coche = Coche("Rojo", 4, 5, 120, 2000)


print("Color:", mi_coche.color)
print("Ruedas:", mi_coche.ruedas)
print("Puertas:", mi_coche.puertas)
print("Velocidad:", mi_coche.velocidad)
print("Cilindrada:", mi_coche.cilindrada)
