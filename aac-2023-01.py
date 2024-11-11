import argparse


def read_txt(file_path):
    with open(file_path, "r") as f:
        all_lines = f.readlines()
        return all_lines


def decipher_calib_doc_part_one(ary):
    result = 0

    for line in ary:
        line_number = []

        for char in line:
            if char.isdigit():
                line_number.append(char)
                break

        for char in line[::-1]:
            if char.isdigit():
                line_number.append(char)
                break

        line_number_final = int("".join(line_number))
        result += line_number_final

    return result


def decipher_calib_doc_part_two(ary):
    result = 0
    worded_digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for line in ary:
        line_numbers = []
        line_length = len(line)

        for idx, char in enumerate(line):
            if char.isdigit():
                line_numbers.append(char)
            elif idx + 2 < line_length and line[idx : idx + 3] in worded_digits:
                line_numbers.append(worded_digits[line[idx : idx + 3]])
            elif idx + 3 < line_length and line[idx : idx + 4] in worded_digits:
                line_numbers.append(worded_digits[line[idx : idx + 4]])
            elif idx + 4 < line_length and line[idx : idx + 5] in worded_digits:
                line_numbers.append(worded_digits[line[idx : idx + 5]])

        line_number_final = int("".join((str(line_numbers[0]), str(line_numbers[-1]))))

        print(line_number_final)
        result += line_number_final

    return result


if __name__ == "__main__":
    print("Starting script for aac-2023-1")
    parser = argparse.ArgumentParser(description="Process a text file.")
    parser.add_argument("file", help="Path to the input .txt file")
    args = parser.parse_args()
    input_list = read_txt(args.file)
    result1 = decipher_calib_doc_part_one(input_list)
    print(f"Result 1: {result1}")
    result2 = decipher_calib_doc_part_two(input_list)
    print(f"Result 2: {result2}")

    # part two of the puzzle => done
    # use PEP8 formatting => done
    # find out what argparse does and alternative methods
