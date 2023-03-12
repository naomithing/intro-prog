import random
import os.path
import json
random.seed()


def draw_board(board): #prints the board
    print(' ----------')
    print('|', board[0][0], '|', board[0][1], '|', board[0][2], '|')
    print(' ----------')
    print('|', board[1][0], '|', board[1][1], '|', board[1][2], '|')
    print(' ----------')
    print('|', board[2][0], '|', board[2][1], '|', board[2][2], '|')
    print(' -----------')
    pass


def wlcmsg(board): # prints the welcome message
    print("Welcome to the 'Unbeatable Noughts and Crosses' game.")
    draw_board(board) # display the board by calling draw_board(board)
    pass


def initiate_board(board):  #sets all elements of the board to one space ' '
    for i in range(3):
        for x in range(3):
            board[i][x] = ' '
    return board


def player_move(board): # asks the user to put the X in the cell
    # and return row and col
    print("Your choices are")
    print('1 2 3 \n4 5 6 \n7 8 9')
    choice = int(input("Choose a number "))
    if choice == 1:
        row = 0
        col = 0
    elif choice == 2:
        row = 0
        col = 1
    elif choice == 3:
        row = 0
        col = 2
    elif choice == 4:
        row = 1
        col = 0
    elif choice == 5:
        row = 1
        col = 1
    elif choice == 6:
        row = 1
        col = 2
    elif choice == 7:
        row = 2
        col = 0
    elif choice == 8:
        row = 2
        col = 1
    elif choice == 9:
        row = 2
        col = 2
    while board[row][col] != ' ':
        print("The space is already taken.")
        choice = int(input("Insert a number: "))
        if choice == 1:
            row = 0
            col = 0
        elif choice == 2:
            row = 0
            col = 1
        elif choice == 3:
            row = 0
            col = 2
        elif choice == 4:
            row = 1
            col = 0
        elif choice == 5:
            row = 1
            col = 1
        elif choice == 6:
            row = 1
            col = 2
        elif choice == 7:
            row = 2
            col = 0
        elif choice == 8:
            row = 2
            col = 1
        elif choice == 9:
            row = 2
            col = 2
    return row, col


def computer_move(board): # lets the computer put the O in the cell
    # and return row and col
    list_of_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    choice = random.choice(list_of_choices)
    if choice == 1:
        row = 0
        col = 0
    elif choice == 2:
        row = 0
        col = 1
    elif choice == 3:
        row = 0
        col = 2
    elif choice == 4:
        row = 1
        col = 0
    elif choice == 5:
        row = 1
        col = 1
    elif choice == 6:
        row = 1
        col = 2
    elif choice == 7:
        row = 2
        col = 0
    elif choice == 8:
        row = 2
        col = 1
    elif choice == 9:
        row = 2
        col = 2
    while board[row][col] != ' ':
        choice = random.choice(list_of_choices)
        if choice == 1:
            row = 0
            col = 0
        elif choice == 2:
            row = 0
            col = 1
        elif choice == 3:
            row = 0
            col = 2
        elif choice == 4:
            row = 1
            col = 0
        elif choice == 5:
            row = 1
            col = 1
        elif choice == 6:
            row = 1
            col = 2
        elif choice == 7:
            row = 2
            col = 0
        elif choice == 8:
            row = 2
            col = 1
        elif choice == 9:
            row = 2
            col = 2
    return row, col


def is_victory(board, mark): # checks who won among the player or computer
    # return True if one of them won, False otherwise
    if board[0][0] == mark and board[0][1] == mark and board[0][2] == mark:
        return True
    elif board[1][0] == mark and board[1][1] == mark and board[1][2] == mark:
        return True
    elif board[2][0] == mark and board[2][1] == mark and board[2][2] == mark:
        return True
    elif board[0][0] == mark and board[1][0] == mark and board[2][0] == mark:
        return True
    elif board[0][1] == mark and board[1][1] == mark and board[2][1] == mark:
        return True
    elif board[0][2] == mark and board[1][2] == mark and board[2][2] == mark:
        return True
    elif board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    elif board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    return False


def is_draw(board): #checks if it is tie between player and computer
    # return True if it is, False otherwise
    for x in range(3):
        for i in range(3):
            if board[x][i] == ' ':
                return False
    return True


def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    # then draw the board
    # then in a loop, get the player move, update and draw the board
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # repeat the loop
    board = initiate_board(board)
    draw_board(board)

    while True:
        row, col = player_move(board)
        board[row][col] = 'X'
        draw_board(board)
        if is_victory(board, 'X'):
            return 1
        if is_draw(board):
            return 0

        row, col = computer_move(board)
        board[row][col] = 'O'
        draw_board(board)
        if is_victory(board, 'O'):
            return -1
        if is_draw(board):
            return 0


def menu():
    # get user input of either 'P', 'S', 'D' or 'Q'
    # P - Play the game
    # S - Save score in file 'leaderboard.txt'
    # D - Load and display the scores from the 'leaderboard.txt'
    # Q - End the program
    print("Your choices are as follows: ")
    print("P for Play game, S for save score, D for display scores, Q to quit")
    choice = input("Enter your choice: ")
    return choice


def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    leaders = {}
    with open("leaderboard.txt", 'r') as f:
        for line in f:
            (key, val) = line.split()
            leaders[key] = val
    return leaders


def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    player_name = input("Enter your name")
    with open("leaderboard.txt", 'a') as f:
        f.write(player_name + " " + str(score) + "\n")
    return


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    print("\n\n\t\tLEADERBOARD\n")
    print("\tName\t\tScore")
    print("\t----\t\t-----")
    for name, score in leaders.items():
        print("\t{}\t\t{}".format(name, score))
    pass


def main():
    board = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]

    wlcmsg(board)
    total_score = 0
    while True:
        choice = menu()
        if choice == 'P':
            score = play_game(board)
            total_score += score
            print('Your current score is: ', total_score)
        if choice == 'S':
            save_score(total_score)
        if choice == 'D':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'Q':
            print('Hope you enjoyed the noughtsandcrosses :)')
            print('Bye-Bye!')
            return


if __name__ == '__main__':
    main()
