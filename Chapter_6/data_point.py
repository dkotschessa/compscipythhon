from math import sqrt


class DataPoint:
    def __init__(self, initial):
        self._originals = tuple(initial)
        self.dimensions = tuple(initial)

    @property
    def num_dimensions(self):
        return len(self.dimensions)

    def distance(self, other):
        combined = zip(self.dimensions, other.dimensions)
        differences = [(x - y) ** 2 for x, y in combined]
        return sqrt(sum(differences))

    def __eq__(self, other):
        if not isinstance(other, DataPoint):
            return NotImplemented
        return self.dimensions == other.dimensions

    def __repr__(self):
        return self._originals.__repr__()
