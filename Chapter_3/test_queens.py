from csp import Constraint, CSP
from queens import QueensConstraint, find_solution

def test_queens_constraint():
    columns  = [1, 2, 3, 4, 5, 6, 7, 8]
    domains = {1: [1, 2, 3, 4, 5, 6, 7, 8],
                2: [1, 2, 3, 4, 5, 6, 7, 8],
                3: [1, 2, 3, 4, 5, 6, 7, 8],
                4: [1, 2, 3, 4, 5, 6, 7, 8],
                5: [1, 2, 3, 4, 5, 6, 7, 8],
                6: [1, 2, 3, 4, 5, 6, 7, 8],
                7: [1, 2, 3, 4, 5, 6, 7, 8],
                8: [1, 2, 3, 4, 5, 6, 7, 8]}
    rows  = {}
    for column in columns:
        rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]
    csp = CSP(columns, rows)
    csp.add_constraint(QueensConstraint(columns))
    assert len(csp.constraints) == 8
    assert csp.domains == domains

def test_find_solution():
    result = find_solution()
    assert result == {1: 1, 2: 5, 3: 8, 4: 6, 5: 3, 6: 7, 7: 2, 8: 4}


    
