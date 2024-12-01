import argparse
import pprint

def read_list(filepath):
    with open(filepath, "r") as fp:
        return fp.read().splitlines()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser("AAC-2023-Day17")
    parser.add_argument("file", help="path to the txt file")
    args = parser.parse_args()
    input_list = read_list(args.file)