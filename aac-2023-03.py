import argparse
import pprint

def read_txt(file_path):
    with open(file_path, "r") as f:
        return f.read().splitlines()

def check_part_number_validity(input_list, part_number_pos):
    symbols = "!@#$%^&*()_+-=/\|"
    length_v = len(input_list) # 140
    length_h = len(input_list[0]) # 140

    # if input_list[part_number_pos[0]-1][part_number_pos[1]-1]:
    #     pass

    for i in range(part_number_pos[0]-1, part_number_pos[0]+2):
        for j in range(part_number_pos[1]-1, part_number_pos[1]+part_number_pos[2]+1):
            if i < 0 or i >= length_v or j < 0 or j >= length_h:
                continue
            elif input_list[i][j] == "*":
                return {"star": (i, j)}
            elif input_list[i][j] in symbols:
                return {"other": (i, j)}
            
    return None

def get_numbers(input_list):
    line_length = len(input_list[0])
    part_number_dict = {}

    for line_no, line in enumerate(input_list):
        l_ptr = 0
        r_ptr = 0
        while r_ptr < line_length:
            if line[r_ptr].isdigit():
                r_ptr += 1
            else:
                if r_ptr > l_ptr:
                    part_number_dict[(line_no, l_ptr, r_ptr-l_ptr)] = int(line[l_ptr:r_ptr])
                    l_ptr = r_ptr
                l_ptr += 1
                r_ptr += 1
        if r_ptr > l_ptr:
            part_number_dict[(line_no, l_ptr, r_ptr-l_ptr)] = int(line[l_ptr:r_ptr])
    
    # pprint.pprint(part_number_dict)

    valid_part_numbers = []
    gears = {}
    for item in part_number_dict:
        if check_part_number_validity(input_list, item) and "star" in check_part_number_validity(input_list, item):
            star_coords = check_part_number_validity(input_list, item)["star"]
            if star_coords in gears:
                gears[star_coords].append(item)
            else:
                gears[star_coords] = [item]

            valid_part_numbers.append(part_number_dict[item])
            print(item, part_number_dict[item], "Valid")
        elif check_part_number_validity(input_list, item):
            valid_part_numbers.append(part_number_dict[item])
            print(item, part_number_dict[item], "Valid")
        else:
            print(item, part_number_dict[item], "Invalid")

    pprint.pprint(gears)
    valid_gear_ratios = []
    for gear in gears:
        if len(gears[gear]) == 2:
            print(gear)
            print(gears[gear][0])
            print(gears[gear][1])
            valid_gear_ratios.append(part_number_dict[gears[gear][0]] * part_number_dict[gears[gear][1]] )

    # print(valid_part_numbers)
    # print(sum(valid_part_numbers))
    print(valid_gear_ratios)
    print(sum(valid_gear_ratios))
    return sum(valid_part_numbers), sum(valid_gear_ratios)


if __name__ == "__main__":
    print("Starting script for aac-2023-3")
    parser = argparse.ArgumentParser(description="A")
    parser.add_argument("file", help="Path to .txt")
    args = parser.parse_args()
    input_list = read_txt(args.file)
    result1, result2 = get_numbers(input_list)
    print(result1, result2)