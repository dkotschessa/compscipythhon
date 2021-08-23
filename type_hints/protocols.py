# https://mypy.readthedocs.io/en/latest/protocols.html#predefined-protocols


# The typing module defines various protocol classes that
#  correspond to common Python protocols, such as Iterable[T].
#   If a class defines a suitable __iter__ method, mypy understands 
#   that it implements the iterable protocol and is compatible with
#    Iterable[T]. For example, 
# IntList below is iterable, over int values:

from typing import Iterator, Iterable, Optional

class IntList:
    def __init__(self, value: int, next: Optional['IntList']) -> None:
        self.value = value
        self.next = next

    def __iter__(self) -> Iterator[int]:
        current = self
        while current:
            yield current.value
            current = current.next


def print_numbered(items: Iterable[int]) -> None:
    for n, x in enumerate(items):
        print(n+1, x)

x = IntList(3, IntList(5, None))
print_numbered(x)    #ok
print_numbered([4,5])  #also ok

## write without type hints to see if I understand better

class IntList:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __iter__(self):
        current = self
        while current:
            yield current.value
            current = current.next
            