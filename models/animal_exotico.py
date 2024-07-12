

from abc import ABC, abstractmethod
from models.animal import Animal

class AnimalExotico(Animal, ABC):
    def __init__(self, pais_origen:str, impuestos:float, nombre:str, edad:int, peso:float):
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuestos = impuestos

    def calcular_flete(self)->float:
        return self._impuestos * self._peso
    
    @abstractmethod
    def hacer_sonido(self):
        pass
