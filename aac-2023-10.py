import argparse


def read_list(file_path):
    with open(file_path, "r") as fp:
        return fp.read().splitlines()


def convert_map_to_array(list_of_lists):
    return [list(line.strip()) for line in list_of_lists]


def traverse_map(twod_array, x, y):
    steps = 0
    direction = "right"
    while twod_array[x][y] != "S":
        if twod_array[x][y] == "|" and direction == "up":
            x -= 1
        elif twod_array[x][y] == "|" and direction == "down":
            x += 1
        elif twod_array[x][y] == "-" and direction == "left":
            y -= 1
        elif twod_array[x][y] == "-" and direction == "right":
            y += 1
        elif twod_array[x][y] == "7" and direction == "up":
            y -= 1
            direction = "left"
        elif twod_array[x][y] == "7" and direction == "right":
            x += 1
            direction = "down"
        elif twod_array[x][y] == "L" and direction == "down":
            y += 1
            direction = "right"
        elif twod_array[x][y] == "L" and direction == "left":
            x -= 1
            direction = "up"
        elif twod_array[x][y] == "F" and direction == "up":
            y += 1
            direction = "right"
        elif twod_array[x][y] == "F" and direction == "left":
            x += 1
            direction = "down"
        elif twod_array[x][y] == "J" and direction == "down":
            y -= 1
            direction = "left"
        elif twod_array[x][y] == "J" and direction == "right":
            x -= 1
            direction = "up"
        else:
            raise Exception("Caught exception!")

        steps += 1
    steps += 1
    return steps


if __name__ == "__main__":
    parser = argparse.ArgumentParser("E")
    parser.add_argument("file", help="path to the file")
    args = parser.parse_args()
    input_list = read_list(args.file)

    map_2d_array = convert_map_to_array(input_list)
    steps = traverse_map(map_2d_array, 31, 112)
    print(steps / 2)
    # "s" at [31][111]
    # fix how to get initial position
