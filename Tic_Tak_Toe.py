board = [ 
[ "" , "" , "" ],
[ "" , "" , "" ],
[ "" , "" , "" ]
]

turn_counter = 0
numbers = []


def match(x, y ,z):
    return x == y == z


def draw_board(bo):
    for i in range(len(bo)):
        if i != 0:
            print("-----------")

        for j in range(len(bo[0])):
            if j != 0:
                print("|", end="")

            if j == 2:
                print(f"{bo[i][j]:^3}")
            else:
                print(f"{bo[i][j]:^3}", end="")
        
def update_board(x, turn):
    if (turn % 2 == 0 ):
        marker = "X"
    else:
        marker = "O"
    x -= 1
    board_x = x // 3
    board_y = x % 3
    board[board_x][board_y] = marker


def get_loc(turn_counter):
    if (turn_counter % 2 == 0 ):
        player = "X"
    else:
        player = "O"
    player_input = input( f"{player} Where would you like to go? ")
    while not player_input.isnumeric() or int(player_input ) in numbers or not( 1 <= int(player_input) <= 9):
        print("Your input is invalid")
        player_input = input( f"{player} Where would you like to go? ")
    x =  int(player_input)
    numbers.append(x)
    print(numbers)
    return x

def reset_board(bo):
    for idx, i in enumerate(bo):
        for j in range(len(i)):
            bo[idx][j] = ""
    numbers.clear()        

def check_row():
    for i in range(len(board)):
        triplet = (board[i][0], board[i][1], board[i][2])
        if all(triplet) and match(*triplet):
            return True
    return False

def check_col():
    for i in range(len(board)):
        triplet = (board[0][i], board[1][i], board[2][i])
        if all(triplet) and match(*triplet):
            return True
    return False

def check_cross():
    triplet = (board[0][0], board[1][1], board[2][2])
    triplet2 = (board[0][2], board[1][1], board[2][0])

    if all(triplet) and match(*triplet):
        return True
    if all(triplet2) and match(*triplet2):
        return True
    else:
        return False
    



def run_game():
    turn_counter = 0
    reset_board(board)
    draw_board(board)

    while(check_cross() == False and check_col() == False and check_row() == False):
        
        x = get_loc(turn_counter)
        update_board(x, turn_counter)
        draw_board(board)
        turn_counter += 1

    if (turn_counter % 2 == 0):
        print("O You Are the Winner!!!")
    else:
        print("X You Are the Winner!!!")


def main():
    z = "yes"
    while z.lower() == "yes":
        run_game()
        z = input("Would you like to play again? ")
    print("Goodbye")

if __name__ == "__main__":
    main()


