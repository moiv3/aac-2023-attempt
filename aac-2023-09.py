import argparse

def read_list(file_path):
    with open(file_path, "r") as fp:
        return fp.read().splitlines()
    
def parse_line(line):
    return [int(i) for i in line.split(" ")]

def reduce_list(lst):
    new_string = []
    first_item = lst[0]
    for idx, _ in enumerate(lst):
        if idx == len(lst) - 1:
            break
        new_string.append(lst[idx+1]-lst[idx])
    return first_item, new_string

def get_extrapolation(string_list):
    first_item_list = []
    while len(set(string_list)) > 1:
        first_item, string_list = reduce_list(string_list)
        first_item_list.append(first_item)
    string_list.append(string_list[0])

    first_item_list_len = len(first_item_list)
    for _ in range(first_item_list_len):
        result_list = []
        item = first_item_list[-1]
        result_list.append(item)
        for add_item in string_list:
            item += add_item
            result_list.append(item)
        string_list = result_list
        first_item_list.pop()
    return string_list[-1]

if __name__ == "__main__":
    parser = argparse.ArgumentParser("D")
    parser.add_argument("file", help="temp")
    args = parser.parse_args()
    input_list = read_list(args.file)

    string_list = [parse_line(line) for line in input_list]
    
    # part 1
    result_list_1 = []
    for string in string_list:
        result = get_extrapolation(string)
        result_list_1.append(result)
    print(sum(result_list_1))
    
    # part 2
    result_list_2 = []
    for string in string_list:
        string.reverse()
        result = get_extrapolation(string)
        result_list_2.append(result)
    print(sum(result_list_2))