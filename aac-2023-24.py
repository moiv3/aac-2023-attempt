import argparse

def read_list(filepath):
    with open(filepath, "r") as fp:
        return fp.read().splitlines()


def parse_part_one(input_list):
    parsed_list = []
    for line in input_list:
        x, y, z = (int(i) for i in line.split("@")[0].split(","))
        a, b, c = (int(i) for i in line.split("@")[1].split(","))
        parsed_list.append(((x, y, z),(a, b, c)))
    print(*parsed_list, sep="\n")
    return parsed_list

def solve_part_one(parsed_list, min_threshold, max_threshold):
    print("==========")
    length = len(parsed_list)
    result = []
    for i in range(length):
        for j in range(i+1, length):
            print("==New set==")
            print(parsed_list[i])
            print(parsed_list[j])
            a = parsed_list[i][1][0]
            b = -parsed_list[j][1][0]
            c = parsed_list[i][1][1]
            d = -parsed_list[j][1][1]
            e = -parsed_list[i][0][0] + parsed_list[j][0][0]
            f = -parsed_list[i][0][1] + parsed_list[j][0][1]
            print((a,b,c,d,e,f))
            
            if (a*d)== (b*c):
                print("parellel lines detected, no solution")
                continue
            else:
                sol_x = ((e*d)-(b*f)) / ((a*d)-(b*c))
                sol_y = ((a*f)-(e*c)) / ((a*d)-(b*c))
                print(f"Time: {sol_x}, {sol_y}")
                intersect_x = parsed_list[i][0][0] + sol_x * parsed_list[i][1][0]
                intersect_y = parsed_list[i][0][1] + sol_x * parsed_list[i][1][1]
                print(f"Intersect: {intersect_x}, {intersect_y}")
                if min_threshold < intersect_x < max_threshold and \
                    min_threshold < intersect_y < max_threshold and \
                    sol_x >= 0 and sol_y >= 0:
                    result.append((intersect_x, intersect_y))
    return result

def solve_part_two(input_list):
    from sympy.abc import a,b,c,x,y,z
    from sympy import solve

    question_array = []
    for i in range(5):
        question_array.append((x - input_list[i][0][0]) * (input_list[i][1][1] - b) - (y - input_list[i][0][1]) * (input_list[i][1][0] - a))
        question_array.append((x - input_list[i][0][0]) * (input_list[i][1][2] - c) - (z - input_list[i][0][2]) * (input_list[i][1][0] - a))

    answer = solve(question_array, x,y,z,a,b,c)
    print(answer)
    return answer

if __name__ == "__main__":
    parser = argparse.ArgumentParser("AAC 2023 Day 24")
    parser.add_argument("file", help="Path to input file")
    args = parser.parse_args()
    input_list = read_list(args.file)
    print(*input_list, sep="\n")
    parsed_input_list = parse_part_one(input_list)
    result = solve_part_one(parsed_input_list, 200000000000000, 400000000000000)
    print(len(result))

    answer = solve_part_two(parsed_input_list)
    print(answer[0][0]+answer[0][1]+answer[0][2])
