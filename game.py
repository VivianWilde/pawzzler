
import random

#Making a tic-tac-toe game
#

class TicTacToe(): #TODO inherit from MiniGame

    #Representation -
    #board is a list
    #pieces are crosses(1 - player) or circles(2 - ai) or empty(0)
    #

    def __init__(self):
        #super().__init__()
        self.board = [f"{x}" for x in range(9)]
        self.player_marker = "X"
        self.ai_marker = "O"

    def over(self):
        return TicTacToe.game_over(self.board)

    @staticmethod
    def game_over(board):
        return winner(self.board) != 'None' or not TicTacToe.available(self.board)

    @staticmethod
    def winner(board):
        for j in (player_marker, ai_marker):
            #rows
            for row in range(3):
                if board[0+(row*3)] == board[1+(row*3)] == board[2 + (row*3)] == j:
                    return j

            #columns
            for col in range(3):
                if board[0+col] == board[3+col] == board[6+col] == j:
                    return j
            #diagonals
            if board[0] == board[5] == board[8] == j:
                return j
            if board[2] == baord[5] == board[6] == j:
                return j
        return 'None'

    @staticmethod
    def available(board):
        return [int(x) for x in board if (x != self.player_marker and x!= self.ai_marker)]

    def player_victory(self):
        return TicTacToe.winner(self.board) == self.player_marker


    def place(self, board, spot, marker):
        board[spot] = marker


    def player_move(self):
        x = int(input(f"Your turn. x coordinate of your next move:")) #magic(frontend)
        y = int(input(f"y coordinate of your next move:")) #magic(frontend)
        spot = y*3 + x
        self.place(self.board, spot, self.player_marker)

    def ai_move(self):

        random.seed()
        best_spot = None
        if random.random() > 0.7:
            best_spot = available[random.ranint(0,len(available))]
        else:
            scores = []
            available = TicTacToe.available(self.board)
            for spot in available:
                new_board = self.board[:]
                new_board[spot] = self.ai_marker
                scores.append(minimax(new_board, self.player_marker))
                best_spot = available[scores.index(max(scores))]

        self.place(self.board, best_spot, self.ai_marker)


 
    @staticmethod
    def minimax(board, player):
        """Returns the score of the board"""

        winner = TicTacToe.winner(board)
        if winner == self.player_marker:
            return -10
        if winner == self.ai_marker:
            return +10
        if winner == 'None' and not TicTacToe.available(board):
            return 0

        available = TicTacToe.available(board)
        scores = []
        for spot in available:
            new_board = board[:]
            new_board[spot] = player
            scores.append(minimax(new_board,TicTacToe.other(player)))

        if player == self.player_marker:
            return min(scores)
        if player == self.ai_marker:
            return max(scores)


    @staticmethod
    def other(player):
        if player == self.player_marker:
            return self.ai_marker
        else:
            return self.player_marker

    def __str__(self):
        return str(self.board)
