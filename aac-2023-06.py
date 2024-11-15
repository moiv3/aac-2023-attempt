import argparse
import math

def read_text(file_path):
    with open(file_path, "r") as fp:
        return fp.read().splitlines()

def parse_time_dist(lst):
    time_list = [item for item in lst[0].split(" ") if item and item != "Time:"]
    dist_list = [item for item in lst[1].split(" ") if item and item != "Distance:"]
    # print(time_list, dist_list)
    race_dict = {}
    for idx, item in enumerate(time_list):
        race_dict[idx] = (int(item), int(dist_list[idx]))
    # print(race_dict)
    return race_dict

def get_race_win_condition(race_dict):
    list_of_ways = []
    for race in race_dict:
        print(race_dict[race])
        print(f"a={1},b=-{race_dict[race][0]},c={race_dict[race][1]}")
        a = 1
        b = -race_dict[race][0]
        c = race_dict[race][1]
        upper_bound = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (a * 2)
        lower_bound = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (a * 2)

        upper_bound_int = math.floor(upper_bound)
        lower_bound_int = math.ceil(lower_bound)
        print(race, upper_bound_int, lower_bound_int)
        list_of_ways.append(upper_bound_int-lower_bound_int+1)
    print(list_of_ways)
    print(math.prod(list_of_ways))
    return math.prod(list_of_ways)

if __name__ == "__main__":
    print("Starting script for aac-2023-6")
    parser = argparse.ArgumentParser(description="A")
    parser.add_argument("file", help="Path to .txt")
    args = parser.parse_args()
    input_list = read_text(args.file)
    race_dict = parse_time_dist(input_list)
    winning_ways = get_race_win_condition(race_dict)