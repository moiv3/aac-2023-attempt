import argparse


def read_list(file_path):
    with open(file_path, "r") as fp:
        return fp.read().splitlines()

# function for part one
def get_twofold_expansion_distance(input_list):
    # transpose and expand by 2-fold
    input_list_first_expand = []
    for line in input_list:
        if all([char == "." for char in line]):
            input_list_first_expand.append(line)
            input_list_first_expand.append(line)
        else:
            input_list_first_expand.append(line)
    
    # this expression is from stackoverflow!!
    input_list_first_expand_transposed = [list(i) for i in zip(*input_list_first_expand)]
    input_list_second_expand = []
    for line in input_list_first_expand_transposed:
        if all([char == "." for char in line]):
            input_list_second_expand.append(line)
            input_list_second_expand.append(line)
        else:
            input_list_second_expand.append(line)
    # print(input_list_second_expand)

    # get all distances by a 2-layer for loop
    y = len(input_list_second_expand)
    x = len(input_list_second_expand[0])
    hashmark_list = []
    for j in range(y):
        for i in range(x):
            if input_list_second_expand[j][i] == "#":
                hashmark_list.append((j, i))
    # print(hashmark_list)

    distance_list = []
    hashmarks = len(hashmark_list)
    for i in range(hashmarks-1):
        for j in range(i+1, hashmarks):
            distance = abs(hashmark_list[j][0] - hashmark_list[i][0]) + abs(hashmark_list[j][1] - hashmark_list[i][1])
            distance_list.append(distance)
    # print(distance_list)
    # print(sum(distance_list))

    return sum(distance_list)

# part 2 function
def get_n_fold_expansion_distance(input_list, multiplier):
    # this time we only get the "indexes" for columns/rows which are all "."
    expand_list_horizontal = []
    for idx, line in enumerate(input_list):
        if all([char == "." for char in line]):
            expand_list_horizontal.append(idx)
    # print(expand_list_horizontal)

    input_list_transposed = [list(i) for i in zip(*input_list)]
    expand_list_vertical = []
    for idx, line in enumerate(input_list_transposed):
        if all([char == "." for char in line]):
            expand_list_vertical.append(idx)
    # print(expand_list_vertical)

    y = len(input_list)
    x = len(input_list[0])
    hashmark_list = []
    for j in range(y):
        for i in range(x):
            if input_list[j][i] == "#":
                hashmark_list.append((j, i))
    # print(hashmark_list)

    # this time we add the multiplier whenever crossing the hashmark_list when calculating distances

    distance_list = []
    hashmarks = len(hashmark_list)
    for i in range(hashmarks-1):
        for j in range(i+1, hashmarks):
            distance = abs(hashmark_list[j][0] - hashmark_list[i][0]) + abs(hashmark_list[j][1] - hashmark_list[i][1])
            min_x = min(hashmark_list[j][0], hashmark_list[i][0])
            max_x = max(hashmark_list[j][0], hashmark_list[i][0])
            distance_expand_x = sum([multiplier-1 for i in range(min_x+1, max_x) if i in expand_list_horizontal])
            min_y = min(hashmark_list[j][1], hashmark_list[i][1])
            max_y = max(hashmark_list[j][1], hashmark_list[i][1])
            distance_expand_y = sum([multiplier-1 for i in range(min_y+1, max_y) if i in expand_list_vertical])
            distance_list.append(distance+distance_expand_x+distance_expand_y)
    # print(distance_list)
    # print(sum(distance_list))
    return sum(distance_list)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("AAC-2023-Day11")
    parser.add_argument("file", help="path to the .txt file")
    args = parser.parse_args()
    input_list = read_list(args.file)

    # part one
    twofold_expansion_dist = get_twofold_expansion_distance(input_list)
    print(twofold_expansion_dist)

    # part two
    nfold_expansion_dist = get_n_fold_expansion_distance(input_list, multiplier=1000000)
    print(nfold_expansion_dist)
            

