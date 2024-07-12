
from models.animal_exotico import AnimalExotico
from abc import ABC, abstractmethod

class Huron(AnimalExotico):
    def __init__(self, pais_origen: str, impuestos: float, nombre: str, edad: int, peso: float):
        super().__init__(pais_origen, impuestos, nombre, edad, peso)

    def hacer_sonido(self) -> str:
        return "¡Eek Eek!"

    def calcular_flete(self) -> float:
        return self._peso * 5.0  # Suponiendo un cálculo arbitrario para el flete
