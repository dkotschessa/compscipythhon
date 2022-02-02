from csp import Constraint, CSP



class SendMoreMoneyConstraint(Constraint):
    def __init__(self, letters):
        super().__init__(letters)
        self.letters = letters

    def satisfied(self, assignment):
        #if there are duplicate values, then it's not a solution
        if len(set(assignment.values())) < len (assignment):
            return False


        #if  all variablees have assigned, check if iit adds correctly
        if len(assignment) == len(self.letters):
            s = assignment['S']
            e = assignment['E']
            n = assignment['N']
            d = assignment['D']
            m = assignment['M']
            o = assignment['O']
            r = assignment['R']
            y = assignment['Y']

            send = s * 1000 + e * 100 + n * 10 + d
            more = m * 1000 + o * 100 + r * 10 + e
            money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
            return send + more == money

        return True # no conflict



def solve_send_more_money():
    letters = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    possible_digits = {}
    for letter in letters:
        possible_digits[letter] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    possible_digits['M'] = [1] # don't want to start wiith 0
    csp = CSP(letters, possible_digits)
    csp.add_constraint(SendMoreMoneyConstraint(letters))
    solution = csp.backtracking_search()
    if solution is None:
        return("no solution found")
    else:
        return(solution)
