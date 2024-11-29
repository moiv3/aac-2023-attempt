import argparse
import pprint

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
        item_steps = {}
        if "-" in item:
            item_steps["lens"] = item.split("-")[0]
            item_steps["motion"] = "-"
            item_steps["focallength"] = None
            item_steps["hash"] = hash_string(item.split("-")[0])
        elif "=" in item:
            item_steps["lens"] = item.split("=")[0]
            item_steps["motion"] = "="
            item_steps["focallength"] = item.split("=")[1]
            item_steps["hash"] = hash_string(item.split("=")[0])
        result.append(item_steps)
    pprint.pprint(result)

    hashmap = {}
    for step in result:
        if step["motion"] == "-":
            if step["hash"] in hashmap:
                for d in hashmap[step["hash"]]:
                    # print(d.keys()[0])
                    if [*d][0] == step["lens"]:
                        hashmap[step["hash"]].remove(d)
        elif step["motion"] == "=":
            # print("========", hashmap)
            # print("==========", step["lens"])
            if step["hash"] not in hashmap or step["hash"] == []:
                hashmap[step["hash"]] = [{step["lens"]: int(step["focallength"])}]

            elif step["hash"] in hashmap:
                flag = True
                for d in hashmap[step["hash"]]:
                    if [*d][0] == step["lens"]:
                        flag = False
                        print("focallength substituted")
                        d[step["lens"]] = int(step["focallength"])
                if flag is True:
                    hashmap[step["hash"]].append({step["lens"]:int(step["focallength"])})
            else:
                raise Exception("Exception B")
        else:
            raise Exception("Exception A: motion is not - or =")
        # print(hashmap)
    # pprint.pprint(hashmap)

    result = 0
    for i in hashmap:
        if hashmap[i]:
            for idx, item in enumerate(hashmap[i]):
                key = list(item.keys())[0]  # Get the single key in the dictionary
                value = item[key]
                result += (i + 1) * (idx + 1) * value
    print(result)