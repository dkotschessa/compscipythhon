from dataclasses import dataclass
from collections import namedtuple


@dataclass
class DataClassCard:
    rank: str
    suit: str


queen_of_hearts = DataClassCard("Q", "Hearts")


class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suiti = suit


queen_of_hearts = RegularCard("Q", "Hearts")
NamedTupleCard = namedtuple("NamedTupleCard", ["rank", "suit"])

Person = namedtuple(Person, ["first_initial", "last_name"])
