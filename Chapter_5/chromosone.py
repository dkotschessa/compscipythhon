from abc import ABC, abstractmethod
from enum import Enum
from typing import TypeVar

T = TypeVar("T", bound="Chromosome")  # for returning self


class Chromosone(ABC):
    @abstractmethod
    def fitness(self) -> float:
        ...

    @classmethod
    @abstractmethod
    def random_instance(cls) -> T:
        ...

    @abstractmethod
    def mutate(self):
        ...
