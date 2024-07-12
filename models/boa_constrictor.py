
from models.animal_exotico import AnimalExotico
from abc import ABC, abstractmethod

class BoaConstrictor(AnimalExotico):
    def __init__(self, pais_origen: str, impuestos: float, nombre: str, edad: int, peso: float):
        super().__init__(pais_origen, impuestos, nombre, edad, peso)
        self.__ratones_comidos = 0

    def hacer_sonido(self) -> str:
        return "¡Tsss!"

    def calcular_flete(self) -> float:
        return self._peso * 10  # Suponiendo un cálculo arbitrario para el flete

    def comer_raton(self) -> None:
        if self.__ratones_comidos < 10:
            self.__ratones_comidos += 1
        else:
            raise ValueError("¡Demasiados Ratones!")

    def dar_ratones_comidos(self) -> int:
        return self.__ratones_comidos

## Este ese le taller N 3