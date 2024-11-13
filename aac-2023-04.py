import argparse

def read_text(file_path):
    with open(file_path, "r") as fp:
        return fp.read().splitlines()
    
def parse_one_game(string):
    result1 = string.split(":")
    game_no = result1[0].split(" ")[-1]
    print(result1[0])
    result2 = result1[1].split("|")
    winning_nums = result2[0].split(" ")
    winning_nums = [num for num in winning_nums if num]
    your_nums = result2[1].split(" ")
    your_nums = [num for num in your_nums if num]
    print(winning_nums, your_nums)
    matches = 0
    for num in your_nums:
        if num in winning_nums:
            matches += 1
    print(matches)
    return game_no, matches

def parse_all_games(input_list):
    total_score = 0
    match_dict = {}
    for game in input_list:
        game_no, matches = parse_one_game(game)
        if matches > 0:
            game_score = 2 ** (matches - 1)
        else:
            game_score = 0
        total_score += game_score

        match_dict[int(game_no)] = matches
    return total_score, match_dict

def get_dupe_cards(input_dict):
    card_qty_dict = {}
    for i in input_dict:
        card_qty_dict[i] = 1
    print(card_qty_dict)
    for i in input_dict:
        for j in range(1,input_dict[i]+1):
            card_qty_dict[i+j] += card_qty_dict[i]
        print(card_qty_dict)
    return card_qty_dict

if __name__ == "__main__":
    print("Starting script for aac-2023-4")
    parser = argparse.ArgumentParser(description="A")
    parser.add_argument("file", help="Path to .txt")
    args = parser.parse_args()
    input_list = read_text(args.file)
    print(input_list)
    total_score, match_dict = parse_all_games(input_list)
    print(total_score)
    print(match_dict)
    card_qty_dict = get_dupe_cards(match_dict)
    print(sum(card_qty_dict.values()))