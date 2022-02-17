from word_search import generate_grid, display_grid, generate_domain


def test_grid():
    grid = generate_grid(5, 6)
    assert len(grid) == 5
    assert len(grid[0]) == 6


def test_display_grid(capsys):
    grid = generate_grid(5, 5)
    displayed_grid = display_grid(grid)
    captured = capsys.readouterr()
    assert type(captured.out) == str
    assert len(captured.out) == (5 + 1) * 5  # row with carriage return times columns


def test_generate_domain():
    word = "SPAM"
    rows = 5
    columns = 5
    grid = generate_grid(rows, columns)
    domain = generate_domain(word, grid)
    test_domain = domain[0]
    assert len(test_domain) == len(word) + 1
    assert test_domain[0].column == 0
    assert test_domain[1].column == 1
    assert test_domain[2].column == 2
    assert test_domain[3].column == 3
    assert test_domain[4].column == 4
