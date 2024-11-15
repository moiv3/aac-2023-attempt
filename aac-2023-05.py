import argparse
import pprint

# config
LAYERS = 7 # how many layers of mapping

def read_text(file_path):
    with open(file_path, "r") as fp:
        return fp.read().splitlines()

# for part 1, returns list of seeds and instructions
def parse_initial_list(lst):
    # deal with seeds
    seeds_list = lst[0].split(" ")[1:]

    instructions_dict = {}
    # deal with mapping
    map_instructions = []
    step = 0
    for item in lst[2:]:
        if "map" in item:
            step += 1
            map_instructions = []
        elif item == "":
            if map_instructions != ['']:
                instructions_dict[step] = map_instructions
            map_instructions = []
        else:
            map_instructions.append(item.split(" "))
    instructions_dict[step] = map_instructions
    # pprint.pprint(instructions_dict)
    # pprint.pprint(seeds_list)
    return seeds_list, instructions_dict

def get_total_mapping_dict(instructions_dict):
    total_mapping_dict = {}
    mapping_dict = {}
    for i in range(1, LAYERS+1):
        mapping_dict = {}
        for line in instructions_dict[i]:
            mapping_dict[(int(line[1]), int(line[1])+int(line[2])-1)] = int(line[0]) - int(line[1])
        total_mapping_dict[i] = mapping_dict
    return total_mapping_dict

# for part 1, takes in (seeds_list, instructions_dict) and returns a list containing the final result of every seed
def get_part_one_result_list(seeds_list, total_mapping_dict):
    result = []
    for seed in seeds_list:
        # print("Dealing with:", seed)
        seed_int = int(seed)
        for i in range(1, LAYERS+1):
            # print(f"Mapping #{i}: from {seed_int}")
            for (x,y) in total_mapping_dict[i]:
                if x <= seed_int <= y:
                    # print(f"seed between {x}, {y}")
                    seed_int += total_mapping_dict[i][(x,y)]
                    break
            # print("To:", seed_int)
        # print(f"Result: {seed_int}")
        result.append(seed_int)
    # print(result)
    return result

def fill_in_mapping_dict(total_mapping_dict):
    new_total_mapping_dict = {}
    l_bound = 0
    u_bound = 4294967295

    temp_r = 4294967295
    for i in range(1, LAYERS+1):
        new_mapping_dict = {}
        # add sotred to ensure runs in good order
        for (x, y) in sorted(total_mapping_dict[i]):
            temp_r = y
            if x > l_bound+1:
                new_mapping_dict[(l_bound+1, x-1)] = 0
                new_mapping_dict[(x, y)] = total_mapping_dict[i][(x, y)]
                l_bound = temp_r
            else:
                new_mapping_dict[(x, y)] = total_mapping_dict[i][(x, y)]
                l_bound = temp_r
        if temp_r < u_bound:
            new_mapping_dict[(temp_r+1, u_bound)] = 0
        new_total_mapping_dict[i] = new_mapping_dict
    return new_total_mapping_dict

# for part 2, takes in (seeds_list, instructions_dict) and returns a list containing the final result of every seed
def get_part_two_result_list(seeds_list, total_mapping_dict):
    print(seeds_list)
    seeds_list_modified=[]
    for i in range(len(seeds_list)):
        if i % 2 == 0:
            seeds_list_modified.append((int(seeds_list[i]), int(seeds_list[i])+int(seeds_list[i+1])-1))

    for i in range(1, LAYERS+1):
        fragment_list = []
        for (x, y) in seeds_list_modified:
            for (lower, upper) in total_mapping_dict[i]:
                movement = total_mapping_dict[i][(lower, upper)]
                if upper < x  or y < lower:
                    continue
                elif lower <= x and y <= upper:
                    fragment_list.append((x+movement, y+movement))
                    break
                elif x <= lower and y <= upper:
                    fragment_list.append((lower+movement, y+movement))
                    continue
                elif lower <= x and upper <= y :
                    fragment_list.append((x+movement, upper+movement))
                    continue
                elif x <= lower and upper <= y:
                    fragment_list.append((lower+movement, upper+movement))
                    continue
                else:
                    raise Exception("Caught execption, check logic!")
        seeds_list_modified = fragment_list
    # pprint.pprint(seeds_list_modified)
    return seeds_list_modified

if __name__ == "__main__":
    print("Starting script for aac-2023-5")
    parser = argparse.ArgumentParser(description="A")
    parser.add_argument("file", help="Path to .txt")
    args = parser.parse_args()
    input_list = read_text(args.file)
    # print(input_list)
    
    # parse input
    seeds_list, instructions_dict = parse_initial_list(input_list)
    total_mapping_dict = get_total_mapping_dict(instructions_dict)

    # part 1
    part1_result = get_part_one_result_list(seeds_list, total_mapping_dict)
    print("Part 1 result:", min(part1_result))

    # alter mapping dict
    new_total_mapping_dict = fill_in_mapping_dict(total_mapping_dict)
    # pprint.pprint(new_total_mapping_dict)

    # part 2
    part2_result = get_part_two_result_list(seeds_list, new_total_mapping_dict)
    print(min(sorted(part2_result)))