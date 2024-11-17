import argparse
import math
from functools import reduce

def read_list(file_path):
    with open(file_path, "r") as fp:
        return fp.read().splitlines()


def lcm_of_list(numbers):
    return reduce(math.lcm, numbers)


def get_tree(lst):
    steps = lst[0]
    result_dict = {}
    for item in lst[2:]:
        result_dict[item[0:3]] = (item[7:10], item[12:15])
    return steps, result_dict


def traverse_tree_part_one(steps, input_dict):
    start_node = 'AAA'
    end_node = 'ZZZ'
    step_len = len(steps)
    steps_travelled = 0
    while start_node != end_node:
        direction = steps[steps_travelled % step_len]
        if direction == 'L':
            start_node = input_dict[start_node][0]
            steps_travelled += 1
        elif direction == 'R':
            start_node = input_dict[start_node][1]
            steps_travelled += 1
        else:
            raise Exception("Something strange happened!")
    return steps_travelled


def traverse_tree_part_two(steps, input_dict):
    a_list = []
    for item in input_dict:
        if item[2] == 'A':
            a_list.append(item)

    a_steps_list = []

    step_len = len(steps)

    for item in a_list:
        print(item)
        steps_travelled = 0
        while steps_travelled <= 1000000:
            direction = steps[steps_travelled % step_len]
            if direction == 'L':
                item = input_dict[item][0]
                steps_travelled += 1
            elif direction == 'R':
                item = input_dict[item][1]
                steps_travelled += 1
            else:
                raise Exception("Something strange happened!")
            
            if item[2] == 'Z':
                print(item, steps_travelled)
                a_steps_list.append(steps_travelled)
                break

    result = lcm_of_list(a_steps_list)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser("D")
    parser.add_argument("file", help="temp")
    args = parser.parse_args()
    input_list = read_list(args.file)
    # print(input_list)
    steps, input_dict = get_tree(input_list)
    steps_travelled_1 = traverse_tree_part_one(steps, input_dict)
    steps_travelled_2 = traverse_tree_part_two(steps, input_dict)
    print(steps_travelled_1)
    print(steps_travelled_2)
