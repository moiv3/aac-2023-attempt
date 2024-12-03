import argparse
from itertools import groupby
import pprint

def read_list(filepath):
    with open(filepath, "r") as fp:
        return fp.read().splitlines()
    
def do_step(metal_dict, manual_note):
    print(metal_dict, manual_note)
    for idx, step_detail in enumerate(manual_dict[manual_note]):
        # last step
        if ":" not in step_detail and step_detail == "A":
            accept_bin.append(metal_dict)
            print("==Part accepted==")
            return
        elif ":" not in step_detail and step_detail == "R":
            reject_bin.append(metal_dict)                   
            print("==Part rejected==")
            return
        elif ":" not in step_detail:
            return do_step(metal_dict, step_detail)
        
        # not last step
        else:
            next_step = step_detail.split(":")[1]
            remain = step_detail.split(":")[0]
            xmas = step_detail[0]
            sign = step_detail[1]
            target = remain[2:]
            print(next_step, remain, xmas, sign, target)
            # match conditions
            if (sign == ">" and metal_dict[xmas] > int(target)) or (sign == "<" and metal_dict[xmas] < int(target)):
                if next_step == "A":
                    accept_bin.append(metal_dict)
                    print("==Part accepted==")
                    return
                if next_step == "R":
                    reject_bin.append(metal_dict)                    
                    print("==Part rejected==")
                    return
                else:
                    return do_step(metal_dict, next_step)
            else:
                continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser("AAC-2023-Day19")
    parser.add_argument("file", help="path to the txt file")
    args = parser.parse_args()
    input_list = read_list(args.file)
    
    # split the list
    # manual = input_list.split('')[0]
    # metals = input_list.split('')[1]
    split_at = ''
    split_list = [list(g) for k, g in groupby(input_list, lambda x: x != split_at) if k]
    manual = split_list[0]
    metals = split_list[1]
    print(manual)
    # print(metals)
    metals_dict_list = []
    for metal in metals:
        metal_dict = {}
        temp_metal_lst = metal[1:-1].split(",")
        print(temp_metal_lst)
        for xmas in temp_metal_lst:
            characteristic = xmas.split("=")[0]
            value = int(xmas.split("=")[1])
            metal_dict[characteristic] = value
        metals_dict_list.append(metal_dict)
    print(metals_dict_list)

    # parse manual
    manual_dict = {}
    for manual_item in manual:
        # manual_string_item_list = []
        manual_note = manual_item.split("{")[0]
        manual_string = manual_item.split("{")[1][:-1]
        manual_string_item_list = manual_string.split(",")
        manual_dict[manual_note] = manual_string_item_list
    pprint.pprint(manual_dict)

    accept_bin = []
    reject_bin = []

    for metal in metals_dict_list:
        do_step(metal, "in")
    print(accept_bin)
    print(reject_bin)

    print(sum([sum(i.values()) for i in accept_bin]))


