import argparse
from functools import reduce


def read_list(filepath):
    with open(filepath, "r") as fp:
        return fp.read().splitlines()


def split_puzzles(acc, x, split_value = ''):
    if x == split_value:
        acc.append([])
    else:
        acc[-1].append(x)
    return acc

def check_reflection_core(puzzle: list, omit: int|None = None) -> int:
    print("Entering [check_reflection_core]")
    puzzle_length = len(puzzle)
    for idx, _ in enumerate(puzzle):
        if omit is not None and idx == omit - 1:
            continue
        if puzzle_length <= idx + 1:
            print("Leaving [check_reflection_core], returning None")
            return None
        elif puzzle[idx] == puzzle[idx + 1]:
            check_key = idx
            nums_to_check = min(puzzle_length - 1 - check_key, check_key + 1)
            check_flag = True
            for i in range(nums_to_check):
                print(check_key)
                if puzzle[check_key - i] == puzzle[check_key + i + 1]:
                    print("Check OK")
                    continue
                else:
                    print("Check Fail")
                    check_flag = False
                    break
            if check_flag:
                # first row is 1
                print(f"Leaving [check_reflection_core], returning {idx + 1}")
                return idx + 1

def check_off_by_one_char(str1:str, str2:str) -> bool:
    if len(str1) != len(str2):
        raise Exception("Length not equal!")

    diff_chars = 0
    for a, b in zip(str1, str2):
        if a != b:
            diff_chars += 1
    if diff_chars == 1:
        return True
    else:
        return False

def check_reflection_core_smudge(puzzle: list) -> int:
    print("Checking answer before smudge...")
    last_answer = check_reflection_core(puzzle)
    print("Last answer:", last_answer)
    puzzle_length = len(puzzle)
    for idx, _ in enumerate(puzzle):
        print(idx)
        if puzzle_length <= idx+1:
            return None
        elif check_off_by_one_char(puzzle[idx], puzzle[idx + 1]):
            print(f"Line {idx} and {idx + 1} are off by one character")
            puzzle_copy = puzzle[:idx] + [puzzle[idx + 1]] + puzzle[idx+1:]
            new_answer = check_reflection_core(puzzle_copy, omit=last_answer)
            if new_answer is None:
                print("New answer is 0, no match. Checking next index...")
            elif new_answer is not None and last_answer == new_answer:
                raise Exception(f"Exception A: Last answer and new answer identical: {new_answer}")
            else:
                print(f"Found new answer. Returning {new_answer}")
                return new_answer
        elif puzzle[idx] == puzzle[idx + 1]:
            print(f"Line {idx} and {idx + 1} are identical")
            check_key = idx
            nums_to_check = min(puzzle_length - 1 - check_key, check_key + 1)
            print("Nums_to_check:", nums_to_check)
            for i in range(nums_to_check):
                print(check_key)
                if check_off_by_one_char(puzzle[check_key - i], puzzle[check_key + i + 1]):
                    print(f"Line {check_key-i} and {check_key+i+1} are off by one character")
                    puzzle_copy = puzzle[:check_key - i] + [puzzle[check_key + i + 1]] + puzzle[check_key-i+1:]
                    print(puzzle_copy)
                    new_answer = check_reflection_core(puzzle_copy, omit=last_answer)
                    if new_answer is None:
                        print("New answer is 0, no match. Checking next index...")
                    elif new_answer is not None and last_answer == new_answer:
                        raise Exception(f"Exception B: Last answer and new answer identical: {new_answer}")
                    else:
                        print(f"Found new answer. Returning {new_answer}")
                        return new_answer
                else:
                    continue
    return None

def check_reflection_part_one(puzzle_dict: dict) -> dict:
    result = {}
    
    for key, puzzle in puzzle_dict.items():
        result[key] = int(check_reflection_core(puzzle) or 0) * 100
        puzzle_transposed = [list(i) for i in zip(*puzzle)]
        result[key] += int(check_reflection_core(puzzle_transposed) or 0)
    return result

def check_reflection_part_two(puzzle_dict: dict) -> dict:
    result = {}
    
    for key, puzzle in puzzle_dict.items():
        print("\n", "Puzzle", key)
        result[key] = int(check_reflection_core_smudge(puzzle) or 0) * 100
        puzzle_transposed = [list(i) for i in zip(*puzzle)]
        result[key] += int(check_reflection_core_smudge(puzzle_transposed) or 0)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser("AAC-2023-Day13")
    parser.add_argument("file", help="path to the txt file")
    args = parser.parse_args()
    input_list = read_list(args.file)

    input_list_by_puzzle = reduce(split_puzzles, input_list, [[]])

    puzzle_dict: dict = {}

    for idx, item in enumerate(input_list_by_puzzle):
        puzzle_dict[idx] = item
    # pprint.pprint(puzzle_dict)

    result_part_one: dict = check_reflection_part_one(puzzle_dict)
    print(result_part_one)
    print(sum(result_part_one.values()))

    result_part_two: dict = check_reflection_part_two(puzzle_dict)
    print(result_part_two)
    print(sum(result_part_two.values()))