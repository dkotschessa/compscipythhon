from enum import Enum
from board import Piece, Board, Move


class C4Piece(Piece, Enum):
    B = "B"
    R = "R"
    E = " "  # stand-in for empty

    @property
    def opposite(self):
        if self == C4Piece.B:
            return C4Piece.R
        elif self == C4Piece.R:
            return C4Piece.B
        else:
            return C4Piece.E

    def __str__(self):
        return self.value


def generate_segments(
    num_columns: int, num_rows: int, segment_length: int
) -> List[List[Tuple[int, int]]]:
    segments = []
    # generate the vertical segments
    for c in range(num_columns):
        for r in range(num_rows - segment_length + 1):
            segment = []
            for t in range(segment_length):
                segment.append((c, r + t))
            segments.append(segment)

    # generate the horizontal segments
    for c in range(num_columns - segment_length + 1):
        for r in range(num_rows):
            segment = []
            for t in range(segment_length):
                segment.append((c + t, r))
            segments.append(segment)

    # generate the bottom left to top right diagonal segments
    for c in range(num_columns - segment_length + 1):
        for r in range(num_rows - segment_length + 1):
            segment = []
            for t in range(segment_length):
                segment.append((c + t, r + t))
            segments.append(segment)

    # generate the top left to bottom right diagonal segments
    for c in range(num_columns - segment_length + 1):
        for r in range(segment_length - 1, num_rows):
            segment = []
            for t in range(segment_length):
                segment.append((c + t, r - t))
            segments.append(segment)
    return segments


class C4Board(Board):
    NUM_ROWS: int = 6
    NUM_COLUMNS: int = 7
    SEGMENT_LENGTH: int = 4
    SEGMENTS: List[List[Tuple[int, int]]] = generate_segments(
        NUM_COLUMNS, NUM_ROWS, SEGMENT_LENGTH
    )

    class Column:
        def __init__(self):
            self._container: List[C4Piece] = []

        @property
        def full(self):
            return len(self._container) == C4Board.NUM_ROWS

        def push(self, item: C4Piece):
            if self.full:
                raise OverflowError("Trying to push piece to full column")
            self._container.append(item)

        def __getitem__(self, index: int):
            if index > len(self._container) - 1:
                return C4Piece.E
            return self._container[index]

        def __repr__(self):
            return repr(self._container)

        def copy(self):
            temp = C4Board.Column()
            temp._container = self._container.copy()
            return temp

    def __init__(self, position=None, turn=C4Piece.B):
        if position is None:
            self.position = [C4Board.Column() for _ in range(C4Board.NUM_COLUMNS)]
        else:
            self.position = position
        self._turn: C4Piece = turn

    @property
    def turn(self):
        return self._turn

    def move(self, location: Move):
        temp_position = self.position.copy()
        for c in range(C4Board.NUM_COLUMNS):
            temp_position[c] = self.position[c].copy()
        temp_position[location].push(self._turn)
        return C4Board(temp_position, self._turn.opposite)

    @property
    def legal_moves(self):
        return [
            Move(c) for c in range(C4Board.NUM_COLUMNS) if not self.position[c].full
        ]

    # Returns the count of black & red pieces in a segment
    def _count_segment(self, segment):
        black_count: int = 0
        red_count: int = 0
        for column, row in segment:
            if self.position[column][row] == C4Piece.B:
                black_count += 1
            elif self.position[column][row] == C4Piece.R:
                red_count += 1
        return black_count, red_count

    @property
    def is_win(self):
        for segment in C4Board.SEGMENTS:
            black_count, red_count = self._count_segment(segment)
            if black_count == 4 or red_count == 4:
                return True
        return False

    def _evaluate_segment(self, segment, player):
        black_count, red_count = self._count_segment(segment)
        if red_count > 0 and black_count > 0:
            return 0  # mixed segments are neutral
        countt = max(red_count, black_count)
        score = 0
        if count == 2:
            score = 1
        elif count == 3:
            score = 100
        elif count == 4:
            score = 1000000
        color = C4Piece.B
        if red_count > black_count:
            color = C4Piece.R
        if color != player:
            return -score
        return score

    def evaluate(self, player: Piece) -> float:
        total = 0
        for segment in C4Board.SEGMENTS:
            total += self._evaluate_segment(segment, player)
        return total

    def __repr__(self):
        display: str = ""
        for r in reversed(range(C4Board.NUM_ROWS)):
            display += "|"
            for c in range(C4Board.NUM_COLUMNS):
                display += f"{self.position[c][r]}" + "|"
            display += "\n"
        return display
