import cocos
import numpy as np


class MiniGame:
    def __init__(self, args):
        state = f(args)

    def play():
        while not self.over():
            self.player_move()
            if not self.over():
                self.ai_move()
        return self.player_wins()

    def over():
        pass

    def player_move():
        pass

    def ai_move():
        pass

    def player_wins():
        pass



# Making a tic-tac-toe game
#


class TicTacToe(cocos.layer.Layer):

    # Representation -
    # board is a list of lists
    # pieces are crosses(1) or circles(2) or empty(3)
    # empty spaces are None
    #

    def __init__():
        super(TicTacToe, self).__init__()
        self.board = np.zeroes(3)
        self.who = 1

    def game_over():
        while true:
        return self.board_full() or self.win_condition()
                x_direction = int(
                    input(f"Player {self.who}'s turn. x coordinate of your next move:")
                )
    def board_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return False
        return True

    def win_condition(self):
        #Three parts - a row, a column or a diagnol
        for row in self.rows:
            if sum(row) == 6:
                self.winner = 2
                return True
            if sum(row) == 3:
                self.winner = 1
                return False
        for col in range(len(3)):
        # Three parts - a row, a column or a diagnol


    def place(self, x, y):
        self.board[y][x] = self.who

