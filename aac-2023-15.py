import argparse
from time import perf_counter

def read_list(filepath):
    with open(filepath, "r") as fp:
        return fp.read().splitlines()
    
def read_list_q15(filepath):
    with open(filepath, "r") as fp:
        return fp.read()

def parse_list(string: str) -> list:
    return string.split(",")
    
def hash_string(string: str) -> int:
    init_value = 0
    for item in string:
        init_value += ord(item)
        init_value = (init_value * 17) % 256
    return init_value


if __name__ == "__main__":
    parser = argparse.ArgumentParser("AAC-2023-Day13")
    parser.add_argument("file", help="path to the txt file")
    args = parser.parse_args()
    input_list = parse_list(read_list_q15(args.file))
    print(input_list)

    result = []
    for item in input_list:
        subresult = hash_string(item)
        result.append(subresult)
    print(result)
    print(sum(result))