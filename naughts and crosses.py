import random

board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]  # creates board


def viewboard():
    row1 = board[0]
    row2 = board[1]
    row3 = board[2]
    print("\n", row1, "\n", row2, "\n", row3)  # outputs the board in a user friendly way


match3 = False
draw = False
used_positions = 0

print("#######################")
print("welcome to tik tack toe")
print("match 3 horozontally, diagonally or vertically to win.")
print("You are X the computer is ~.")
print("#######################")  # intro / instructions


def player_move():
    z = input("where would you like to move? enter row number then column number both numbers separated by a space: ")
    choice = z.split(" ")  # splits users co-ords into a list of row and column
    row = int(choice[0])
    column = int(choice[1])
    check_space(row, column, "p")  # checks if users choice is clear


def check_space(row, column, person):
    global used_positions
    if board[row][column] == "-":

        used_positions += 1

        if person == "p":
            board[row][column] = "X"  # when position is clear enter x
            viewboard()

        if person == "c":
            board[row][column] = "~"  # when position is clear enter ~
            viewboard()




    else:
        if person == "p":
            player_move()
        if person == "c":
            computer_move()


def computer_move():
    row = random.randint(0, 2)
    column = random.randint(0,
                            2)  # generates random row and column for computer not effecient ####might need to patch in future
    check_space(row, column, "c")


checker = ""


def win(person):
    global checker
    global match3
    if person == "p":
        checker = "X"

    if person == "c":
        checker = "~"

    if board[0][0] == checker and board[0][1] == checker and board[0][2] == checker:  # checks top line
        print(" the winner is ", person)
        match3 = True

    if board[1][0] == checker and board[1][1] == checker and board[1][2] == checker:  # checks mid line
        print(" the winner is ", person)
        match3 = True
    if board[2][0] == checker and board[2][1] == checker and board[2][2] == checker:  # checks bottom line
        print(" the winner is ", person)
        match3 = True

    if board[0][0] == checker and board[1][0] == checker and board[2][0] == checker:  # checks first column
        print(" the winner is ", person)
        match3 = True
    if board[1][0] == checker and board[1][1] == checker and board[1][2] == checker:  # checks mid column
        print(" the winner is ", person)
        match3 = True
    if board[2][0] == checker and board[2][1] == checker and board[2][2] == checker:  # checks last column
        print(" the winner is ", person)
        match3 = True

    if board[0][0] == checker and board[1][1] == checker and board[2][2] == checker:  # checks diagonal y=-x
        print(" the winner is ", person)
        match3 = True

    if board[2][0] == checker and board[1][1] == checker and board[0][2] == checker:  # checks diagonal y = x
        print(" the winner is ", person)
        match3 = True


while used_positions <= 9:
    player_move()
    win("p")
    if match3 == True:
        break;
    computer_move()
    win("c")
    if match3 == True:
        break;
