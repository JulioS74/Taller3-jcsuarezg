

from models.huron import BoaConstrictor, Huron  # Importamos las clases BoaConstrictor y Huron desde el módulo models.huron

class Guarderia:
    def __init__(self):
        self.boas = [
            BoaConstrictor("Brasil", 100, "Marina", 10, 5.0),
            BoaConstrictor("Colombia", 120, "Ursula", 8, 4.5)
        ]
        self.hurones = [
            Huron("Rusia", 50, "Ruperto", 3, 1.2),
            Huron("Francia", 60, "Rumualdo", 4, 1.5)
        ]

    def alimentar_boa(self, indice: int) -> str:
        try:
            boa = self.boas[indice]
            boa.comer_raton()
            return "Éxito"
        except IndexError:
            return "Esta Boa no existe!"
        except ValueError:
            return "La boa está llena"

if __name__ == "__main__":
    guarderia = Guarderia()
    resultado = guarderia.alimentar_boa(0)
    print(resultado)
