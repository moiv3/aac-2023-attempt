import argparse
import itertools

# Use all (y,x) notation in this puzzle!

class Traverser:

    id_iter = itertools.count()

    def __init__(self, path=[], intersections=[], prev=(0,1), curr=(1,1), steps=1,fromNode=(0,1), fromDirection=None):
        
        self.id = next(self.id_iter)
        self.path=path
        self.intersections=intersections
        self.prev=prev
        self.curr=curr
        self.steps=steps
        self.validity=True
        self.fromNode=fromNode
        self.fromDirection=fromDirection

def read_list(filepath):
    with open(filepath, "r") as fp:
        return fp.read().splitlines()
    
def part_one(input_list):
    map_y = len(input_list)
    map_x = len(input_list[0])
    endpoint = (map_y - 1, map_x - 2)
    print(endpoint)
    traverser = Traverser()
    print(traverser.id)
    traverser_list = []
    traverser_list.append(traverser)
    traverser_step_list=[]
    for traverser in traverser_list:
        while traverser.curr != endpoint:
            # check which way is valid
            # up direction
            if input_list[traverser.curr[0]-1][traverser.curr[1]] == "." and (traverser.curr[0]-1 ,traverser.curr[1]) != traverser.prev:
                traverser.path.append(traverser.curr)
                traverser.prev = traverser.curr
                traverser.curr = (traverser.curr[0]-1 ,traverser.curr[1])
                traverser.steps += 1
            # down direction
            elif input_list[traverser.curr[0]+1][traverser.curr[1]] == "." and (traverser.curr[0]+1 ,traverser.curr[1]) != traverser.prev:
                traverser.path.append(traverser.curr)
                traverser.prev = traverser.curr
                traverser.curr = (traverser.curr[0]+1 ,traverser.curr[1])
                traverser.steps += 1
            # left direction
            elif input_list[traverser.curr[0]][traverser.curr[1]-1] == "." and (traverser.curr[0] ,traverser.curr[1]-1) != traverser.prev:
                traverser.path.append(traverser.curr)
                traverser.prev = traverser.curr
                traverser.curr = (traverser.curr[0] ,traverser.curr[1]-1)
                traverser.steps += 1
            # right direction
            elif input_list[traverser.curr[0]][traverser.curr[1]+1] == "." and (traverser.curr[0] ,traverser.curr[1]+1) != traverser.prev:
                traverser.path.append(traverser.curr)
                traverser.prev = traverser.curr
                traverser.curr = (traverser.curr[0] ,traverser.curr[1]+1)
                traverser.steps += 1
            # right AND down slopes
            elif input_list[traverser.curr[0]+1][traverser.curr[1]] == "v" and input_list[traverser.curr[0]][traverser.curr[1]+1] == ">":
                traverser_list.append(Traverser(
                    prev=(traverser.curr[0],traverser.curr[1]+1),
                    curr=(traverser.curr[0] ,traverser.curr[1]+2),
                    steps=traverser.steps+2)
                )
                traverser.path.append(traverser.curr)
                traverser.prev = (traverser.curr[0]+1 ,traverser.curr[1])
                traverser.curr = (traverser.curr[0]+2 ,traverser.curr[1])
                traverser.steps += 2
            # down slope
            elif input_list[traverser.curr[0]+1][traverser.curr[1]] == "v" and (traverser.curr[0]+1 ,traverser.curr[1]) != traverser.prev:
                traverser.path.append(traverser.curr)
                traverser.prev = (traverser.curr[0]+1 ,traverser.curr[1])
                traverser.curr = (traverser.curr[0]+2 ,traverser.curr[1])
                traverser.steps += 2
            # right slope
            elif input_list[traverser.curr[0]][traverser.curr[1]+1] == ">" and (traverser.curr[0] ,traverser.curr[1]+1) != traverser.prev:
                traverser.path.append(traverser.curr)
                traverser.prev = (traverser.curr[0] ,traverser.curr[1]+1)
                traverser.curr = (traverser.curr[0] ,traverser.curr[1]+2)
                traverser.steps += 2
            else:
                print("No next step, ending")
                print(vars(traverser))
                return
            
        print(f"Traverser {traverser.id} arrived at terminal with steps: {traverser.steps}")
        # print(vars(traverser))
        traverser_step_list.append(traverser.steps)

    return sorted(traverser_step_list)

def build_map(input_list):
    map_y = len(input_list)
    map_x = len(input_list[0])
    endpoint = (map_y - 1, map_x - 2)
    print(endpoint)
    traverser = Traverser()
    print(traverser.id)
    traverser_list = []
    traverser_list.append(traverser)
    traverser_step_list=[]
    node_dict = {}
    for traverser in traverser_list:
        while traverser.curr != endpoint:
            # check if traverser is at a node
            if all(
                (input_list[traverser.curr[0]-1][traverser.curr[1]] != ".",
                input_list[traverser.curr[0]+1][traverser.curr[1]] != ".",
                input_list[traverser.curr[0]][traverser.curr[1]-1] != ".",
                input_list[traverser.curr[0]][traverser.curr[1]+1] != ".")
                ):
                
                # put node and distance into node_dict
                if traverser.fromNode not in node_dict:
                    node_dict[traverser.fromNode] = {traverser.curr: {"direction": traverser.direction,
                                                                      "steps": traverser.steps}}
                else:
                    node_dict[traverser.fromNode][traverser.curr] = {"direction": traverser.direction,
                                                                      "steps": traverser.steps}
                
                # logic to determine the outgoing direction
                prev_y, prev_x = traverser.prev
                curr_y, curr_x = traverser.curr
                if prev_y - curr_y < 0 and prev_x == curr_x:
                    outgoing_direction = "u"
                elif prev_y - curr_y > 0 and prev_x == curr_x:
                    outgoing_direction = "d"
                elif prev_x - curr_x < 0 and prev_y == curr_y:
                    outgoing_direction = "l"
                elif prev_x - curr_x > 0 and prev_y == curr_y:
                    outgoing_direction = "r"
                
                # put node and distance into node_dict, the other way around
                if traverser.curr not in node_dict:
                    node_dict[traverser.curr] = {traverser.fromNode: {"direction": outgoing_direction,
                                                                      "steps": traverser.steps}}
                else:
                    node_dict[traverser.curr][traverser.fromNode] = {"direction": outgoing_direction,
                                                                      "steps": traverser.steps}
                
                # spawn new Traversers if needed
                # spawn right Traverser x+1
                if input_list[traverser.curr[0]][traverser.curr[1]+1] != "#" and (traverser.curr not in node_dict or (all(node_dict[traverser.curr][i]["direction"] != 'r' for i in node_dict[traverser.curr]))):
                    traverser_list.append(Traverser(
                        fromNode=traverser.curr,
                        fromDirection="r",
                        prev=(traverser.curr[0], traverser.curr[1]),
                        curr=(traverser.curr[0], traverser.curr[1]+1),
                        steps=1)
                    )
                    print("Spawning new traverser in Right direction")
                # spawn left Traverser x-1
                if input_list[traverser.curr[0]][traverser.curr[1]-1] != "#" and (traverser.curr not in node_dict or (all(node_dict[traverser.curr][i]["direction"] != 'l' for i in node_dict[traverser.curr]))):
                    traverser_list.append(Traverser(
                        fromNode=traverser.curr,
                        fromDirection="l",
                        prev=(traverser.curr[0], traverser.curr[1]),
                        curr=(traverser.curr[0], traverser.curr[1]-1),
                        steps=1)
                    )
                    print("Spawning new traverser in Left direction")
                # spawn up Traverser y-1
                if input_list[traverser.curr[0]-1][traverser.curr[1]] != "#" and (traverser.curr not in node_dict or (all(node_dict[traverser.curr][i]["direction"] != 'u' for i in node_dict[traverser.curr]))):
                    traverser_list.append(Traverser(
                        fromNode=traverser.curr,
                        fromDirection="u",
                        prev=(traverser.curr[0], traverser.curr[1]),
                        curr=(traverser.curr[0]-1, traverser.curr[1]),
                        steps=1)
                    )
                    print("Spawning new traverser in Up direction")
                # spawn down Traverser y+1
                if input_list[traverser.curr[0]+1][traverser.curr[1]] != "#" and (traverser.curr not in node_dict or (all(node_dict[traverser.curr][i]["direction"] != 'd' for i in node_dict[traverser.curr]))):
                    traverser_list.append(Traverser(
                        fromNode=traverser.curr,
                        fromDirection="d",
                        prev=(traverser.curr[0], traverser.curr[1]),
                        curr=(traverser.curr[0]+1, traverser.curr[1]),
                        steps=1)
                    )
                    print("Spawning new traverser in Down direction")


            # check which way is valid
            # up direction
            elif input_list[traverser.curr[0]-1][traverser.curr[1]] == "." and (traverser.curr[0]-1 ,traverser.curr[1]) != traverser.prev:
                traverser.path.append(traverser.curr)
                traverser.prev = traverser.curr
                traverser.curr = (traverser.curr[0]-1 ,traverser.curr[1])
                traverser.steps += 1
            # down direction
            elif input_list[traverser.curr[0]+1][traverser.curr[1]] == "." and (traverser.curr[0]+1 ,traverser.curr[1]) != traverser.prev:
                traverser.path.append(traverser.curr)
                traverser.prev = traverser.curr
                traverser.curr = (traverser.curr[0]+1 ,traverser.curr[1])
                traverser.steps += 1
            # left direction
            elif input_list[traverser.curr[0]][traverser.curr[1]-1] == "." and (traverser.curr[0] ,traverser.curr[1]-1) != traverser.prev:
                traverser.path.append(traverser.curr)
                traverser.prev = traverser.curr
                traverser.curr = (traverser.curr[0] ,traverser.curr[1]-1)
                traverser.steps += 1
            # right direction
            elif input_list[traverser.curr[0]][traverser.curr[1]+1] == "." and (traverser.curr[0] ,traverser.curr[1]+1) != traverser.prev:
                traverser.path.append(traverser.curr)
                traverser.prev = traverser.curr
                traverser.curr = (traverser.curr[0] ,traverser.curr[1]+1)
                traverser.steps += 1

        print(f"Node map: {node_dict}")
        return node_dict

def part_two(input_list):
    map_y = len(input_list)
    map_x = len(input_list[0])
    endpoint = (map_y - 1, map_x - 2)
    print(endpoint)
    traverser = Traverser()
    print(traverser.id)
    traverser_list = []
    traverser_list.append(traverser)
    traverser_step_list=[]
    for traverser in traverser_list:
        if traverser_step_list:
            print(f"[Max:{max(traverser_step_list)}] Starting traverser {traverser.id}...")
        # print(f"Traverser position: {traverser.curr}")
        # print(f"Traverser intersections: {traverser.intersections}")
        while traverser.validity and traverser.curr != endpoint:
            # print(traverser.curr)
            # print(traverser.intersections)
            # first check is that way is surronded by special symbols
            if (traverser.curr in traverser.intersections) and all(
                (input_list[traverser.curr[0]-1][traverser.curr[1]] != ".",
                input_list[traverser.curr[0]+1][traverser.curr[1]] != ".",
                input_list[traverser.curr[0]][traverser.curr[1]-1] != ".",
                input_list[traverser.curr[0]][traverser.curr[1]+1] != ".")
                ):
                print(f"[Deactiavting] Traverser {traverser.id} ran into an intersection travelled before: {traverser.curr}")
                traverser.validity = False
                break

            elif all(
                (input_list[traverser.curr[0]-1][traverser.curr[1]] != ".",
                input_list[traverser.curr[0]+1][traverser.curr[1]] != ".",
                input_list[traverser.curr[0]][traverser.curr[1]-1] != ".",
                input_list[traverser.curr[0]][traverser.curr[1]+1] != ".")
                ):
                print(f"Traverser {traverser.id} ran into an intersection not travelled before: {traverser.curr}")
                intersections = traverser.intersections[:]
                intersections.append(traverser.curr)
                traverser.intersections = intersections

                # up direction
                if input_list[traverser.curr[0]-1][traverser.curr[1]] != "#" and (traverser.curr[0]-1 ,traverser.curr[1]) != traverser.prev:
                    traverser_list.append(Traverser(
                        path=traverser.path,
                        intersections=traverser.intersections,
                        prev=(traverser.curr[0]-1, traverser.curr[1]),
                        curr=(traverser.curr[0]-2, traverser.curr[1]),
                        steps=traverser.steps+2)
                    )
                    print("Spawning new traverser in Up direction")
                # down direction
                if input_list[traverser.curr[0]+1][traverser.curr[1]] != "#" and (traverser.curr[0]+1 ,traverser.curr[1]) != traverser.prev:
                    traverser_list.append(Traverser(
                        path=traverser.path,
                        intersections=traverser.intersections,
                        prev=(traverser.curr[0]+1, traverser.curr[1]),
                        curr=(traverser.curr[0]+2, traverser.curr[1]),
                        steps=traverser.steps+2)
                    )
                    print("Spawning new traverser in Down direction")
                # left direction
                if input_list[traverser.curr[0]][traverser.curr[1]-1] != "#" and (traverser.curr[0] ,traverser.curr[1]-1) != traverser.prev:
                    traverser_list.append(Traverser(
                        path=traverser.path,
                        intersections=traverser.intersections,
                        prev=(traverser.curr[0], traverser.curr[1]-1),
                        curr=(traverser.curr[0], traverser.curr[1]-2),
                        steps=traverser.steps+2)
                    )
                    print("Spawning new traverser in Left direction")
                # right direction
                if input_list[traverser.curr[0]][traverser.curr[1]+1] != "#" and (traverser.curr[0] ,traverser.curr[1]+1) != traverser.prev:
                    traverser_list.append(Traverser(
                        path=traverser.path,
                        intersections=traverser.intersections,
                        prev=(traverser.curr[0], traverser.curr[1]+1),
                        curr=(traverser.curr[0], traverser.curr[1]+2),
                        steps=traverser.steps+2)
                    )
                    print("Spawning new traverser in Right direction")

                traverser.validity = False
                print(f"Deactivating traverser {traverser.id}")
                break

            # check which way is valid
            # up direction
            elif input_list[traverser.curr[0]-1][traverser.curr[1]] in (".", "v") and (traverser.curr[0]-1 ,traverser.curr[1]) != traverser.prev:
                traverser.path.append(traverser.curr)
                traverser.prev = traverser.curr
                traverser.curr = (traverser.curr[0]-1 ,traverser.curr[1])
                traverser.steps += 1
            # down direction
            elif input_list[traverser.curr[0]+1][traverser.curr[1]] in (".", "v") and (traverser.curr[0]+1 ,traverser.curr[1]) != traverser.prev:
                traverser.path.append(traverser.curr)
                traverser.prev = traverser.curr
                traverser.curr = (traverser.curr[0]+1 ,traverser.curr[1])
                traverser.steps += 1
            # left direction
            elif input_list[traverser.curr[0]][traverser.curr[1]-1] in (".", ">") and (traverser.curr[0] ,traverser.curr[1]-1) != traverser.prev:
                traverser.path.append(traverser.curr)
                traverser.prev = traverser.curr
                traverser.curr = (traverser.curr[0] ,traverser.curr[1]-1)
                traverser.steps += 1
            # right direction
            elif input_list[traverser.curr[0]][traverser.curr[1]+1] in (".", ">") and (traverser.curr[0] ,traverser.curr[1]+1) != traverser.prev:
                traverser.path.append(traverser.curr)
                traverser.prev = traverser.curr
                traverser.curr = (traverser.curr[0] ,traverser.curr[1]+1)
                traverser.steps += 1
        if traverser.validity and traverser.curr == endpoint:
            print(f"Traverser {traverser.id} arrived at terminal with steps: {traverser.steps}")
            traverser_step_list.append(traverser.steps)
    return sorted(traverser_step_list)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("AAC 2023 Day 22")
    parser.add_argument("file", help="Path to input file")
    args = parser.parse_args()
    input_list = read_list(args.file)
    print(*input_list, sep="\n")
    # traverser_step_list_one = part_one(input_list=input_list)
    # print(traverser_step_list_one)
    traverser_step_list_two = build_map(input_list=input_list)
    print(traverser_step_list_two)