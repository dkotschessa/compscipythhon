from dna_search import (
    Nucleotide,
    Codon,
    Gene,
    string_to_gene,
    linear_contains,
    binary_contains,
)
import random


def test_Nucleotide():
    assert Nucleotide.A == 1
    assert Nucleotide.C == 2
    assert Nucleotide.G == 3
    assert Nucleotide.T == 4


def test_gene_to_string():
    gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"
    test_gene = string_to_gene(gene_str)

    first_codon = test_gene[0]

    assert len(test_gene) == len(gene_str) / 3

    assert first_codon[0] == Nucleotide.A
    assert first_codon[1] == Nucleotide.C
    assert first_codon[2] == Nucleotide.G


def test_linear_contains_true():

    gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"
    my_gene: Gene = string_to_gene(gene_str)
    acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
    assert linear_contains(my_gene, acg) == True


def test_linear_contains_false():

    gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"
    my_gene: Gene = string_to_gene(gene_str)
    gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
    assert linear_contains(my_gene, gat) == False


def test_binary_contains_true():

    gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"
    my_gene: Gene = string_to_gene(gene_str)
    acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)

    my_sorted_gene: Gene = sorted(my_gene)
    assert binary_contains(my_sorted_gene, acg) == True


def test_binary_contains_false():

    gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"
    my_gene: Gene = string_to_gene(gene_str)
    gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
    my_sorted_gene: Gene = sorted(my_gene)
    assert binary_contains(my_sorted_gene, gat) == False
