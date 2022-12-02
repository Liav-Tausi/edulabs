def player_num(player: list[str,list[str]]) -> int:
    """
    :param player:
    :return: int 1 or -1

     this function takes the symbol of the player and converts it to (1 for x) or (-1 for o)
    """
    if player[0] == 'X':
        return 1
    else:
        return -1


def update_win(win_board: dict[str:list], player: list[str,list[str]], grid_size: int) -> None:
    """
    :param win_board:
    :param player:
    :param grid_size:
    :return: None , it updates the values in win_grid

    # this function converts the coordinates that was inserted by the user to indexes
    # (in the win_grid dict) to row's values and to column's values depended on the index of each one
    # the numbers whether if 1 or -1 cancel each other if on the same row or column
    # same for the two diagonals
    """
    row_inx: int = int(player[1][0]) - 1
    col_inx: int = int(player[1][1]) - 1
    num: int = player_num(player)
    win_board['row'][row_inx] += num
    win_board['column'][col_inx] += num
    if row_inx == col_inx:
        win_board['diagonal'][0] += num
    if row_inx + col_inx == grid_size - 1:
        win_board['diagonal'][1] += num


def check_win(win_board: dict, grid_size: int, turn: int, player) -> bool | str:
    """
    :param win_board:
    :param grid_size:
    :param turn:
    :return: bool if win or no win | str if draw

    this function checks whether if the sum of etch row or column or diagonal retches the grid_size
    if yes it's a win if not it's whether a draw or no win yet
    """
    num = player * grid_size
    for i in win_board["row"]:
        if i == num:
            return True
    for j in win_board["column"]:
        if j == num:
            return True
    for g in win_board["diagonal"]:
        if g == num:
            return True
    if turn == grid_size ** 2:
        return "Draw!"
    else:
        return False


def display(num: int,built: list) -> None:
    """
    :param num:
    :param built:
    :return: None | displays the lists that store the player symbol

     this function displays the board for the players to choose their next move
    """
    print("\t", end="\t")
    for i in range(num):
        print(f"{i+1}", end="\t\t\t")
    print(" ")
    print()
    for g,row in enumerate(range(num)):
        print(g + 1, end="    ")
        print(f"\t")
        for column in range(num):
            if column == 0:
                print("\t", end=" ")
            else:
                print(f"| ", end=" ")
            print(f"__ {built[row][column]} __", end="  ")
        print(" ")


def list_build(num: int) -> list:
    """
    :param num:
    :return: list | a list that resembles the board

    this function builds the board as a list for ex:
    for board size 3x3 [[" ", " ", " ",][" ", " ", " ",][" ", " ", " ",]]
    """
    board = []*num
    for place in range(num):
        board.append(['_']*num)
    return board




def gretting() -> None:
    """
    :return: None

    this function greets you :)
    """
    print("""\033[0;30;1m
                                 ______   __  __     ______                                                                      
                                /\__  _\ /\ \_\ \   /\  ___\                                                                      
                                \/_/\ \/ \ \  __ \  \ \  __\                                                                      
                                   \ \_\  \ \_\ \_\  \ \_____\                                                                    
                                    \/_/   \/_/\/_/   \/_____/                                                                    
                                                                                                                                  
     ______   __     ______        ______   ______     ______        ______   ______     ______       
    /\__  _\ /\ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\      
    \/_/\ \/ \ \ \  \ \ \____     \/_/\ \/ \ \  __ \  \ \ \____     \/_/\ \/ \ \ \/\ \  \ \  __\      
       \ \_\  \ \_\  \ \_____\       \ \_\  \ \_\ \_\  \ \_____\       \ \_\  \ \_____\  \ \_____\    
        \/_/   \/_/   \/_____/        \/_/   \/_/\/_/   \/_____/        \/_/   \/_____/   \/_____/    
                                                                                                          
            \033[0;31;1m       x  x \033[0;30;1m         ______     ______      __    __     ______   \033[1;34;1m   \      /- \033[0;30;1m                          
            \033[0;31;1m    x        x\033[0;30;1m      /\  ___\    /\  __ \   /\ "-./  \   /\  ___\   \033[1;34;1m   -\   /- \033[0;30;1m              
            \033[0;31;1m   x          x\033[0;30;1m      \ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __ \   \033[1;34;1m    -/-  \033[0;30;1m               
            \033[0;31;1m   x          x\033[0;30;1m       \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\    \033[1;34;1m /- -\ \033[0;30;1m                    
            \033[0;31;1m    x        x\033[0;30;1m         \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/    \033[1;34;1m/-    -\  \033[0;30;1m
            \033[0;31;1m       x  x\033[0;30;1m                                                         \033[1;34;1m -        -   \033[0;30;1m
            \033[0;30;1m 
    """)
    start: str = input("PRESS ANY KEY TO START:  ")



def name_func() -> list[str,str]:
    """
    :return: list | list of names of players

    this function takes and returns the name of the players playing
    """
    name1: str = input("Please Insert Player 1 name: ").lower()
    # input validation
    while not name1.isalpha():
        name1: str = input("\033[0;31;1mTry Again!\033[0;30;0mPlayer 1 name: ").lower()
    name2: str = input("Please Insert Player 2 name: ").lower()
    # input validation
    while not name2.isalpha():
        name2: str = input("\033[0;31;1mTry Again!\033[0;30;0mPlayer 2 name: ").lower()
    return [name1, name2]



def user_input(built_board: list, names: list, turn: list[int], grid_size: int, already_been: list) -> list[str,list[str,str]]:
    """
    :param built_board:
    :param names:
    :param turn:
    :param grid_size:
    :return: list[list[str,list[str,str]]] | list "1" is the symbol of player list and of list 2 that consist the coordinates

    this function takes the user inputted coordinates and depended on the turn assigns the player his symbol
    """
    print(f"\nIt's {names[turn[0] % 2]}'s turn")
    row_col = input("\nInsert numbers of row & column in a %/% format (ex:1/2): ").strip()

    # input validation
    while (row_col in already_been) or (len(row_col) != 3) or (row_col[1] != "/") or (int(row_col[0]) > grid_size) or (int(row_col[2]) > grid_size):
        row_col = input("\n\033[0;31;1mTry Again!\033[0;30;0m row & column in a %/% format: ").strip()
    already_been.append(row_col)
    row_col_split = row_col.split("/")

    # if turn is even X if odd O
    if turn[0] % 2 == 0:
        x_or_o = "X"
    else:
        x_or_o = "O"
    # appending X or O to coordinates in list_build()'s built list (board in main)
    built_board[int(row_col_split[0]) - 1][int(row_col_split[1]) - 1] = x_or_o
    turn[0] += 1
    return [x_or_o, row_col_split]



def game_layout(names_list: list) -> list[str,str]:
    """
    :param names_list:
    :return: list | consist of the parameters of the size of the board

    this function explain the rules to the player and takes the parameters for the size of the board
    """

    print(f"""                                   
                               WELCOME {(names_list[0]).title()} AND {(names_list[1]).title()}
                               
                                 \033[1;34;1mLET'S GET STARTED!\033[0;30;1m 
                         \033[1;34;1mCHOOSE A LAYOUT GRID FROM \033[1;31;1m3X3\033[0;30;1m\033[1;34;1m TO \033[1;31;1m9X9\033[0;30;1m\033[1;34;1m!\033[0;30;1m
 
        FOR REFERENCE: 3X3                                  FOR REFERENCE 9X9
        
           1     2     3                      1     2     3     4     5     6     7     8     9
              |     |                            |     |     |     |     |     |     |     |     
        1  -  |  -  |  -                   1  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  
         _____|_____|_____                  _____|_____|_____|_____|_____|_____|_____|_____|_____
              |     |                            |     |     |     |     |     |     |     |        
        2  -  |  -  |  -       <--->       2  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  
         _____|_____|_____                  _____|_____|_____|_____|_____|_____|_____|_____|_____
              |     |                            |     |     |     |     |     |     |     |     
        3  -  |  -  |  -                   3  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  
              |     |                       _____|_____|_____|_____|_____|_____|_____|_____|_____
                                                 |     |     |     |     |     |     |     |     
           RULES:                          4  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  - 
                                            _____|_____|_____|_____|_____|_____|_____|_____|_____
    Win: complete  a line/diagonal line          |     |     |     |     |     |     |     |     
                                           5  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  
    Draw: no player has won and             _____|_____|_____|_____|_____|_____|_____|_____|_____
    there is no point to keep playing            |     |     |     |     |     |     |     |     
                                           6  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  
                                            _____|_____|_____|_____|_____|_____|_____|_____|_____
                                                 |     |     |     |     |     |     |     |    
                                           7  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  
                                            _____|_____|_____|_____|_____|_____|_____|_____|_____
                                                 |     |     |     |     |     |     |     |     
                                           8  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  
                                            _____|_____|_____|_____|_____|_____|_____|_____|_____
                                                 |     |     |     |     |     |     |     |     
                                           9  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -                                   
\033[0;30;0m""")
    grid: str = input("Insert The Grid Leyout In '#x#' format: ").lower().strip()
    # input validation
    while grid not in ["3x3","4x4","5x5","6x6","7x7","8x8","9x9"]:
        grid: str = input("\033[0;31;1mTry Again!\033[0;30;0m Insert The Grid Leyout In '#x#' format: ").lower().strip()
    final_grid: list = grid.split('x')
    return final_grid



