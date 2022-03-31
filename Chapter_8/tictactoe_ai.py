from minimax import find_best_move
from tictactoe import TTTBoard
from board import Board, Move

board = TTTBoard()


def get_player_move():
    player_move = Move(1)
    while player_move not in board.legal_moves:
        play = int(input("Enter a legal square (0-8)"))
        player_move = Move(play)
    return player_move


if __name__ == "__main__":
    # main game loop
    while True:
        human_move = get_player_move()
        board = board.move(human_move)
        if board.is_win:
            print("Human wins!")
            break
        elif board.is_draw:
            print("Draw!")
            break
        computer_move = find_best_move(board)
        print(f"Computer move is {computer_move}")
        board = board.move(computer_move)
        print(board)
        if board.is_win:
            print("Computer wins!")
            break
        elif board.is_draw:
            print("Draw!")
            break
