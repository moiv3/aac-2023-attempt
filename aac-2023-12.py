import argparse
import pprint


def read_list(file_path):
    with open(file_path, "r") as fp:
        return fp.read().splitlines()
    

def parse_lines(input_list):
    output_list = []
    for item in input_list:
        target_string = item.split(" ")[0]
        target_seq = [int(i) for i in item.split(" ")[1].split(",")]
        output_list.append((target_string, target_seq))
    return output_list


def recursive_function(input_list, input_seq):    
    len_input_list = len(input_list)
    total = 0
    if len(input_seq) == 0:
        return 0
    else:
        con = input_seq[0]
        for idx, char in enumerate(input_list):
            print("Trying to match:", input_seq, con, input_list[idx:])
            if (idx+con <= len_input_list and all([char in ('#') for char in input_list[idx:idx+con]])):
                print("Matched consecutive #s, forcing match")
                if len(input_seq) == 1:
                    print("Last sequence, recursion ending. Returning 1")
                    return 1
                else:
                    print("Recursively checking:", input_list[idx+con+1:], input_seq[1:])
                    total += recursive_function(input_list[idx+con+1:], input_seq[1:])
                    print("force break")
                    break

            elif (idx+con <= len_input_list and all([char in ('?','#') for char in input_list[idx:idx+con]])):
                if idx+con+1 < len_input_list and input_list[idx+con] == "#":
                    print("Next char is #, no match")
                    continue
                if idx >= 1 and input_list[idx-1] == "#":
                    print("Prev char was #, no match")
                    continue
                print("Matched", con, input_list[idx:])

                if len(input_seq) == 1:
                    print("Last sequence, recursion ending. Counting possible ways:")
                    print(input_list, input_seq[0])
                    counter = 0
                    for idx, char in enumerate(input_list):
                        if idx + input_seq[0] <= len(input_list) and all(char in ("?", "#") for char in input_list[idx:idx+input_seq[0]]) and '#' not in input_list[idx+input_seq[0]+1:] and '#' not in input_list[:idx]:
                            counter += 1
                        
                    print("Possible ways:", counter)
                    return counter
                else:
                    print("Recursively checking:", "/", input_list[idx+con+1:], "/", input_seq[1:])
                    total += recursive_function(input_list[idx+con+1:], input_seq[1:])
            else:
                print("No match", con, input_list)
                continue
        return total

def recursive_function_2(input_list, input_seq):
    print(input_list, input_seq)
    if len(input_list) < sum(input_seq):
        return 0
    elif len(input_seq) == 1 and input_seq[0] == 0:
        if all([char in ('?','.') for char in input_list]):
            return 1
        else:
            return 0
        
    elif input_seq[0] == 0:
        return recursive_function_2(input_list[1:],input_seq[1:])
    
    elif input_list[0] == '#':
        if input_seq[0] == 0:
            return 0
        else:
            input_seq_new = [input_seq[0]-1] + input_seq[1:]

            return recursive_function_2(input_list[1:],input_seq_new)
    elif input_list[0] == '.':
        return recursive_function_2(input_list[1:],input_seq)
    elif input_list[0] == '?':
        return recursive_function_2('#'+input_list[1:],input_seq) + recursive_function_2('.'+input_list[1:],input_seq)

def brute_force_function(input_list, input_seq):
    match_counter = 0
    unknowns = input_list.count("?")
    for i in range(2 ** unknowns):
        new_string = ""
        j = i
        for char in input_list:
            if char != "?":
                new_string += char
            elif char == "?":
                if j % 2 == 0:
                    new_string += "."
                else:
                    new_string += "#"
                j = j // 2
        # print(new_string)
        new_string_rep=[]
        hash_counter_temp = 0
        for char in new_string:
            if char == "." and hash_counter_temp == 0:
                continue
            elif char == "." and hash_counter_temp > 0:
                new_string_rep.append(hash_counter_temp)
                hash_counter_temp = 0
            else:
                hash_counter_temp += 1
        if hash_counter_temp > 0:
            new_string_rep.append(hash_counter_temp)
        # print(new_string, new_string_rep)
        if new_string_rep == input_seq:
            match_counter += 1
    return match_counter

if __name__ == "__main__":
    parser = argparse.ArgumentParser("AAC-2023-Day11")
    parser.add_argument("file", help="path to the .txt file")
    args = parser.parse_args()
    input_list = read_list(args.file)

    input_list_parsed = parse_lines(input_list)

    result = {}
    for idx, item in enumerate(input_list_parsed):
        # print(tuple(item))
        new_x = item[0]+item[0]
        new_y = item[1]+item[1]
        # result[idx+1] = (brute_force_function(item[0], item[1]))        result[idx+1] = (brute_force_function(item[0], item[1]))
        result[idx+1] = (brute_force_function(new_x, new_y))
    pprint.pprint(result)
    print(sum(result.values()))

    # input_list = ".#.?.?.?##??#??#??#?"
    # input_seq = [1,1,1,7,5]

    # print(brute_force_function(input_list, input_seq))

    # output = 8926, too high
    # output = 7506, just right!