import argparse

def read_list(filepath):
    with open(filepath, "r") as fp:
        return fp.read().splitlines()
    
def parse_list(input_list: list[str]):
    return [x.split(" ") for x in input_list]

def get_lake_area(input_list):
    x_curr = 0
    y_curr = 0
    total_dist = 0
    vertices = [(0,0)]

    for step in input_list:
        direction = step[0]
        length = step[1]

        if direction == "R":
            x_curr += int(length)
        elif direction == "L":
            x_curr -= int(length)
        elif direction == "U":
            y_curr -= int(length)
        elif direction == "D":
            y_curr += int(length)
        total_dist += int(length)
        vertices.append((x_curr, y_curr))

    print(vertices)
    ul_dr = 0
    ur_dl = 0
    for idx, vertice in enumerate(vertices):
        if idx > len(vertices) - 2:
            break
        else:
            ul_dr += vertices[idx][0] * vertices[idx+1][1]
            ur_dl += vertices[idx][1] * vertices[idx+1][0]
    area = abs(ul_dr - ur_dl) / 2
    print("Area:", area)
    print("Total dist:", total_dist)
    # Pick's Theorem 皮克定理：
    # Suppose that a polygon has integer coordinates for all of its vertices.
    # Let i be the number of integer points interior to the polygon, 
    # and let b be the number of integer points on its boundary (including both vertices and points along the sides).
    # Then the area A of this polygon is: A = i + b / 2 − 1
    # 若S代表n邊形邊上的格子點數；I代表n邊形內部的格子點數，則n邊形的面積為S/2 + I - 1.
    inner_grid_points = area - total_dist / 2 + 1
    result = total_dist + inner_grid_points
    print("Result:", result)

def get_lake_area_part_two(input_list):
    x_curr = 0
    y_curr = 0
    total_dist = 0
    vertices = [(0,0)]

    for step in input_list:
        direction = step[2][7]
        length = int(step[2][2:7], 16)

        if direction == "0":
            x_curr += int(length)
        elif direction == "2":
            x_curr -= int(length)
        elif direction == "3":
            y_curr -= int(length)
        elif direction == "1":
            y_curr += int(length)
        total_dist += int(length)
        vertices.append((x_curr, y_curr))

    print(vertices)
    ul_dr = 0
    ur_dl = 0
    for idx, vertice in enumerate(vertices):
        if idx > len(vertices) - 2:
            break
        else:
            ul_dr += vertices[idx][0] * vertices[idx+1][1]
            ur_dl += vertices[idx][1] * vertices[idx+1][0]
    area = abs(ul_dr - ur_dl) / 2
    print("Area:", area)
    print("Total dist:", total_dist)
    inner_grid_points = area - total_dist / 2 + 1
    result = total_dist + inner_grid_points
    print("Result:", result)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser("AAC-2023-Day17")
    parser.add_argument("file", help="path to the txt file")
    args = parser.parse_args()
    input_list = read_list(args.file)
    split_list = parse_list(input_list)
    get_lake_area(split_list)
    get_lake_area_part_two(split_list)