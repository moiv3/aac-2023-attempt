import argparse
import numpy as np
from numpy.typing import NDArray
import copy

def read_list(filepath):
    with open(filepath, "r") as fp:
        return fp.read().splitlines()
    
def parse_input(input_list: list[str]):
    result = []
    for idx, input_string in enumerate(input_list):
        from_str = input_string.split("~")[0]
        to_str = input_string.split("~")[1]
        from_x, from_y, from_z = (int(d) for d in from_str.split(","))
        to_x, to_y, to_z = (int(d) for d in to_str.split(","))
        # print(from_x,from_y,from_z)
        # print(to_x,to_y,to_z)
        item = {}
        item["id"] = idx + 1
        item["start_x"], item["start_y"], item["start_z"] = (from_x,from_y,from_z)
        item["end_x"], item["end_y"], item["end_z"] = (to_x,to_y,to_z)

        if to_z > from_z:
            item["direction"] = "z"
        elif to_y > from_y:
            item["direction"] = "y"
        elif to_x > from_x:
            item["direction"] = "x"
        else:
            item["direction"] = "z"

        result.append(item)
    return result

def create_3d_array(z: int,y:int,x:int):
    x = np.zeros((z,y,x))
    # print(x)
    return x

def add_bricks_into_array(bricks:list[dict], threed_array: NDArray):
    for brick in bricks:
        # print(brick)
        if brick["direction"] == "x":
            for x in range(brick["start_x"], brick["end_x"]+1):
                threed_array[brick["start_z"]][brick["start_y"]][x] = brick["id"]
        elif brick["direction"] == "y":
            for y in range(brick["start_y"], brick["end_y"]+1):
                threed_array[brick["start_z"]][y][brick["start_x"]] = brick["id"]
        elif brick["direction"] == "z":
            for z in range(brick["start_z"], brick["end_z"]+1):
                threed_array[z][brick["start_y"]][brick["start_x"]] = brick["id"]
        
    return threed_array

def brick_fall(parsed_input, full_3d_array, fall_once=False):
    total_moves = 1
    cycles = 0
    first_cycle = True
    fell_bricks = set()
    while first_cycle or total_moves > 0:
        cycles += 1
        total_moves = 0
        # print(f"==Initiating new fall cycle # {cycles}==")
        for brick in parsed_input:
            # print(f"checking brick {brick["id"]}")
            if brick["direction"] == "z":
                while brick["start_z"] > 1 and full_3d_array[brick["start_z"]-1][brick["start_y"]][brick["start_x"]] == 0:
                    brick["start_z"] -= 1
                    brick["end_z"] -= 1
                    total_moves += 1
                    # print(f"Fell down brick {brick["id"]}")
                    fell_bricks.add(brick["id"])

            elif brick["direction"] == "y":
                # print([(brick["start_z"]-1,y,brick["start_x"]) for y in range(brick["start_y"],brick["end_y"]+1)])
                while brick["start_z"] > 1 and all([full_3d_array[brick["start_z"]-1][y][brick["start_x"]] == 0 for y in range(brick["start_y"],brick["end_y"]+1)]):
                    brick["start_z"] -= 1
                    brick["end_z"] -= 1
                    total_moves += 1
                    # print(f"Fell down brick {brick["id"]}")
                    fell_bricks.add(brick["id"])

            elif brick["direction"] == "x":
                # print([(brick["start_z"]-1,brick["start_y"],x) for x in range(brick["start_x"],brick["end_x"]+1)])
                # print([full_3d_array[brick["start_z"]-1][brick["start_y"]][x] == 0 for x in range(brick["start_x"],brick["end_x"]+1)])
                while brick["start_z"] > 1 and all([full_3d_array[brick["start_z"]-1][brick["start_y"]][x] == 0 for x in range(brick["start_x"],brick["end_x"]+1)]):
                    brick["start_z"] -= 1
                    brick["end_z"] -= 1
                    total_moves += 1
                    # print(f"Fell down brick {brick["id"]}")
                    fell_bricks.add(brick["id"])
            else:
                pass

        # print(f"Blocks fallen during this cycle: {total_moves}")
        # if fall_once flag is True, return early with result
        if fall_once and total_moves == 0:
            return False, set()
        elif fall_once:
            return True, fell_bricks
        # normal logic
        elif first_cycle and total_moves == 0:
            print(f"No blocks fallen during first cycle, ending loop")
            return False, set()
        else:
            first_cycle = False

    # print(f"No blocks fallen, ending loop")
    return parsed_input, fell_bricks

if __name__ == "__main__":
    parser = argparse.ArgumentParser("AAC 2023 Day 22")
    parser.add_argument("file", help="Path to input file")
    args = parser.parse_args()
    input_list = read_list(args.file)
    empty_3d_array = create_3d_array(330,10,10)
    parsed_input = parse_input(input_list)
    print(*parsed_input, sep="\n")
    full_3d_array = add_bricks_into_array(parsed_input, empty_3d_array)
    print(full_3d_array)
    bigcycles = 0
    while True:
        bigcycles += 1
        # print(f"======Starting a New Big fall cycle {bigcycles}======")
        new_parsed_input, _ = brick_fall(parsed_input, full_3d_array)
        # print(new_parsed_input)
        if new_parsed_input is False:
            break
        # build new 3d array by new input
        empty_3d_array = create_3d_array(330,10,10)
        full_3d_array = add_bricks_into_array(new_parsed_input, empty_3d_array)
        parsed_input = new_parsed_input
        
    print("=====Bricks after initial fall=======")
    print("final array of bricks:")
    print(*parsed_input, sep="\n")
    print("=====Backing up array of bricks after initial fall=======")
    parsed_input_backup = copy.deepcopy(parsed_input)

    print("==========================")
    print("checking each brick for support:")
    brick_check_list = parsed_input
    total_fell_bricks_count = 0
    fell_bricks_list = []
    safely_disintegrated = 0
    for i in range(len(brick_check_list)):
        print(f"========Checking brick #{brick_check_list[i]["id"]}========")
        # print(f"Excluded brick: {brick_check_list[i]}")

        brick_check_list = copy.deepcopy(parsed_input_backup)
        # print(*brick_check_list, sep="\n")
        all_bricks_copy = [brick_check_list[a] for a in range(len(brick_check_list)) if a != i]
        # print(f"Remaining bricks:")
        # print(*all_bricks_copy, sep="\n")
        empty_3d_array = create_3d_array(330,10,10)
        full_3d_array = add_bricks_into_array(all_bricks_copy, empty_3d_array)
        # print(full_3d_array)
        # part 1
        # fall_result, _ = brick_fall(all_bricks_copy, full_3d_array, fall_once=True)
        # if fall_result is False:
        #     print(f"{brick["id"]} is safe fo disintegrate!")
        #     safely_disintegrated += 1
        
        # part 2
        total_brick_fall_set = set()
        bigcycles = 0
        while True:
            bigcycles += 1
            # print(f"======Starting a New Big fall cycle {bigcycles}======")
            # print("Before fall:")
            # print(*all_bricks_copy, sep="\n")
            new_parsed_input, brick_fall_set = brick_fall(all_bricks_copy, full_3d_array)
            total_brick_fall_set.update(brick_fall_set)
            # print(new_parsed_input)
            if new_parsed_input is False:
                total_fell_bricks_count += len(total_brick_fall_set)
                fell_bricks_list.append(len(total_brick_fall_set))
                print(f"***Total fell down bricks when removing brick {brick_check_list[i]["id"]}: {len(total_brick_fall_set)}")
                break
            # build new 3d array by new input
            empty_3d_array = create_3d_array(330,10,10)
            full_3d_array = add_bricks_into_array(new_parsed_input, empty_3d_array)
            parsed_input = new_parsed_input
        # input()
        
    # print(f"Total safe bricks: {safely_disintegrated}")
    print(f"Total bricks fallen: {total_fell_bricks_count}")
    print(f"Fell bricks list by brick: {fell_bricks_list}")
