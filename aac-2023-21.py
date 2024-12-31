import argparse
from itertools import groupby
import pprint
from collections import deque

def read_list(filepath):
    with open(filepath, "r") as fp:
        return fp.read().splitlines()
    
def get_start_pos(map_list):
    for idx_y, row in enumerate(map_list):
        if "S" in row:
            for idx_x, col in enumerate(row):
                if col == "S":
                    return (idx_x, idx_y)
    return None

def move_one_step(input_map, start_position):
    map_y = len(input_map)
    map_x = len(input_map[0])
    x, y = start_position
    result = []
    # go up
    if y - 1 >= 0 and input_map[y - 1][x] != "#":
        result.append((x, y-1))
    # go down
    if y + 1 < map_y and input_map[y + 1][x] != "#":
        result.append((x, y+1))
    # go left
    if x - 1 >= 0 and input_map[y][x - 1] != "#":
        result.append((x-1, y))
    # go right
    if x + 1 < map_x and input_map[y][x + 1] != "#":
        result.append((x+1, y))
    return result

def build_map(input_map, start_position):
    map_y = len(input_map)
    map_x = len(input_map[0])
    x, y = start_position
    result = {}

    result[(x,y)] = 0
    queue = deque()
    # initial and steps
    queue.append(((x,y), 0))

    while queue:
        (curr_x, curr_y), curr_steps = queue.popleft()
        # go up
        if curr_y - 1 >= 0 and (curr_x, curr_y-1) not in result and input_map[curr_y - 1][curr_x] != "#":
            result[(curr_x, curr_y-1)] = curr_steps + 1
            queue.append(((curr_x, curr_y-1), curr_steps + 1))
        # go down
        if curr_y + 1 < map_y and (curr_x, curr_y+1) not in result and input_map[curr_y + 1][curr_x] != "#":
            result[(curr_x, curr_y+1)] = curr_steps + 1
            queue.append(((curr_x, curr_y+1), curr_steps + 1))
        # go left
        if curr_x - 1 >= 0 and (curr_x-1, curr_y) not in result and input_map[curr_y][curr_x-1] != "#":
            result[(curr_x-1, curr_y)] = curr_steps + 1
            queue.append(((curr_x-1, curr_y), curr_steps + 1))
        # go right
        if curr_x + 1 < map_x and (curr_x+1, curr_y) not in result and input_map[curr_y][curr_x+1] != "#":
            result[(curr_x+1, curr_y)] = curr_steps + 1
            queue.append(((curr_x+1, curr_y), curr_steps + 1))
        # print(queue)

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser("AAC 2023 Day 21")
    parser.add_argument("file", help="Path to input file")
    args = parser.parse_args()
    input_list = read_list(args.file)
    print(input_list)

    start_pos = get_start_pos(input_list)
    print(start_pos)
    result = build_map(input_list, start_pos)
    print(result)

    counts = 0
    even_corner = 0
    odd_corner = 0
    even_all = 0
    odd_all = 0
    for item in result:
        if result[item] % 2 == 0 and result[item] > 65:
            even_corner += 1
        if result[item] % 2 == 1 and result[item] > 65:
            odd_corner += 1
        if result[item] % 2 == 0:
            even_all += 1
        if result[item] % 2 == 1:
            odd_all += 1
    print(odd_corner, even_corner, even_all, odd_all)
    n = 202300
    result_two = (n+1) ** 2 * odd_all + (n**2) * even_all - (n+1) * odd_corner + n * even_corner
    print(result_two)
    # start_pos = set()
    # start_pos.add(get_start_pos(input_list))
    # print(start_pos)
    # pos_set = set()

    # STEPS = 64

    # for _ in range(STEPS):
    #     pos_set = set()
    #     for item in start_pos:
    #         sub_result = move_one_step(input_list, item)
    #         for sub_result_item in sub_result:
    #             pos_set.add(sub_result_item)
    #     start_pos = pos_set
    #     print(pos_set)
    # print(len(pos_set))

