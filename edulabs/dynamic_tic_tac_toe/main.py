from game import *
from datetime import datetime


# creator: liav tausi
# date: 2022/12/02

# this is my sizable dynamic tic-tac-toe game!
# built by liav "creator" as part of learning python in EduLabs College


if __name__ == "__main__":

    while True:
        gretting()
        names: list = name_func()
        already_been = list()
        turn: list[int] = [0]
        final_grid: list = game_layout(names)
        board = list_build(int(final_grid[0]))
        win_grid = {
            "row": [0] * int(final_grid[0]),
            "column": [0] * int(final_grid[0]),
            "diagonal": [0, 0]
        }
        start_time = datetime.now()
        while True:
            player = user_input(board, names, turn, int(final_grid[0]), already_been)
            display(int(final_grid[0]), board)
            update_win(win_board=win_grid, player=player, grid_size=int(final_grid[0]))
            win = check_win(win_board=win_grid, grid_size=int(final_grid[0]),turn=turn[0], player=player_num(player))
            if win is True:
                print(f"{names[turn[0] % 1].upper()} is the winner!")
                end_time = datetime.now()
                print("game time:", (end_time - start_time))
                break
            else:
                if win == "Draw!":
                    end_time = datetime.now()
                    print("game time:", (end_time - start_time))
                    break
                else:
                    pass
        start_again = input("Do you want to play another game? yes/no:").lower()
        if start_again == "yes":
            while start_again not in ["yes","no"]:
                start_again = input("\033[0;31;1mTry Again!\033 yes/no :").lower()
            continue
        break


