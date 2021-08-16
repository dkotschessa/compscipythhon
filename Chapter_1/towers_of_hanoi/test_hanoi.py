from hanoi import Stack, hanoi, move_disc
import pytest



def test_fill_stack():
    """test puttingut 3 discs on container A"""
    tower_a: Stack[int] = Stack()
    tower_b: Stack[int] = Stack()
    tower_c: Stack[int] = Stack()
    num_discs: int = 3
    for i in range(1, num_discs + 1):
        tower_a.push(i)
    assert tower_a._container == [1,2,3]
    assert tower_b._container == []
    assert tower_c._container == []


def test_move_disc():
    """ test moving from one tower to another"""
    tower_a: Stack[int] = Stack()
    tower_b: Stack[int] = Stack()
    tower_c: Stack[int] = Stack()
    num_discs: int = 3
    for i in range(1, num_discs + 1):
        tower_a.push(i)
    
    
    move_disc(from_tower=tower_a, to_tower=tower_b)
    assert tower_a._container == [1,2]
    #assert tower_b == [3]




def test_hanoi():
    tower_a: Stack[int] = Stack()
    tower_b: Stack[int] = Stack()
    tower_c: Stack[int] = Stack()


    num_discs: int = 3
    for i in range(1, num_discs + 1):
        tower_a.push(i)

    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)
    assert tower_c._container == [1,2,3]
 

