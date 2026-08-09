from abc import ABC, abstractmethod

class Comando(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def ejecutar(self):
        pass

class ComandoSaludo(Comando):
    def ejecutar(self):
        print(f"¡Hola! Soy {self.nombre}")

class ComandoHora(Comando):
    def ejecutar(self):
        import datetime
        ahora = datetime.datetime.now().strftime("%H:%M")
        print(f"Son las {ahora}")
class ComandoDespedida(Comando):
    def ejecutar(self):
        print("Adios señor")

comandos = [ComandoSaludo("Jarvis"), ComandoHora("hora"), ComandoDespedida("despedida")]

for c in (comandos):
    c.ejecutar()

comando_generico = Comando("test")