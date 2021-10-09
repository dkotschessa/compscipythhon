from missionaries import MCState, node_to_path, display_solution
from generic_search import bfs

def test_mcstate_init():
    state = MCState(3, 3, True)
    assert state.wm == 3
    assert state.wc == 3
    assert state.em == 0
    assert state.ec == 0
    assert state.boat == True

def test_mcstate_str_3_3_true():
    state = MCState(3, 3, True)
    state_str = str(state)
    assert state_str == 'On the west bank there are 3 missionaries and 3 cannibals.\nOn the east bank there are 0 missionaries and 0 cannibals.\nThe boat is on the west bank.'


def test_mcstate_str_2_2_false():
    state = MCState(2, 2, False)
    state_str = str(state)
    assert state_str == 'On the west bank there are 2 missionaries and 2 cannibals.\nOn the east bank there are 1 missionaries and 1 cannibals.\nThe boat is on the east bank.'

def test_goal_test():
    state = MCState(0, 0, True) # all on west bank
    assert state.goal_test() == True

def test_illegal_state():
    state = MCState(2, 3, True) # More cannibals than missionaries
    assert state.is_legal == False

def test_successors():
    state = MCState(0, 0, True) # all on west bank
    assert len(state.successors()) == 0 # no more moves
    state = MCState(3,2, False) # on cannibal on west to move
    assert len(state.successors()) == 1 # only one move left


def test_solution(capsys):
    start: MCState = MCState(3, 3, True)
    solution: Optional[Node[MCState]] = bfs(start, MCState.goal_test,
     MCState.successors)
    path: List[MCState] = node_to_path(solution)
    display_solution(path)
    captured = capsys.readouterr()
    # start statte
    assert "On the west bank there are 3 missionaries and 3 cannibals." in captured.out
    # end state
    assert "On the west bank there are 0 missionaries and 0 cannibals." in captured.out

