import argparse

def read_list(file_path):
    with open(file_path, "r") as fp:
        return fp.read().splitlines()

def get_tree(lst):
    steps = lst[0]
    result_dict = {}
    for item in lst[2:]:
        result_dict[item[0:3]] = (item[7:10], item[12:15])
    return steps, result_dict

def traverse_tree(steps, input_dict):
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
    print(start_node)
    return steps_travelled

if __name__ == "__main__":
    parser = argparse.ArgumentParser("D")
    parser.add_argument("file", help="temp")
    args = parser.parse_args()
    input_list = read_list(args.file)
    # print(input_list)
    steps, input_dict = get_tree(input_list)
    steps_travelled = traverse_tree(steps, input_dict)
    print(steps, len(steps))
    print(steps_travelled)
