import argparse
import pprint

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

# for part 1, takes in (seeds_list, instructions_dict) and returns a list containing the final result of every seed
def get_part_one_result_list(seeds_list, instructions_dict):
    total_mapping_dict = {}
    mapping_dict = {}
    for i in range(1,8):
        mapping_dict = {}
        for line in instructions_dict[i]:
            mapping_dict[(int(line[1]), int(line[1])+int(line[2])-1)] = int(line[0]) - int(line[1])
        total_mapping_dict[i] = mapping_dict
    pprint.pprint(total_mapping_dict)

    result = []
    for seed in seeds_list:
        # print("Dealing with:", seed)
        seed_int = int(seed)
        for i in range(1,8):
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

if __name__ == "__main__":
    print("Starting script for aac-2023-5")
    parser = argparse.ArgumentParser(description="A")
    parser.add_argument("file", help="Path to .txt")
    args = parser.parse_args()
    input_list = read_text(args.file)
    # print(input_list)

    # part 1
    seeds_list, instructions_dict = parse_initial_list(input_list)
    part1_result = get_part_one_result_list(seeds_list, instructions_dict)
    print("Part 1 result:", min(part1_result))
