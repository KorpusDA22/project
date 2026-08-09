from abc import ABC, abstractmethod

class Interprete(ABC):
    @abstractmethod
    def interpretar(seld, texto):
        """Recibe el texto del usuario y devuelve el comando ejecutar"""
        pass
class InterpreteKeywords(Interprete):
    def __init__(self, comandos):
        self.comandos = comandos

    def interpretar(self, texto):
        texto = texto.lower()
        for palabra_clave, comando in self.comandos.items():
            if palabra_clave in texto:
                return comando
        return None
class Comando:
    def __init__(self, nombre):
        self.nombre = nombre

    def ejecutar(self):
        print(f"Ejecutando comando genérico: {self.nombre}")


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

comandos = {
    "hora": ComandoHora("hora"),
    "hola": ComandoSaludo("Jarvis"),
    "adios": ComandoDespedida("despedida")
}

Interprete = InterpreteKeywords(comandos)

while True:
    texto = input("Tu: ")
    comando = Interprete.interpretar(texto)
    if texto.lower() in ("salir", "exit"):
        print("Hasta luego señor")
        break
    if comando:
        comando.ejecutar()
    else:
        print("No entendí ese comando")
