from typing import TypeVar, Generic, List
T = TypeVar('T')


class Stack(Generic[T]):

    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self: T) -> None:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


def move_disc(from_tower, to_tower):
    disc = from_tower.pop()
    to_tower.push(disc)






def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n==1:
        end.push(begin.pop())
        #move_disc(begin, end)
    else: 
        hanoi(begin, temp, end, n-1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n-1)
    





