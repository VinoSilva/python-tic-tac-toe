import util

grid_size : int = int(input("What is the grid size:")) 

grid_size = grid_size if grid_size >= 3 else 3

def create_board(grid_size):
    ls = [];

    for i in range(grid_size):
        nested_ls = []

        for m in range(grid_size):
            nested_ls.append("0")

        ls.append(nested_ls)

    return ls

def print_board(board):
    def print_horizontal_line(size):
        text = " "

        for i in range(size):
            text += "--- "
            
        print(text)

    number_letter_map = {
        "1": "X",
        "2": "O",
        "0": " "
    }

    board_size = len(board)

    for row_index,row in enumerate(board):
        text = ""
        print_horizontal_line(board_size)
        for column_index,column in enumerate(row):
            if column_index == 0:
                text += "|"

            text += f" {number_letter_map[column]} |"

        print(text)
    print_horizontal_line(board_size)

def check_winner(board):
    n = len(board)  # Determine the size of the board

    number_to_letter_map = {
        "0": " ",
        "1": "X",
        "2": "O"
    }

    # Check rows
    for row in board:
        if all(cell == row[0] and cell != '' for cell in row):
            return number_to_letter_map[row[0]]

    # Check columns
    for col in range(n):
        if all(board[row][col] == board[0][col] and board[row][col] != '' for row in range(n)):
            return number_to_letter_map[board[0][col]]

    # Check main diagonal (top-left to bottom-right)
    if all(board[i][i] == board[0][0] and board[i][i] != '' for i in range(n)):
        return number_to_letter_map[board[0][0]]

    # Check anti-diagonal (top-right to bottom-left)
    if all(board[i][n - i - 1] == board[0][n - 1] and board[i][n - i - 1] != '' for i in range(n)):
        return number_to_letter_map[board[0][n - 1]]

    return number_to_letter_map["0"]

def set_board_value(board,choice,player):
    row = int(choice.split(",")[0])
    column = int(choice.split(",")[1])

    if(board[row][column] == "0"):
        board[row][column] = player
        return True
    else:
        return True

board = create_board(grid_size)
print_board(board)

cont = "y"

while(cont == "y"):
    player_turn = "1"
    winner = " "
    board = create_board(grid_size)

    while(winner == " "):
        util.cls()
        print_board(board)
        choice = input(f"Player {player_turn} What row and column do you choose? row,column:")

        if(not set_board_value(board,choice,player_turn)):
            print("Wrong spot!")
            util.pause()

        winner = check_winner(board)

        if winner == " ":
            if(player_turn == "1"):
                player_turn = "2"
            else:
                player_turn = "1" 

    util.cls()
    print_board(board)
    print(f"Winner is player {player_turn}")
    cont = input("Do you want to continue? (y for yes)")
