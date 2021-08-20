"""
Side quest to learn more about bitwise operations
using tutorial from https://realpython.com/python-bitwise-operators/
"""

"""
In Python, strings are represented as arrays of Unicode code points.
 To reveal their ordinal values, call ord() on each of the characters:
"""

# +----------+---------+----------------------------+
# | Operator | Example |          Meaning           |
# +----------+---------+----------------------------+
# | &        | a & b   | Bitwise AND                |
# | |        | a | b   | Bitwise OR                 |
# | ^        | a ^ b   | Bitwise XOR (exclusive OR) |
# | ~        | ~a      | Bitwise NOT                |
# | <<       | a << n  | Bitwise left shift         |
# | >>       | a >> n  | Bitwise right shift        |
# +----------+---------+----------------------------+






# +----------+---------+---------------+
# | Operator | Example | Equivalent to |
# +----------+---------+---------------+
# | &=       | a &= b  | a = a & b     |
# | |=       | a |= b  | a = a | b     |
# | ^=       | a ^= b  | a = a ^ b     |
# | <<=      | a <<= n | a = a << n    |
# | >>=      | a >>= n | a = a >> n    |
# +----------+---------+---------------+





# Another tangent - Unicode and encodings https://realpython.com/python-encodings-guide/
# tangent completed!


ordinal = [ord(character) for character in "€uro"]

# This is the integer code point of each character  in unicode (see tutorial on encoding)
# rewrite them in binary

chr(97) # is the inverse

(42).bit_length() # check bit length (how long is the number in binary)


## short circuit evaluation

def call(x):
    print(f"call({x=})")
    return x

call(False) or call(True)  # Both operands evaluated



call(True) or call(False)  # Only the left operand evaluated

#unless you use bitwise operators

call(True) | call(False)

##Bitwise operators

a = 0b0000

b = 0b1111

"""
In [87]: a or b
Out[87]: 'ob0000'

In [88]: a and b
Out[88]: 'ob1111'

In [89]: a xor b
  File "<ipython-input-89-6637868c93bc>", line 1
    a xor b
      ^
SyntaxError: invalid syntax
"""

def xor(a, b):
    return (a and not b) or (not a and b)


"""
In [107]: bin(a | b)
Out[107]: '0b1111'

In [108]: bin(xor(a,b))
Out[108]: '0b1111'

In [109]: bin(a & b)
Out[109]: '0b0'
"""

"""
Note: Unsigned data types don’t let you store negative numbers such
 as -273 because there’s no space for a sign in a regular bit pattern.
  Trying to do so would result in a compilation error, a runtime 
  exception, or an integer overflow depending on the language used.
"""

# In [110]: ~344
# Out[110]: -345
#WHY? - 
# because this is the out put of binary
# 1 os 0b01
# ~1 is 0b10 - flipping each bit


#BITEWISE SHIFT


a = 0b100111

"""
In [121]: bin(a<<1)
Out[121]: '0b1001110'

In [123]: a << 2
Out[123]: 156
"""

#basically 
"""

a << n = a * (2**n)


1      1
10     2

100    4

1000   8

"""

# bit mask
# we wanto to constraing the length of a bit pattern so that a left shift of 
# 100111010     is
# 001110100      (the 1 on the left is gone)


"""
In [127]: 39 << 3
Out[127]: 312

In [128]: (39 << 3) & 255
Out[128]: 56
"""

# RIGHT SHIFT

x: int = 0b10011101
y: str = bin(x >> 1)
z: str = bin(a >> 2)

# shifting to the right is effectively halving

## result is floored a result is fractional

"""
In [168]: 5 >> 1
Out[168]: 2

In [169]: 5 //2
Out[169]: 2

In [170]: 5 /2
"""

## keep a bit length while shifting - use a bit mask

# arithmetic (pythn) vs logical shift (not)
# "sign bit" for positive/negative


# +---------------+---------------------+----------+------+-------------------------+
# | Decimal Value | Signed Binary Value | Sign Bit | Sign |         Meaning         |
# +---------------+---------------------+----------+------+-------------------------+
# |        -10010 |           100111002 |        1 | -    | Negative number         |
# |          2810 |           000111002 |        0 | +    | Positive number or zero |
# +---------------+---------------------+----------+------+-------------------------+


"""

In [171]: bin(-10)
Out[171]: '-0b1010'
"""
  
# logical right shift = zero filled right shift

# 10001100 --> 0100110

#the information about the sign (leftmost bit) is lost
# always replaced by zero so number is positive
# there is no logical right shift in python -can be simulated

from ctypes import c_uint32 as unsigned_int32

result = unsigned_int32(-100).value >> 1

"""
In [6]: print(bin(result))
0b1111111111111111111111111001110


>> is called the signed right shift operator - maintains the sign 

In [7]: num = bin(-10)


In [14]: num = -0b01

In [15]: num
Out[15]: -1

In [16]: num << 1
Out[16]: -2

In [17]: bin(num)
Out[17]: '-0b1'

Python doesn’t always store integers in plain two’s complement binary.
 Instead, it follows a custom adaptive strategy that works like sign-magnitude 
 with an unlimited number of bits. It converts numbers back and forth between their i
 nternal representation and two’s complement to mimic the standard behavior of the arithmetic shift.
"""


# +-----------------+----------------------+----------------+
# | Binary Sequence | Sign-Magnitude Value | Unsigned Value |
# +-----------------+----------------------+----------------+
# |       001010102 |                 4210 |           4210 |
# |       101010102 |                -4210 |          17010 |
# +-----------------+----------------------+----------------+

# A zero on the leftmost bit indicates a positive (+) number, and a one indicates a negative (-) number. 



# Two's complement


# +-------------------+------------------------+--------------------------+
# | Positive Sequence | One’s Complement (NOT) | Two’s Complement (NOT+1) |
# +-------------------+------------------------+--------------------------+
# | 000000002         | 111111112              | 000000002                |
# | 000000012         | 111111102              | 111111112                |
# | 000000102         | 111111012              | 111111102                |
# | ⋮                 | ⋮                       | ⋮                        |
# | 011111112         | 100000002              | 100000012                |
# +-------------------+------------------------+--------------------------+

##
## FLOATING POINT NUMBERS
##

# Single precision: 1 sign bit, 8 exponent bits, 23 mantissa bits
# Double precision: 1 sign bit, 11 exponent bits, 52 mantissa bits <<-- python Float

print(f"{42:b}")  # Print 42 in binary

print(f"{42:032b}")  # Print 42 in binary on 32 zero-padded digits

#or
bin(42)#binaryliteral

# ensure bit lengths by using a mask

mask = 0b11111111
bin(-42 & mask)

# or use modulo
bin(-42 % (1 << 8))

# or import fromctypes
from ctypes import c_uint8 as unsigned_byte
bin(unsigned_byte(-42).value)

"""sidebar: another tangent possibly: https://realpython.com/python-data-structures/
"""

# array module
from array import array

"""
 |  Arrays represent basic values and behave very much like lists, except
 |  the type of objects stored in them is constrained. The type is specified
 |  at object creation time by using a type code, which is a single character.
 |  The following type codes are defined:
 |  
 |      Type code   C Type             Minimum size in bytes
 |      'b'         signed integer     1
 |      'B'         unsigned integer   1
 |      'u'         Unicode character  2 (see note)
"""

signed = array("b", [-42, 42])
unsigned = array("B")
unsigned.frombytes(signed.tobytes())
unsigned
bin(unsigned[0])

bin(unsigned[1])

"""
Copying raw bytes between these two arrays changes how bits are interpreted. However, 
it takes twice the amount of memory, which is quite wasteful. To perform such a bit
 rewriting in place, you can rely on the struct module, which uses a similar set of format
  characters for type declarations:
"""

from struct import pack, unpack
unpack("BB", pack("bb", -42, 42))

bin(214)

"""
Built-In Data Types
Python bitwise operators are defined for the following built-in data types:

int
bool
set and frozenset
dict (since Python 3.9)

It’s not a widely known fact, but bitwise operators can perform operations from set algebra, 
such as union, intersection, and symmetric difference, as well as merge and update dictionaries.
"""



# +---------------------------------------+------------------+
# |              Set Method               | Bitwise Operator |
# +---------------------------------------+------------------+
# | a.union(b)                            | a | b            |
# | a.update(b)                           | a |= b           |
# | a.intersection(b)                     | a & b            |
# | a.intersection_update(b)              | a &= b           |
# | a.symmetric_difference(b)             | a ^ b            |
# | a.symmetric_difference_update(vegies) | a ^= b           |
# +---------------------------------------+------------------+


