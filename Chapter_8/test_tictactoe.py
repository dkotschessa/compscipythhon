from __future__ import annotations
import unittest
from minimax import find_best_move
from tictactoe import TTTBoard, TTTPiece
from board import Move


def test_easy_position():
    # win in one move
    """
    XOX
    XEO
    EEO
    """

    to_win_easy_position = [
        TTTPiece.X,
        TTTPiece.O,
        TTTPiece.X,
        TTTPiece.X,
        TTTPiece.E,
        TTTPiece.O,
        TTTPiece.E,
        TTTPiece.E,
        TTTPiece.O,
    ]

    test_board1 = TTTBoard(to_win_easy_position, TTTPiece.X)
    answer1 = find_best_move(test_board1)
    assert answer1 == 6


def test_block_position():
    # must block O's to win
    """
    XEE
    EEO
    EXO
    """
    to_block_position = [
        TTTPiece.X,
        TTTPiece.E,
        TTTPiece.E,
        TTTPiece.E,
        TTTPiece.E,
        TTTPiece.O,
        TTTPiece.E,
        TTTPiece.X,
        TTTPiece.O,
    ]
    test_board2 = TTTBoard(to_block_position, TTTPiece.X)
    answer = find_best_move(test_board2)
    assert answer == 2


def test_hard_position():
    # find the best move to win 2 moves
    """
    XEE
    EEO
    OXE
    """
    to_win_hard_position = [
        TTTPiece.X,
        TTTPiece.E,
        TTTPiece.E,
        TTTPiece.E,
        TTTPiece.E,
        TTTPiece.O,
        TTTPiece.O,
        TTTPiece.X,
        TTTPiece.E,
    ]
    test_board3 = TTTBoard(to_win_hard_position, TTTPiece.X)

    answer3 = find_best_move(test_board3)
    assert answer3 == 1
