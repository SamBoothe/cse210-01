'''
Tic-Tac-Toe
Author - Sam Boothe
'''

def main():
    player = next_player("")
    game_board = display_board()
    while not (winner(game_board) or draw(game_board)):
        display_game_board(game_board)
        player_move(player, game_board)
        player = next_player(player)
    display_game_board(game_board)
    if draw(game_board) == False:
        print("Good game. Thanks for playing!")
    else:
        print("Game is a draw! Better luck next time!")

def next_player(current_player):
    if current_player == "" or current_player == "o":
        return "x"
    elif current_player == "x":
        return "o"

def player_move(player, game_board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    game_board[square - 1] = player

def winner(game_board):
    return (game_board[0] == game_board[1] == game_board[2] or
            game_board[3] == game_board[4] == game_board[5] or
            game_board[6] == game_board[7] == game_board[8] or
            game_board[0] == game_board[3] == game_board[6] or
            game_board[1] == game_board[4] == game_board[7] or
            game_board[2] == game_board[5] == game_board[8] or
            game_board[0] == game_board[4] == game_board[8] or
            game_board[2] == game_board[4] == game_board[6])

def display_game_board(game_board):
    print()
    print(f"{game_board[0]}|{game_board[1]}|{game_board[2]}")
    print('-+-+-')
    print(f"{game_board[3]}|{game_board[4]}|{game_board[5]}")
    print('-+-+-')
    print(f"{game_board[6]}|{game_board[7]}|{game_board[8]}")
    print()

def display_board():
    game_board = []
    for square in range(9):
        game_board.append(square + 1)
    return game_board

def draw(game_board):
    for square in range(9):
        if game_board[square] != "x" and game_board[square] != "o":
            return False
    return True

if __name__ == "__main__":
    main()