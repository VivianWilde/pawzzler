import random

# Making a tic-tac-toe game
#


class TicTacToe:  # TODO inherit from MiniGame

    # Representation -
    # board is a list
    # pieces are crosses(1 - player) or circles(2 - ai) or empty(0)
    #
    player_marker = "[X]"
    ai_marker = "[O]"

    def __init__(self):
        # super().__init__()
        self.board = ["[ ]" for x in range(9)]

    def over(self):
        return TicTacToe.game_over(self.board)

    @staticmethod
    def game_over(board):
        return TicTacToe.winner(board) != "None" or not TicTacToe.available(board)

    @staticmethod
    def winner(board):
        for j in (TicTacToe.player_marker, TicTacToe.ai_marker):
            # rows
            for row in range(3):
                if (
                    board[0 + (row * 3)]
                    == board[1 + (row * 3)]
                    == board[2 + (row * 3)]
                    == j
                ):
                    return j

            # columns
            for col in range(3):
                if board[0 + col] == board[3 + col] == board[6 + col] == j:
                    return j
            # diagonals
            if board[0] == board[4] == board[8] == j:
                return j
            if board[2] == board[4] == board[6] == j:
                return j
        return "None"

    @staticmethod
    def available(board):
        return [
            i
            for i in range(len(board))
            if (board[i] != TicTacToe.player_marker and board[i] != TicTacToe.ai_marker)
        ]

    def player_victory(self):
        return TicTacToe.winner(self.board) == TicTacToe.player_marker

    def place(self, board, spot, marker):
        board[spot] = marker

    def player_move(self):
        x = int(input("Your turn. x coordinate of your next move:"))  # magic(frontend)
        y = int(input("y coordinate of your next move:"))  # magic(frontend)
        spot = y * 3 + x
        self.place(self.board, spot, TicTacToe.player_marker)

    def ai_move(self):
        print("AI's move\n")
        available = TicTacToe.available(self.board)
        random.seed()
        best_spot = None
        if random.random() > 0.7:
            best_spot = available[random.randint(0, len(available) - 1)]
        else:
            scores = []
            for spot in available:
                new_board = self.board[:]
                new_board[spot] = TicTacToe.ai_marker
                scores.append(TicTacToe.minimax(new_board, TicTacToe.player_marker))
                best_spot = available[scores.index(max(scores))]

        self.place(self.board, best_spot, TicTacToe.ai_marker)

    @staticmethod
    def minimax(board, player):
        """Returns the score of the board"""

        winner = TicTacToe.winner(board)
        if winner == TicTacToe.player_marker:
            return -10
        if winner == TicTacToe.ai_marker:
            return +10
        if winner == "None" and not TicTacToe.available(board):
            return 0

        available = TicTacToe.available(board)
        scores = []
        for spot in available:
            new_board = board[:]
            new_board[spot] = player
            scores.append(TicTacToe.minimax(new_board, TicTacToe.other(player)))

        if player == TicTacToe.player_marker:
            return min(scores)
        if player == TicTacToe.ai_marker:
            return max(scores)

    @staticmethod
    def other(player):
        if player == TicTacToe.player_marker:
            return TicTacToe.ai_marker
        else:
            return TicTacToe.player_marker

    def __str__(self):
        display = ""
        for i in range(3):
            for j in range(3):
                display = display + f"{self.board[i*3 + j]}"
            display += "\n"
        return display
