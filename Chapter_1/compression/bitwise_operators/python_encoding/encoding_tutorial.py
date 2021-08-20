# from https://realpython.com/python-encodings-guide/

import string
from math import ceil, log

s = "What's wrong with ASCII?!?!"

def example1():
    s = "What's wrong with ASCII?!?!"
    print(s)
    print(s.rstrip(string.punctuation))

def make_bitseq(s: str) -> str:
    """.git/Here’s a handy way to represent ASCII strings as
     sequences of bits in Python. Each character from the ASCII 
     string gets pseudo-encoded into 8 bits, with spaces in between 
     the 8-bit sequences that each represent a single character:
    """

    if not s.isascii():
        raise ValueError("ASCII only allowed")
    return " ".join(f"{ord(i):08b}" for i in s)


def n_possible_values(nbits: int) -> int:
    """ 
    Given a number of bits, what is the number of values that can be repreesented?
    1  it can be 1 or 0
    2 bits can be
    00
    01
    10
    11
    """

    return 2 ** nbits

def n_bits_required(nvalues: int) -> int:
    """ given a range of possible values, how can we find the 
    number of bits n that is required for the range to be fully represented
    i.e. solve for n in 2^n = x"""
    return ceil(log(nvalues) / log(2))

# Note the ranges for ASCII

# Code Point Range	    Class
# 0 through 31	        Control/non-printable characters
# 32 through 64	        Punctuation, symbols, numbers, and space
# 65 through 90	        Uppercase English alphabet letters
# 91 through 96	        Additional graphemes, such as [ and \
# 97 through 122       	Lowercase English alphabet letters
# 123 through 126	    Additional graphemes, such as { and |
# 127	                Control/non-printable character (DEL)



n_bits_required(128)  # 0 through 127 - answer is 7, so
                      # ASCII is 7 bit code

                      

# It's one bit short of a byte!


# +-----------------+----------+---------+
# | Type of Literal |  Prefix  | Example |
# +-----------------+----------+---------+
# | n/a             | n/a      | 11      |
# | Binary literal  | 0b or 0B | 0b11    |
# | Octal literal   | 0o or 0O | 0o11    |
# | Hex literal     | 0x or 0X | 0x11    |
# +-----------------+----------+---------+

def utf_8_encode(s = "résumé"):
    return s.encode('utf-8')

def utf_8_decode(s =  b'r\xc3\xa9sum\xc3\xa9'):
    return s.decode('utf-8')

# utf_8_encode('El Niño') 
b'El Ni\xc3\xb1o'
# the 'El' is asci compatible 
# the n tilde is escaped to hex

# UTF 8 is variable length
ibrow = "🤨"
ibrow_length = len(ibrow)

ibrow_decoded = utf_8_encode(ibrow)

ibrow_length_encoded = len(ibrow_decoded)

# Calling list() on a bytes object gives you
# the decimal value for each byte
decimal_values_for_each_byte  = list(ibrow_decoded)


# +------------------+------------------------------+----------------------------------------------------+-------------------------+
# |  Decimal Range   |          Hex Range           |                  What’s Included                   |        Examples         |
# +------------------+------------------------------+----------------------------------------------------+-------------------------+
# | 0 to 127         | "\u0000" to "\u007F"         | U.S. ASCII                                         | "A", "\n", "7", "&"     |
# | 128 to 2047      | "\u0080" to "\u07FF"         | Most Latinic alphabets*                            | "ę", "±", "ƌ", "ñ"      |
# | 2048 to 65535    | "\u0800" to "\uFFFF"         | Additional parts of the multilingual plane (BMP)** | "ത", "ᄇ", "ᮈ", "‰"      |
# | 65536 to 1114111 | "\U00010000" to "\U0010FFFF" | Other***                                           | "𝕂", "𐀀", "😓", "🂲", |
# +------------------+------------------------------+----------------------------------------------------+-------------------------+

###
# PTYHON BUILT IN FUNCTIONS
###

ascii('abcdeefg') # ASCII only representation of an object 
ascii('jalepeño') # with non ASCII characters escaped (to hex)
ascii(0xc0ffee)  # Hex literal (int)

bin(0) # binary representation of an integer, with the prefix "0b"
bin(0xc0ffee) # Hex literal (int)


bytes(10) # coerces the input to bytes, representing raw binary data

# Iterable of ints
bytes((104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100))

bytes("real 🐍", "utf-8")  # String + encoding

chr(97) # chr() converts an integer code point to a single Unicode character:
chr(7048)


chr(1114111)


chr(0x10FFFF)  # Hex literal (int)


chr(0b01100100)  # Binary literal (int)

# hex() gives the hexadecimal representation of an integer, with the prefix "0x":


hex(100) 


[hex(i) for i in [1, 2, 4, 8, 16]]


[hex(i) for i in range(16)]

# int() coerces the input to int, optionally interpreting the input in a given base:

int(11.0)

int('11')
int('11', base=2)
int('11', base=8)
int('11', base=16)
int(0xc0ffee - 1.0)
int.from_bytes(b"\x0f", "little")
int.from_bytes(b'\xc0\xff\xee', "big")

# The Python ord() function converts a single Unicode character to its integer code point:
ord("a")
ord("ę")
ord("ᮈ")
[ord(i) for i in "hello world"]

# str() coerces the input to str, representing text:

str("str of string")
str(5)
str([1, 2, 3, 4])  # Like [1, 2, 3, 4].__str__(), but use str()
str(b"\xc2\xbc cup of flour", "utf-8")
str(0xc0ffee)

"""
Maybe read this a bunch of times
 https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
"""

# tend to assumee utf-8 theese days, but if you don't know
# https://chardet.readthedocs.io/en/latest/ is a useful library

# unicodedata library

import unicodedata

unicodedata.name("€")

unicodedata.lookup("EURO SIGN")

unicodedata.name("🐍")
