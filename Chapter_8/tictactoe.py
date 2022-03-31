from __future__ import annotations
from enum import Enum
from board import Piece, Board, Move
from typing import List


class TTTPiece(Piece, Enum):
    X = "X"
    O = "O"
    E = " "  # stand in for empty

    @property
    def opposite(self) -> TTTPiece:
        if self == TTTPiece.X:
            return TTTPiece.O
        elif self == TTTPiece.O:
            return TTTPiece.X
        else:
            return TTTPiece.E

    def __str__(self) -> str:
        return self.value


class TTTBoard(Board):
    def __init__(
        self, position: List[TTTPiece] = [TTTPiece.E] * 9, turn: TTTPiece = TTTPiece.X
    ) -> None:
        self.position: List[TTTPiece] = position
        self._turn: TTTPiece = turn

    @property
    def turn(self) -> Piece:
        return self._turn

    def move(self, location: Move) -> Board:
        temp_position: List[TTTPiece] = self.position.copy()
        temp_position[location] = self._turn
        return TTTBoard(temp_position, self._turn.opposite)

    @property
    def legal_moves(self) -> List[Move]:
        return [
            Move(l) for l in range(len(self.position)) if self.position[l] == TTTPiece.E
        ]

    @property
    def is_win(self) -> bool:
        first_row_win = (
            self.position[0] == self.position[1]
            and self.position[0] == self.position[2]
            and self.position[0] != TTTPiece.E
        )
        second_row_win = (
            self.position[3] == self.position[4]
            and self.position[3] == self.position[5]
            and self.position[3] != TTTPiece.E
        )
        third_row_win = (
            self.position[6] == self.position[7]
            and self.position[6] == self.position[8]
            and self.position[6] != TTTPiece.E
        )
        first_column_win = (
            self.position[0] == self.position[3]
            and self.position[0] == self.position[6]
            and self.position[0] != TTTPiece.E
        )
        second_column_win = (
            self.position[1] == self.position[4]
            and self.position[1] == self.position[7]
            and self.position[1] != TTTPiece.E
        )
        third_column_win = (
            self.position[2] == self.position[5]
            and self.position[2] == self.position[8]
            and self.position[2] != TTTPiece.E
        )
        l_to_r_diagonal_win = (
            self.position[0] == self.position[4]
            and self.position[0] == self.position[8]
            and self.position[0] != TTTPiece.E
        )
        r_to_l_diagonal_win = (
            self.position[2] == self.position[4]
            and self.position[2] == self.position[6]
            and self.position[2] != TTTPiece.E
        )

        return (
            first_row_win
            or second_row_win
            or third_row_win
            or first_column_win
            or second_column_win
            or third_column_win
            or l_to_r_diagonal_win
            or r_to_l_diagonal_win
        )

    def evaluate(self, player: Piece) -> float:
        if self.is_win and self.turn == player:
            return -1

        elif self.is_win and self.turn != player:
            return 1

        else:
            return 0

    def __repr__(self) -> str:
        return f"""
        {self.position[0]}|{self.position[1]}|{self.position[2]}
        -----
        {self.position[3]}|{self.position[4]}|{self.position[5]}
        -----
        {self.position[6]}|{self.position[7]}|{self.position[8]}"""
