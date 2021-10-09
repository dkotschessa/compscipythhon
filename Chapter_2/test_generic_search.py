from generic_search import linear_contains, binary_contains, Stack, Node, Queue, PriorityQueue
from maze import MazeLocation

def test_linear_contains():
    assert linear_contains([1,2], 1) == True
    assert linear_contains([1,3,4], 2) == False



def test_binary_contains():
    assert binary_contains([1,2], 1) == True
    assert binary_contains([1,3,4], 2) == False

def test_stack():
    s = Stack()
    assert s.empty == True
    s.push(1)
    s.push(2)
    s.push(3)
    t = Stack()
    assert str(s) == '[1, 2, 3]'
    s.pop()
    assert str(s) == '[1, 2]'
    s.pop()
    assert str(s) == '[1]'
    s.pop()
    assert s.empty == True

def test_node():
    location1 = MazeLocation(1,2)
    location2 = MazeLocation(2,3)
    n = Node(location1, location2)
    assert n.state == location1
    assert n.parent == location2
    assert n.cost == 0.0
    assert n.heuristic == 0.0

def test_queue_empty():
    q = Queue()
    assert q.empty == True

def test_queue_push():
    q = Queue()
    q.push(1)
    q.push(2)
    assert list(q._container) == [1,2]

def test_queue_pop():
    q = Queue()
    q.push(1)
    q.push(2)
    assert q.pop() == 1 # FIFO
    assert list(q._container) == [2]


def test_priority_queue():
    q = PriorityQueue()
    assert q.empty
    q.push(1)
    assert not q.empty
    q.push(2)
    assert q._container == [1,2]
    q.pop()
    assert q._container == [2] #FIFO
    





