# reveal.py

import math
reveal_type(math.pi)  # only works in mypy

radius = 1
circumference = 2 * math.pi * radius
reveal_locals() # only works in mypy


pi: float = 3.142

def circumference(radius: float) -> float:
    return 2 * pi * radius

    
