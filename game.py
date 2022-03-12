import cocos
import numpy as np

#Making a tic-tac-toe game
#

class TicTacToe(cocos.layer.Layer):

    #Representation -
    #board is a list of lists
    #pieces are crosses(1) or circles(2) or empty(3)
    #empty spaces are None
    #

    def __init__():
        super(TicTacToe, self).__init__()
        self.board = np.zeroes(3)
        self.who = 1


    def play():
        while(true):
            if not game_over():
                x_direction = int(input(f"Player {self.who}'s turn. x coordinate of your next move:"))
                y_direction = int(input(f"y coordinate of your next move:"))
                self.place(x, y)
                self.next_player()
            else:
                return

    def game_over():
        return self.board_full() or self.win_condition()

    def board_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return False
        return True

    def win_condition
        #Three parts - a row, a column or a diagnol
        for row in self.rows:
            if sum(row) == 6:
                self.winner = 2
                return True
            if sum(row) == 3:
                self.winner = 1
                return False
        for col in range(len(3))


    def place(self, x, y):
        self.board[y][x] = self.who

    def next_player():
        self.who = abs(self.who -1)
