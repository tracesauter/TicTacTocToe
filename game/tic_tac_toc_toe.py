import numpy as np
from enum import Enum
from typing import Tuple, List

class Player(Enum):
    X = 1
    O = -1

    def next(self):
        if self == Player.X:
            return Player.O
        else:
            return Player.X
    
    @staticmethod
    def get_name_from_value(value: int) -> str:
        if value == 1:
            return Player.X.name
        elif value == -1:
            return Player.O.name
        else:
            return " "


class TicTacTocToe:
    def __init__(self):
        self.board = np.zeros((4,4))
        self.turn: int = 1
        self.player: Player = Player.X
        self.winner = None
    
    def reset(self):
        self.board = np.zeros((4,4))
        self.turn = 1
        self.player = Player.X
        self.winner = None

    def move(self, row: int, col: int) -> None:
        if self.board[row][col] == 0:
            self.board[row][col] = self.player.value
            winner = self.get_winner()
            if winner != 0:
                self.winner = winner
                print(f"Player {self.winner} wins!")
            elif self.turn == 16:
                self.winner = 0
                print("Draw!")
            else:
                self.turn += 1
                self.player = self.player.next()
        else:
            print("Invalid move")
    
    def print_board(self) -> None:
        print("  | 0 | 1 | 2 | 3 |")
        print("  -----------------")
        for i in range(4):
            print(f"{i} |", end=" ")
            for j in range(4):
                print(Player.get_name_from_value(self.board[i][j]), end=" | ")
            print("\n  -----------------")

    def check_column(self, col: int) -> int:
        if np.sum(self.board[:,col]) == 4:
            return 1
        elif np.sum(self.board[:,col]) == -4:
            return -1
        else:
            return 0
    
    def check_row(self, row: int) -> int:
        if np.sum(self.board[row,:]) == 4:
            return 1
        elif np.sum(self.board[row,:]) == -4:
            return -1
        else:
            return 0
    
    def check_diagonal(self) -> int:
        if np.sum(np.diag(self.board)) == 4:
            return 1
        elif np.sum(np.diag(self.board)) == -4:
            return -1
        else:
            return 0
    
    def check_anti_diagonal(self) -> int:
        if np.sum(np.diag(np.fliplr(self.board))) == 4:
            return 1
        elif np.sum(np.diag(np.fliplr(self.board))) == -4:
            return -1
        else:
            return 0
    
    def get_winner(self) -> int:
        for i in range(4):
            if self.check_column(i) == 1 or self.check_row(i) == 1:
                return 1
            elif self.check_column(i) == -1 or self.check_row(i) == -1:
                return -1
        if self.check_diagonal() == 1 or self.check_anti_diagonal() == 1:
            return 1
        elif self.check_diagonal() == -1 or self.check_anti_diagonal() == -1:
            return -1
        else:
            return 0
    
    def get_open_positions(self) -> List[Tuple[int, int]]:
        open_positions: List[Tuple[int, int]] = []
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    open_positions.append((i,j))
        return open_positions

    def pick_random_move(self) -> Tuple[int, int]:
        open_positions = self.get_open_positions()
        random_index: int = np.random.randint(len(open_positions))
        return open_positions[random_index]

# function to play the game against the computer
def play_game():
    game = TicTacTocToe()
    game.print_board()
    while game.winner == None:
        if game.player == Player.X:
            (row, col) = input("Enter row and column separated by space: ").split()
            row, col = int(row), int(col)
            game.move(row, col)
        else:
            row, col = game.pick_random_move()
            game.move(row, col)
        game.print_board()
        print('\n\n\n')
    if game.winner == 0:
        print("Game over! Draw!")
    else:
        print(f"Game over! Winner is {Player.get_name_from_value(game.winner)}")
    game.reset()

if __name__ == "__main__":
    play_game()
