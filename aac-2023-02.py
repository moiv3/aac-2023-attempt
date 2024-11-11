import argparse

# config
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def read_txt(file_path):
    with open(file_path, "r") as f:
        all_lines = f.read().splitlines()
        return all_lines
    
def judge_feasible_game(games):
    passed_games = []
    all_game_prod = []
    for game in games:
        game_no = game.split(":")[0].split("Game ")[1]
        print(game_no)
        game_detail = game.split(":")[1].split(";")
        print(game_detail)

        break_counter = False

        max_ball_dict = {'red': 0,
                         'green': 0,
                         'blue': 0}
        for trial in game_detail:
            trial_dict = {}
            for i, j in enumerate(trial.split(" ")):
                if i == 0:
                    pass
                elif i % 2 == 0:
                    trial_dict[j.split(",")[0]] = int(trial.split(" ")[i-1])
            print(trial_dict)

            if ('red' in trial_dict and trial_dict['red'] > MAX_RED) or ('green' in trial_dict and trial_dict['green'] > MAX_GREEN) or ('blue' in trial_dict and trial_dict['blue'] > MAX_BLUE):
                break_counter = True

            for color in ['red', 'green', 'blue']:
                if color in trial_dict:
                    max_ball_dict[color] = max(trial_dict[color], max_ball_dict[color])

        if not break_counter:
            # print(f"{game_no} passed")
            passed_games.append(int(game_no))

        print(f"max_ball_dict: {max_ball_dict}, {max_ball_dict.values()}")

        game_prod = 1
        for value in max_ball_dict.values():
            if value > 0:
                game_prod *= value
        print(game_prod)
        all_game_prod.append(game_prod)

    # print(passed_games)
    print(all_game_prod)
    return sum(passed_games), sum(all_game_prod)


if __name__ == "__main__":
    print("Starting script for aac-2023-2")
    parser = argparse.ArgumentParser(description="Process a text file.")
    parser.add_argument("file", help="Path to the input .txt file")
    args = parser.parse_args()
    input_list = read_txt(args.file)
    result1, result2 = judge_feasible_game(input_list)
    print(f"Result 1: {result1}, result 2: {result2}")


    