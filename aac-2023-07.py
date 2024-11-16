import argparse
import pprint

# config
TYPES = 7
TOTAL_HANDS = 1000


def read_list(filepath):
    with open(filepath, "r") as fp:
        return fp.read().splitlines()


def card_order_fn(s):

    card_order = {
        "A": "N",
        "K": "M",
        "Q": "L",
        "J": "K",
        "T": "J",
        "9": "I",
        "8": "H",
        "7": "G",
        "6": "F",
        "5": "E",
        "4": "D",
        "3": "C",
        "2": "B",
    }

    return card_order[s]


def parse_input_list(input_list):

    output_dict = {}
    alpha_dict = {}

    for line in input_list:
        hand = line.split(" ")[0]
        bet = int(line.split(" ")[1])
        alpha = (
            card_order_fn(hand[0])
            + card_order_fn(hand[1])
            + card_order_fn(hand[2])
            + card_order_fn(hand[3])
            + card_order_fn(hand[4])
        )
        output_dict[hand] = {
            "bet": bet,
            "type": 0,
            "rank_in_same_type": 0,
            "rank": 0,
            "alpha": alpha,
        }
        alpha_dict[alpha] = hand

    # pprint.pprint(output_dict)
    return output_dict, alpha_dict


def judge_hand_rank(input_dict):
    for item in input_dict:

        count_dict = {}

        for card in ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]:
            count_dict[card] = item.count(card)
        # input_dict[item]["count"] = count_dict
        # print(count_dict.values())
        # print(sorted(count_dict.values(),reverse=True))

        card_count_lst = sorted(count_dict.values(), reverse=True)

        if card_count_lst[0] == 5:
            input_dict[item]["type"] = 6  # 5 of a kind
        elif card_count_lst[0] == 4:
            input_dict[item]["type"] = 5  # 4 of a kind
        elif card_count_lst[0] == 3 and card_count_lst[1] == 2:
            input_dict[item]["type"] = 4  # Full house
        elif card_count_lst[0] == 3:
            input_dict[item]["type"] = 3  # 3 of a kind
        elif card_count_lst[0] == 2 and card_count_lst[1] == 2:
            input_dict[item]["type"] = 2  # Two pair
        elif card_count_lst[0] == 2:
            input_dict[item]["type"] = 1  # One pair
        else:
            input_dict[item]["type"] = 0  # High card

    return input_dict


def sort_hand_rank(input_dict, alpha_dict):

    for i in range(TYPES):
        temp_list = [
            input_dict[item]["alpha"]
            for item in input_dict
            if input_dict[item]["type"] == i
        ]
        temp_list.sort()
        # print(temp_list)

        for idx, item in enumerate(temp_list):
            input_dict[alpha_dict[item]]["rank_in_same_type"] = idx
    # pprint.pprint(input_dict)
    return input_dict


def get_real_rank(input_dict):

    count_dict = {}
    total_dict = {}

    for i in range(TYPES):
        count_dict[i] = sum(1 for item in input_dict.values() if item["type"] == i)
        total_dict[i] = sum(1 for item in input_dict.values() if item["type"] <= i)
    # print(count_dict, total_dict)

    for item in input_dict:
        input_dict[item]["rank"] = (
            total_dict[int(input_dict[item]["type"])]
            - count_dict[int(input_dict[item]["type"])]
            + input_dict[item]["rank_in_same_type"]
            + 1
        )

    print(input_dict)
    return input_dict


if __name__ == "__main__":
    print("Starting script for aac-2023-07")
    parser = argparse.ArgumentParser(description="C")
    parser.add_argument("file", help="path to .txt")
    args = parser.parse_args()
    input_list = read_list(args.file)

    input_dict, alpha_dict = parse_input_list(input_list)
    output_dict = judge_hand_rank(input_dict)
    output_dict_2 = sort_hand_rank(input_dict, alpha_dict)
    output_dict_3 = get_real_rank(output_dict_2)
    result_1 = sum(
        output_dict_3[item]["bet"] * output_dict_3[item]["rank"]
        for item in output_dict_3
    )

    print(result_1)
