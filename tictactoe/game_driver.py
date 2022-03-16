from tictactoe import TicTacToe

my_game = TicTacToe()
print(my_game)
while not my_game.over():
    my_game.player_move()
    print(my_game)
    if not my_game.over():
        my_game.ai_move()
        print(my_game)
if my_game.player_victory():
    print("You won!")
