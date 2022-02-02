from random import choice
from string import ascii_uppercase
from csp import CSP, Constraint
from typing import NamedTuple

class GridLocation(NamedTuple):
    row: int
    column: int


def generate_grid(rows, columns):
    #initialize grid with random letters
    grid = [[choice(ascii_uppercase) for c in range(columns)] for r in range(rows)]
    return grid

def display_grid(grid):
    for row in grid:
        print("".join(row))

def generate_domain(word, grid):
    domain = []
    height = len(grid)
    width = len(grid[0])
    length = len(word)
    for row in range(height):
        for col in range(width):
            columns = range(col, col + length + 1)
            rows = range(row, row + length + 1)
            if col + length <= width:
                # left to right
                left_to_right = [GridLocation(row, c) for c in columns]
                domain.append(left_to_right)
                # diagonal towards bottom right
                if row + length <= height:
                    diagonal_towards_bottom_right = [GridLocation(r, col + (r - row)) for r in rows]
                    domain.append(diagonal_towards_bottom_right)
            if row + length <= height:
                # top to bottom
                top_to_bottom = [GridLocation(r, col) for r in rows]
                domain.append(top_to_bottom)
                # diagonal towards bottom left
                if col - length >= 0:
                    diagonal_towards_bottom_left = [GridLocation(r, col - (r - row)) for r in rows]
                    domain.append(diagonal_towards_bottom_left)
        return domain

class WordSearchConstraint(Constraint):
    def __init__(self, words):
        super().__init__(words)
        self.words = words

    def satisfied(self, assignment):
        all_locations = [locs for values in assignment.values() for locs in values]
        return len(set(all_locations)) == len(all_locations)
    
def run_word_search():
    grid = generate_grid(9, 9)
    words = ["matthew", "joe", "mary", "SARAH", "SALLY"] # some lowercasee tomake them visible
    locations = {}
    for word in words:
        locations[word] = generate_domain(word, grid)
    csp = CSP(words, locations)
    csp.add_constraint(WordSearchConstraint(words))
    solution = csp.backtracking_search()
    if solution is None:
        print("No solution found")
    else:
        for word, grid_locations in solution.items():
            #random reverse half the time
            if choice([True, False]):
                grid_locations.reverse()
            for index, letter in enumerate(word):
                (row, col) = (grid_locations[index].row, grid_locations[index].column)
                grid[row][col] = letter
    display_grid(grid)


