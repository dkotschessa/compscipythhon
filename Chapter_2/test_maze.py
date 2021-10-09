from maze import Cell, Maze, MazeLocation, euclidean_distance, manhattan_distance
import pytest
from generic_search import node_to_path
from generic_search import dfs, bfs, astar




def test_cell():
    assert Cell.EMPTY == ' '
    assert Cell.BLOCKED == 'X'
    assert Cell.START == 'S'
    assert Cell.GOAL == 'G'
    assert Cell.PATH == '*'




def test_maze_start_goal():
    m: Maze = Maze()
    maze_string = m.__str__()
    maze_array = maze_string.split('\n')
    assert maze_string[0][0] == 'S'
    assert 'G' in maze_array[-2]

def test_maze_init():
    m: Maze = Maze()
    assert m._rows == 10
    assert m._columns == 20
    assert m.start == MazeLocation(0,0)
    assert m.goal == MazeLocation(9,9)

def test_goal_test():
    m: Maze = Maze()
    not_goal = MazeLocation(3,3)
    assert not m.goal_test(not_goal)
    real_goal = MazeLocation(9,9)
    assert m.goal_test(real_goal)

def test_successors():

    m: Maze = Maze(sparseness=0) # completely open maze
    loc = MazeLocation(5,5)
    successors_list = m.successors(loc)
    assert successors_list[0] == MazeLocation(6,5)
    assert successors_list[1] == MazeLocation(4,5)
    assert successors_list[2] == MazeLocation(5,6)
    assert successors_list[3] == MazeLocation(5,4)

def test_successors_blocked():
    """ Completely blocked maze should have no successors"""
    m = Maze(sparseness=1)
    loc = MazeLocation(5,5)
    successors_list = m.successors(loc)
    assert len(successors_list) == 0
    
def test_mark():
    m: Maze = Maze(sparseness=0) # completely open maze
    path = [(1,1), (1,2), (1,3), (1,4), (1,5)]
    maze_path = [MazeLocation(x,y) for (x,y) in path]
    m.mark(maze_path)
    assert m._grid[1][1:6] == ['*', '*', '*', '*', '*']
    

def test_clear():
    m: Maze = Maze(sparseness=0) # completely open maze
    path = [(1,1), (1,2), (1,3), (1,4), (1,5)]
    maze_path = [MazeLocation(x,y) for (x,y) in path]
    m.mark(maze_path)
    assert m._grid[1][1:6] == ['*', '*', '*', '*', '*']
    m.clear(maze_path)
    assert m._grid[1][1:6] == [' ', ' ', ' ', ' ', ' ']




def test_maze_solvable_dfs():
    """ a maze with zero sparseness should always be solvable"""
    m: Maze = Maze(sparseness=0)
    solution: Optional[Node[MazeLocation]] = dfs(m.start, m.goal_test, m.successors)
    assert solution
    path1: List[MazeLocation] = node_to_path(solution)
    m.mark(path1)
    assert m._grid[8][9] == '*' # spot right above goal should be marked


def test_maze_solvable_bfs():
    """ a maze with zero sparseness should always be solvable"""
    m: Maze = Maze(sparseness=0)
    solution: Optional[Node[MazeLocation]] = bfs(m.start, m.goal_test, m.successors)
    assert solution
    path1: List[MazeLocation] = node_to_path(solution)
    m.mark(path1)
    assert m._grid[9][8] == '*' # spot LEFT of goal marked


def test_euclidean_distance():
    origin = MazeLocation(0,0)
    goal = MazeLocation(3,4)
    e_distance = euclidean_distance(goal)
    distance_to_goal = e_distance(origin)
    assert distance_to_goal == 5.0
    

def test_manhattan_distance():
    origin = MazeLocation(0,0)
    goal = MazeLocation(3,4)
    m_distance = manhattan_distance(goal)
    distance_to_goal = m_distance(origin)
    assert distance_to_goal == 7.0


def test_maze_astar():
    m: Maze = Maze(sparseness=0)
    distance: Callable[[MazeLocation], float] = manhattan_distance(m.goal)
    solution3: Optional[Node[MazeLocation]] = astar(m.start, m.goal_test, m.successors, distance)  
    path3: List[MazeLocation] = node_to_path(solution3)
    m.mark(path3)
    assert m._grid[9][8] == '*' # spot LEFT of goal marked











