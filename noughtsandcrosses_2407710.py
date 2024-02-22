import random
import json
random.seed()

def draw_board(board):
    # develop code to draw the board
    print("-------------")
    print("|" + " " + board[0][0] + " " + "|" + " " + board[0][1] + " " + "|" + " " + board[0][2] + " " + "|")
    print("-------------")
    print("|" + " " + board[1][0] + " " + "|" + " " + board[1][1] + " " + "|" + " " + board[1][2] + " " + "|")
    print("-------------")
    print("|" + " " + board[2][0] + " " + "|" + " " + board[2][1] + " " + "|" + " " + board[2][2] + " " + "|")
    print("-------------")
    

def welcome(board):
    # prints the welcome message
    print('Welcome to the "Unbeatble Noughts and Crosses" game. \n The board layout is shown below:')
    # display the board by calling draw_board(board)
    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want.")

    

def initialise_board(board):
    # develop code to set all elements of the board to one space 
    for a in range(3):
        for b in range(3):
            board[a][b]= ' '
    return board
    
def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    while True:
        player_move = input("choose your square \n 1 2 3 \n 4 5 6 \n 7 8 9 : ")
        if player_move in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            player_move = int(player_move) - 1
            if board[int(player_move / 3)][player_move % 3] == ' ':
                return int(player_move / 3), player_move % 3
            else:
                print("This cell is already occupied. Please choose a different cell.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")
    return row, col# and return row and col
 
    

def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    
    valuevalid = True
    while valuevalid:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            valuevalid = False
    return row, col # and return row and col
    


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
  
    if (board[0][0] == mark and board[0][1] == mark and board[0][2] == mark) or \
        (board[1][0] == mark and board[1][1] == mark and board[1][2] == mark) or \
        (board[2][0] == mark and board[2][1] == mark and board[2][2] == mark) or \
        (board[0][0] == mark and board[1][0] == mark and board[2][0] == mark) or \
        (board[0][1] == mark and board[1][1] == mark and board[2][1] == mark) or \
        (board[0][2] == mark and board[1][2] == mark and board[2][2] == mark) or \
        (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark) or \
        (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark):
        return True
    else:
        return False   # return True if someone won, False otherwise
    

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True  # return True if it is, False otherwise
        
def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    board = initialise_board(board)
    # then draw the board
    draw_board(board)
    # then in a loop, get the player move, update and draw the board
    while True:
        print("Your Turn to play")
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)
         # check if the player has won by calling check_for_win(board, mark),
        if check_for_win(board, 'X'):
            # if so, return 1 for the score
            return 1
        # if not check for a draw by calling check_for_draw(board)
        elif check_for_draw(board):
            # if drawn, return 0 for the score
            return 0
        # if not, then call choose_computer_move(board)
        # to choose a move for the computer
        row, col = choose_computer_move(board)
        # update and draw the board
        board[row][col] = 'O'
        draw_board(board)
        # check if the computer has won by calling check_for_win(board, mark),
        if check_for_win(board, 'O'):
            # if so, return -1 for the score
            return -1
        # if not check for a draw by calling check_for_draw(board)
        elif check_for_draw(board):
        # if drawn, return 0 for the score
         return 0
                    
                
def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    print("\nEnter one of the following options")
    print("1. Play the game")
    print("2. Save score in leaderboard")
    print("3. Load and display the scores from the leaderboard.txt")
    print("q. End the program")
    choice = input("Enter your choice: ")
    return choice

def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    try:
        # open the file in read mode
        with open("leaderboard.txt", "r") as file:
            leaderboard = json.load(file)
    except:
        # if the file doesn't exist, create a new dictionary
        leaderboard = {}
    
    return leaderboard
    
def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    player_name = input("Enter your name: ")
    try:
        with open("leaderboard.txt", "r") as file:
            data = json.load(file)
    except:
        data = {}
    data[player_name] = score
    with open("leaderboard.txt", "w") as file:
        json.dump(data, file)

    return


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # ed in the Python dictionary parameter leader
    print("----Leaderboard----")
    for name, score in leaders.items():
        print(f"{name}: {score}")

    

