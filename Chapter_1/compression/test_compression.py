import pytest
from trivial_compression import CompressedGene
from sys import getsizeof

compress_params = [
    ('A', "00"),  # input, expected
    ('C', "01"),
    ('G', "10"),
    ('T', '11'),
]





@pytest.mark.parametrize("input, expected", compress_params)
def test_compression(input, expected):
    compressed = CompressedGene(input)
    bit_string = bin(compressed.bit_string)
    assert bit_string[3:] == expected  # last two
    


decompress_params = [
    (0b100, "A"),  # input, expected
    (0b101, "C"),  # remember the first 1 is sentinel
    (0b110, "G"),
    (0b111, 'T'),
]



@pytest.mark.parametrize("input, expected", decompress_params)
def test_decompress(input, expected):
    compressed = CompressedGene('A') # needs a value for input but we will edit the bit_string
    compressed.bit_string = input
    assert compressed.decompress() == expected


def test_compressed_is_smaller():
    string = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    original_size = getsizeof(string)
    compressed = CompressedGene(string)

    compressed_size = getsizeof(compressed.bit_string)

    assert compressed_size < original_size

def test_compressed_decompressed():
    string = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    original_size = getsizeof(string)
    compressed = CompressedGene(string)

    decompressed = compressed.decompress()

    assert string == decompressed 











