import argparse


def read_list(file_path):
    with open(file_path, "r") as fp:
        return fp.read().splitlines()


def convert_map_to_array(list_of_lists):
    return [list(line.strip()) for line in list_of_lists]


def find_starting_position(map_2d_array, start_char="S"):
    map_y = len(map_2d_array)
    map_x = len(map_2d_array[0])

    for idx, lst in enumerate(map_2d_array):
        if start_char in lst:
            for idx2, char in enumerate(lst):
                if start_char == char:
                    # (x, y) = idx, idx2
                    upper, lower, left, right = False, False, False, False
                    if idx - 1 >= 0 and map_2d_array[idx - 1][idx2] in ("|", "7", "F"):
                        upper = True
                    if idx + 1 < map_y and map_2d_array[idx + 1][idx2] in (
                        "|",
                        "J",
                        "L",
                    ):
                        lower = True
                    if idx2 - 1 >= 0 and map_2d_array[idx][idx2 - 1] in ("-", "L", "F"):
                        left = True
                    if idx2 + 1 < map_x and map_2d_array[idx][idx2 + 1] in (
                        "-",
                        "7",
                        "J",
                    ):
                        right = True

                    # print(upper, lower, left, right)

                    # get real S character based on above logic
                    if upper and lower:
                        start_char = "|"
                    elif left and right:
                        start_char = "-"
                    elif upper and left:
                        start_char = "J"
                    elif upper and right:
                        start_char = "L"
                    elif lower and left:
                        start_char = "7"
                    elif lower and right:
                        start_char = "F"
                    else:
                        raise Exception("Exception D")

                    return idx, idx2, start_char
    return None


def traverse_map(twod_array, x, y, start_char):

    steps = 0
    if start_char in ("-", "7"):
        direction = "right"
    elif start_char in ("|", "L", "J"):
        direction = "down"
    elif start_char == "F":
        direction = "up"
    else:
        raise Exception("Exception E")

    twod_array[x][y] = start_char
    start_flag = True
    x_start = x
    y_start = y

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
            raise Exception("Caught exception F!")
        # print(x,y,twod_array[x][y])
        steps += 1

        if start_flag:
            twod_array[x_start][y_start] = "S"
            start_flag = False

    return steps


def traverse_map_part_two(twod_array, x, y, start_char, empty_map):

    empty_map = empty_map[:]
    if start_char in ("-", "7"):
        direction = "right"
    elif start_char in ("|", "L", "J"):
        direction = "down"
    elif start_char == "F":
        direction = "up"
    else:
        raise Exception("Exception E")

    twod_array[x][y] = start_char
    start_flag = True
    x_start = x
    y_start = y

    while twod_array[x][y] != "S":
        # print(empty_map)
        # print(x, y, twod_array[x][y])
        empty_map[x][y] = twod_array[x][y]

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

        if start_flag:
            twod_array[x_start][y_start] = "S"
            start_flag = False

    empty_map[x][y] = start_char
    # print(empty_map)

    area = 0
    for idx, line in enumerate(empty_map):
        sub_area = 0
        outside = True
        temp_F = False
        temp_L = False
        for char in line:
            if char == "." and outside:
                pass
            elif char == "." and not outside:
                sub_area += 1
            elif char == "|":
                outside = not outside
            elif char == "-":
                pass
            elif char == "F":
                temp_F = True
            elif char == "L":
                temp_L = True
            elif char == "J":
                if temp_F:
                    outside = not outside
                    temp_F = False
                elif temp_L:
                    temp_L = False
                else:
                    raise Exception("Exception A")
            elif char == "7":
                if temp_F:
                    temp_F = False
                elif temp_L:
                    outside = not outside
                    temp_L = False
                else:
                    raise Exception("Exception B")
            else:
                raise Exception("Exception C")
        # print("Outside check:", outside)
        # print(f"Line {idx+1} area: {sub_area}")
        area += sub_area

    return area


def create_empty_map(x: int, y: int) -> list:
    # [["."]* x] * y will not work, because Python references same object!
    return [["."] * x for _ in range(y)]


if __name__ == "__main__":
    parser = argparse.ArgumentParser("AAC-2023-Day10")
    parser.add_argument("file", help="path to the .txt file")
    args = parser.parse_args()
    input_list = read_list(args.file)

    # initialize
    map_2d_array = convert_map_to_array(input_list)
    map_y = len(map_2d_array)
    map_x = len(map_2d_array[0])
    print(f"Input file read successfully, columns(x):{map_x}, rows(y):{map_y}")

    # part 1
    x, y, start_char = find_starting_position(map_2d_array, start_char="S")
    print(f"Starting position: x={x}, y={y}, starting pipe is {start_char}")
    steps = traverse_map(map_2d_array, x, y, start_char)
    farthest_point = int(steps / 2)
    print(f"Part 1 farthest point: {farthest_point} steps")

    # part 2
    empty_map = create_empty_map(map_x, map_y)
    print(f"Empty map created for part 2.")

    area = traverse_map_part_two(
        map_2d_array, x, y, start_char=start_char, empty_map=empty_map
    )
    print(f"Part 2 area: {area}")
