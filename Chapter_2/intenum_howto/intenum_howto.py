# Tangential learning from https://docs.python.org/3.11/howto/enum.html
#

#first, enum

from enum import Enum
# class Weekday(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     SUNDAY = 7


from enum import Flag

class Weekday(Flag):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 4
    THURSDAY = 8
    FRIDAY = 16
    SATURDAY = 32
    SUNDAY = 64

weekend = Weekday.SATURDAY | Weekday.SUNDAY

# for day in weekend:
#     print(day)
# this doesn't work in python 3.8

##  intenum

from enum import IntEnum

class Shape(IntEnum):
    CIRCLE = 1
    SQUARE = 2

class Request(IntEnum):
    POST = 1
    GET = 2

# they work like number

"""
In [18]: Shape == 1
Out[18]: False

In [19]: Shape.CIRCLE == 1
Out[19]: True

In [20]: Shape.CIRCLE
Out[20]: <Shape.CIRCLE: 1>

In [21]: Shape.CIRCLE == Request.POST
Out[21]: True
"""
