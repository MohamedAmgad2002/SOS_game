import os
import shutil
import random


def game():
    global player_one_score, player_two_score, board, grid
    # to make terminal clean

    def clearConsole():
        command = "clear"
        if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
            command = "cls"
        os.system(command)

    # make the grid of rows and columns
    board = [["¦   ¦" for a in range(4)] for b in range(4)]
    grid = [i for i in range(4)]

    # declare scores of the two players and their names
    player_one_score = 0
    player_two_score = 0
    p1 = input("Player one please enter your name: ").capitalize()
    p2 = input("Player two please enter your name: ").capitalize()
    players = [p1, p2]

    # choose randomly who will begin
    choice = random.choice(players)
    if choice == p1:
        p1 = p1
        p2 = p2
    else:
        temp = p1
        p1 = p2
        p2 = temp

    def display_board():
        # numbering horizontal for column
        print("\n")
        for i in grid:
            print(f"    {i} ", end="")
            if i == 3:
                print("\n")

        # form the table shape
        x = 0
        for i in board:
            print("   ---   ---   ---   ---")
            print(x, " ".join(i))
            print("   ---   ---   ---   ---")
            x += 1
        print(f"{p1}: {player_one_score}", f"{p2}: {player_two_score}", sep="        ")

    # check is row and column are right or not
    def check_input(row, column):
        clearConsole()
        if (row < 4 and row >= 0) and (column < 4 and column >= 0):
            # check if index is empty or not
            if board[row][column] != "¦ S ¦" and board[row][column] != "¦ O ¦":
                board[row][column] = "¦ " + character.upper() + " ¦"
                display_board()
                return
            else:
                display_board()
                print("this place is not empty")
                row, column = map(int, input("Please enter row then column: "))
                check_input(row, column)
                return
        else:
            print("Invalid input")
            row, column = map(int, input("Please enter row then column: "))
            check_input(row, column)
            return

    # list to prevent repatation calculation of points to any one of the two
    # players
    horizontal = [0, 1, 2, 3]

    # check if there are any sos in any horizontal row or not
    def check_horizontal(player, previous):
        global player_one_score, player_two_score, count
        # if it is player one
        if player == 1:
            for i in range(4):
                for j in range(2):
                    if (
                        board[i][j] == "¦ S ¦"
                        and board[i][j + 2] == "¦ S ¦"
                        and board[i][j + 1] == "¦ O ¦"
                    ):
                        if i in previous:
                            previous.remove(i)
                            player_one_score += 1
                            clearConsole()
                            display_board()
                            # take another turn
                            player_one_inputs()
                            return player_one_score
                        else:
                            continue
        # if it is player two
        elif player == 2:
            for i in range(4):
                for j in range(2):
                    if (
                        board[i][j] == "¦ S ¦"
                        and board[i][j + 2] == "¦ S ¦"
                        and board[i][j + 1] == "¦ O ¦"
                    ):
                        if i in previous:
                            previous.remove(i)
                            player_two_score += 1
                            clearConsole()
                            display_board()
                            # take another turn
                            player_two_inputs()
                            return player_two_score
                        else:
                            continue

    # list to prevent repatation calculation of points to any one of the two
    # players
    vertical = [0, 1, 2, 3]

    # check if there are any sos in any vertical column or not
    def check_vertical(player, previous):
        global player_one_score, player_two_score, count
        # if it is player 1
        if player == 1:
            for j in range(4):
                for i in range(2):
                    if (
                        board[i][j] == "¦ S ¦"
                        and board[i + 2][j] == "¦ S ¦"
                        and board[i + 1][j] == "¦ O ¦"
                    ):
                        if j in previous:
                            previous.remove(j)
                            player_one_score += 1
                            clearConsole()
                            display_board()
                            # take another turn
                            player_one_inputs()
                            return player_one_score
                        else:
                            continue
        # if it is player 2
        elif player == 2:
            for j in range(4):
                for i in range(2):
                    if (
                        board[i][j] == "¦ S ¦"
                        and board[i + 2][j] == "¦ S ¦"
                        and board[i + 1][j] == "¦ O ¦"
                    ):
                        if j in previous:
                            previous.remove(j)
                            player_two_score += 1
                            clearConsole()
                            display_board()
                            # take another turn
                            player_two_inputs()
                            return player_two_score
                        else:
                            continue

    # list to add state at which sos formed to prevent repetation
    l_oblique = []

    def check_left_oblique(player, previous):
        global player_one_score, player_two_score, count
        # if it is player 1
        if player == 1:
            for i in range(2):
                for j in range(2):
                    if (
                        board[i][j] == "¦ S ¦"
                        and board[i + 2][j + 2] == "¦ S ¦"
                        and board[i + 1][j + 1] == "¦ O ¦"
                    ):
                        cordinate = str(i) + str(j)
                        if cordinate not in previous:
                            previous.append(cordinate)
                            player_one_score += 1
                            clearConsole()
                            display_board()
                            # take another turn
                            player_one_inputs()
                            return player_one_score
                        else:
                            continue

        # if it is player 2
        elif player == 2:
            for i in range(2):
                for j in range(2):
                    if (
                        board[i][j] == "¦ S ¦"
                        and board[i + 2][j + 2] == "¦ S ¦"
                        and board[i + 1][j + 1] == "¦ O ¦"
                    ):
                        cordinate = str(i) + str(j)
                        if cordinate not in previous:
                            previous.append(cordinate)
                            player_two_score += 1
                            clearConsole()
                            display_board()
                            # take another turn
                            player_two_inputs()
                            return player_two_score
                        else:
                            continue

    # list to add state at which sos formed to prevent repetation
    r_oblique = []

    def check_right_oblique(player, previous):
        global player_one_score, player_two_score, count
        # if it is player 1
        if player == 1:
            for i in range(2):
                for j in range(3, 1, -1):
                    if (
                        board[i][j] == "¦ S ¦"
                        and board[i + 2][j - 2] == "¦ S ¦"
                        and board[i + 1][j - 1] == "¦ O ¦"
                    ):
                        cordinate = str(i) + str(j)
                        if cordinate not in previous:
                            previous.append(cordinate)
                            player_one_score += 1
                            clearConsole()
                            display_board()
                            # take another turn
                            player_one_inputs()
                            return player_one_score
                        else:
                            continue
        # if it is player 2
        elif player == 2:
            for i in range(2):
                for j in range(3, 1, -1):
                    if (
                        board[i][j] == "¦ S ¦"
                        and board[i + 2][j - 2] == "¦ S ¦"
                        and board[i + 1][j - 1] == "¦ O ¦"
                    ):
                        cordinate = str(i) + str(j)
                        if cordinate not in previous:
                            previous.append(cordinate)
                            player_two_score += 1
                            clearConsole()
                            display_board()
                            # take another turn
                            player_two_inputs()
                            return player_two_score
                        else:
                            continue

    def player_one_inputs():
        global character, count
        # increment counter
        count += 1
        # to stop game when board is full
        if count <= 16:
            # take character that the player will play
            character = input(f"\n{p1} Please enter 'S' or 'O': ")
            if character.lower() == "s" or character.lower() == "o":
                # to prevent player from entering space between inputs or any
                # other character
                try:
                    row, column = map(
                        int,
                        input(
                            f"{p1} Please enter row then column without space between them: "
                        ),
                    )
                    check_input(row, column)
                    player = 1
                    check_horizontal(player, horizontal)
                    check_vertical(player, vertical)
                    check_right_oblique(player, r_oblique)
                    check_left_oblique(player, l_oblique)
                except ValueError:
                    print("invalid input please enter numbers only")
                    row, column = map(
                        int,
                        input(
                            f"{p1} Please enter row then column without space between them: "
                        ),
                    )
                    check_input(row, column)
                    player = 1
                    check_horizontal(player, horizontal)
                    check_vertical(player, vertical)
                    check_right_oblique(player, r_oblique)
                    check_left_oblique(player, l_oblique)
            else:
                print("Invalid input please enter 'S' or 'O'")
                player_one_inputs()
        else:
            return

    def player_two_inputs():
        global character, count
        # increment counter with one
        count += 1
        # to stop game when board is completely filled
        if count <= 16:
            # take character from player
            character = input(f"\n{p2} please enter 'S' or 'O': ")
            if character.lower() == "s" or character.lower() == "o":
                # to prevent player from entering space or any other character
                try:
                    row, column = map(
                        int,
                        input(
                            f"{p2} Please enter row then column without space between them: "
                        ),
                    )
                    check_input(row, column)
                    player = 2
                    check_horizontal(player, horizontal)
                    check_vertical(player, vertical)
                    check_right_oblique(player, r_oblique)
                    check_left_oblique(player, l_oblique)
                except ValueError:
                    print("invalid input please enter numbers only")
                    row, column = map(
                        int,
                        input(
                            f"{p2} Please enter row then column without space between them: "
                        ),
                    )
                    check_input(row, column)
                    player = 2
                    check_horizontal(player, horizontal)
                    check_vertical(player, vertical)
                    check_right_oblique(player, r_oblique)
                    check_left_oblique(player, l_oblique)
            else:
                print("Invalid input please enter 'S' or 'O'")
                player_two_inputs()
        else:
            return

    def main():
        global count
        # start game with counter zero
        count = 0
        while True:
            clearConsole()
            display_board()
            player_one_inputs()
            # if all places filled then stop the game
            if count == 16:
                break
            clearConsole()
            display_board()
            player_two_inputs()
            if count == 16:
                break
        # declare who win else the game end with drawn
        if player_one_score > player_two_score:
            clearConsole()
            # a command to print in the middle of the screen
            columns = shutil.get_terminal_size().columns
            print(f"Congratulations {p1} for Winning".center(columns))
            descion = input("Do you want to play again [Y/N]".center(columns))
            if descion.lower() == "y":
                game()
            else:
                print("Thank you")
        elif player_one_score < player_two_score:
            clearConsole()
            # a command to print in the middle of the screen
            columns = shutil.get_terminal_size().columns
            print(f"Congratulations {p2} for Winning".center(columns))
            descion = input("Do you want to play again [Y/N]".center(columns))
            if descion.lower() == "y":
                game()
            else:
                print("Thank you")
        else:
            clearConsole()
            # a command to print in the middle of the screen
            columns = shutil.get_terminal_size().columns
            print("No one win".center(columns))
            descion = input("Do you want to play again [Y/N]".center(columns))
            if descion.lower() == "y":
                game()
            else:
                print("Thank you")

    main()


# run game
game()
