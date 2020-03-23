
print("Welcome to tic-tac-toe! 1 players, or 2?")
choice = int(input("> "))

loop = True

Matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_board(Matrix):
    print("  " + str(Matrix[0]) + "  |   " + str(Matrix[1]) + "  |  " + str(Matrix[2]) + "\n"
         "------------------\n"
         "  " + str(Matrix[3]) + "  |   " + str(Matrix[4]) + "  |  " + str(Matrix[5]) + "\n"
         "------------------\n"
         "  " + str(Matrix[6]) + "  |   " + str(Matrix[7]) + "  |  " + str(Matrix[8]) + "\n")
    return Matrix

def win_check(Matrix):
    if (Matrix[0] == "X" and Matrix[1] == "X" and Matrix[2] == "X") or (Matrix[0] == "O" and Matrix[1] == "O" and Matrix[2] == "O"):
        loop = False
        print("case 1")
    elif (Matrix[3] == "X" and Matrix[4] == "X" and Matrix[5] == "X") or (Matrix[3] == "O" and Matrix[4] == "O" and Matrix[5] == "O"):
        loop = False
        print("case 2")
    elif (Matrix[6] == "X" and Matrix[7] == "X" and Matrix[8] == "X") or (Matrix[6] == "O" and Matrix[7] == "O" and Matrix[8] == "O"):
        loop = False
        print("case 3")

    elif (Matrix[0] == "X" and Matrix[3] == "X" and Matrix[6] == "X") or (Matrix[0] == "O" and Matrix[3] == "O" and Matrix[6] == "O"):
        loop = False
        print("case 4")
    elif (Matrix[1] == "X" and Matrix[4] == "X" and Matrix[7] == "X") or (Matrix[1] == "O" and Matrix[4] == "O" and Matrix[7] == "O"):
        loop = False
        print("case 5")
    elif (Matrix[2] == "X" and Matrix[5] == "X" and Matrix[8] == "X") or (Matrix[2] == "O" and Matrix[5] == "O" and Matrix[8] == "O"):
        loop = False
        print("case 6")

    elif (Matrix[0] == "X" and Matrix[4] == "X" and Matrix[8] == "X") or (Matrix[0] == "O" and Matrix[4] == "O" and Matrix[8] == "O"):
        loop = False
        print("case 7")
    elif (Matrix[6] == "X" and Matrix[4] == "X" and Matrix[2] == "X") or (Matrix[6] == "O" and Matrix[4] == "O" and Matrix[2] == "O"):
        loop = False
        print("case 8")
    else:
        loop = True
    return loop

while loop:
    print("Player 1's turn!")
    Matrix = print_board(Matrix)
    choice = int(input("> "))
    Matrix[choice-1] = "X"
    print_board(Matrix)
    loop = win_check(Matrix)
    if loop == False:
        print_board(Matrix)
        print("Player 1 wins!")

    if loop:
        print("Player 2's turn!")
        Matrix = print_board(Matrix)
        choice = int(input("> "))
        Matrix[choice - 1] = "O"
        loop = win_check(Matrix)
        if loop == False:
            print_board(Matrix)
            print("Player 2 wins!")
    else:
        pass




