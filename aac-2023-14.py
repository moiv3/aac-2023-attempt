import argparse
from time import perf_counter

def read_list(filepath):
    with open(filepath, "r") as fp:
        return fp.read().splitlines()

def pull_lever_part_one(input_list, cycle=False, times=1):
    input_list_parsed = [list(i) for i in input_list]
    new_list = input_list_parsed[:]
    seen_counter = 0
    result_set = set()
    cycle_set = set()
    cycle_list = []
    end_counter = 0
    # for s in new_list:
    #     print(*s)
    for cycle_no in range(1, times+1):
        for i in ["north", "west", "south", "east"]:
            if not cycle and i in ["west", "south", "east"]:
                continue
            total_moves = 1
            steps = 0

            while total_moves > 0:
                # print("===================")
                steps += 1
                total_moves = 0
                input_list = new_list[:]
                for idx_y, line in enumerate(input_list):
                    for idx_x, _ in enumerate(line):

                        if i == 'north':
                            if idx_y == 0:
                                continue
                            elif input_list[idx_y][idx_x] == "O" and input_list[idx_y-1][idx_x] == ".":
                                new_list[idx_y-1][idx_x] = "O"
                                new_list[idx_y][idx_x] = "."
                                total_moves += 1
                        elif i == 'south':
                            if idx_y == len(input_list)-1:
                                continue
                            elif input_list[idx_y][idx_x] == "O" and input_list[idx_y+1][idx_x] == ".":
                                new_list[idx_y+1][idx_x] = "O"
                                new_list[idx_y][idx_x] = "."
                                total_moves += 1
                        elif i == 'west':
                            if idx_x == 0:
                                continue
                            elif input_list[idx_y][idx_x] == "O" and input_list[idx_y][idx_x-1] == ".":
                                new_list[idx_y][idx_x-1] = "O"
                                new_list[idx_y][idx_x] = "."
                                total_moves += 1
                        elif i == 'east':
                            if idx_x == len(input_list[0])-1:
                                continue
                            elif input_list[idx_y][idx_x] == "O" and input_list[idx_y][idx_x+1] == ".":
                                new_list[idx_y][idx_x+1] = "O"
                                new_list[idx_y][idx_x] = "."
                                total_moves += 1
            # print("Total moves:", total_moves)
        # print("Steps:", steps)

        # for s in new_list:
        #     print(*s)
        result_one = 0
        length = len(new_list)
        for idx, line in enumerate(new_list):
            result_one += sum(length-idx for i in line if i == "O")

        # deal with multiple cycles, finding the pattern
        if result_one in result_set:
            seen_counter += 1
            cycle_list.append(result_one)
        else:
            seen_counter = 0
            result_set.add(result_one)
            cycle_list = []
        
        # start recording cycle when x=6 consecutive seens
        if seen_counter >= 6:
            # print(f"seen_counter triggered at cycle {cycle}, starting at cycle {cycle-seen_counter}")
            cycle_set.add(result_one)
            end_counter += 1
        
        # TODO: potential bug: same numbers in a cycle, for example test case
        if end_counter >= 50:
            print(f"Found cycle, length: {len(cycle_set)}, starting at cycle {cycle_no-seen_counter}")
            return new_list, cycle_no-seen_counter, len(cycle_set), cycle_list[0:len(cycle_set)]

    return new_list, None, None, None

def calc_result_one(lst):
    result_one = 0
    length = len(lst)
    for idx, line in enumerate(lst):
        result_one += sum(length-idx for i in line if i == "O")
    # print(result_one)
    return result_one

if __name__ == "__main__":
    parser = argparse.ArgumentParser("AAC-2023-Day13")
    parser.add_argument("file", help="path to the txt file")
    args = parser.parse_args()
    input_list = read_list(args.file)

    # part one
    result_one, _, _, _ = pull_lever_part_one(input_list)
    print(calc_result_one(result_one))

    # part two
    result_two, cycle_start_index, cycle_length, cycle_details = pull_lever_part_one(input_list, cycle=True, times=500)
    print(cycle_details)
    target = 10 ** 9
    answer_two = cycle_details[(target - cycle_start_index - 1) % cycle_length]
    print(answer_two)
    
    # write tests here