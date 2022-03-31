from __future__ import annotations
from abc import ABC, abstractmethod
from typing import NewType, List


Move = NewType("Move", int)


class Piece:
    @property
    def opposite(self) -> Piece:
        raise NotImplementedError("Should be implementedby subclasses")


class Board(ABC):
    @property
    @abstractmethod
    def turn(self) -> Piece:
        ...

    @abstractmethod
    def move(self, location) -> Board:
        ...

    @property
    @abstractmethod
    def legal_moves(self) -> List[Move]:
        ...

    @property
    @abstractmethod
    def is_win(self) -> bool:
        ...

    @property
    def is_draw(self) -> bool:
        return (not self.is_win) and (len(self.legal_moves) == 0)

    @abstractmethod
    def evaluate(self, player) -> float:
        ...
