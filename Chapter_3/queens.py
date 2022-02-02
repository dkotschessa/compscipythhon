from csp import Constraint, CSP

class QueensConstraint(Constraint):
    def __init__(self, columns):
        super().__init__(columns)
        self.columns = columns

    def satisfied(self, assignment):
        #q1c = queen 1 column, q1r = queen 1 row
        for q1c, q1r in assignment.items():
            #q2c = queen 2 column
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignment:
                    q2r = assignment[q2c] #q2r = queen 2 row
                    if q1r == q2r: #same row?
                        return False
                    if abs(q1r - q2r) == abs(q1c-q2c): #same diagonal
                        return False
        return True



def find_solution():
    columns = [1, 2, 3, 4, 5, 6, 7, 8]
    rows  = {}
    for column in columns:
        rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]
    csp = CSP(columns, rows)
    csp.add_constraint(QueensConstraint(columns))
    solution = csp.backtracking_search()
    if solution is None:
        return("No solution found!")
    else:
        return(solution)



