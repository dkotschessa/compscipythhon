from send_more_money import solve_send_more_money
from csp import Constraint

def test_send_more_money():
    solution = solve_send_more_money()
    assert solution == {'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O': 0, 'R': 8, 'Y': 2}
    


