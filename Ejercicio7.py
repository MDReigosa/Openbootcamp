class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def mostrar_resultado(self):
        if self.nota >= 5:
            print("Has aprobado")
        else:
            print("No has aprobado.")



alumno1 = Alumno("Juan", 7.8)


alumno1.imprimir_informacion()


alumno1.mostrar_resultado()