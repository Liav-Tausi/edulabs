from E2_api_trivia_back import *


if __name__ == "__main__":
    trivia_battle: TriviaBattle = TriviaBattle("https://opentdb.com/api.php?", 20)
    battle = Battle("Player one", "Player two", trivia_battle, 5)

    min_points = len(battle.display_content["results"]) // 2 + 1
    rounds_played = 0

    while True:
        rounds_played += 1

        battle.prompt_for_answer(battle.player_one)
        if battle.win_counter[battle.player_one] >= min_points:
            print(battle.is_win())
            break
        battle.prompt_for_answer(battle.player_two)
        if battle.win_counter[battle.player_two] >= min_points:
            print(battle.is_win())
            break

        if rounds_played >= battle.best_of:
            break


    print(battle.display_score())
