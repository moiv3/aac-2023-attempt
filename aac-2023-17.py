import argparse

def read_list(filepath):
    with open(filepath, "r") as fp:
        return fp.read().splitlines()
    
def parse_list(input_strings):
    grid = [[int(x) for x in row] for row in input_strings]
    return grid
    
# the following is a type-along with Reddit tutorial:
# https://www.reddit.com/r/adventofcode/comments/18luw6q/2023_day_17_a_longform_tutorial_on_day_17/

# 操作 state_queues_by_cost, seen_cost_by_state兩個重要dict的function
# 如果(x, y)有看過，什麼都不做
# 如果(x, y)沒有看過，登錄到state_queues_by_cost裡面，在標記為有看過
def add_state(cost, x, y):
    if x < 0 or y < 0:
        return
    if x >= len(input_grid[0]) or y >= len(input_grid):
        return
    
    new_cost = cost + input_grid[y][x]

    if x == end_x and y == end_y:
        print("Found end:", new_cost)
        exit()

    state = (x, y)

    if state not in seen_cost_by_state:
        state_queues_by_cost.setdefault(new_cost, []).append(state)
        seen_cost_by_state[state] = new_cost

def move_and_add_state(cost, x, y, dx, dy, distance, part):

    x += dx
    y += dy

    if x < 0 or y < 0:
        return
    if x >= len(input_grid[0]) or y >= len(input_grid):
        return
    
    new_cost = cost + input_grid[y][x]

    if x == end_x and y == end_y:
        # part one
        if part == 1:
            print("Got to end, min cost is:", new_cost)
            exit()

        # part two
        elif part == 2:
            if distance >= 4:
                print("Got to end, min cost is:", new_cost)
                raise SystemExit()
            else:
                return
            
        else:
            raise Exception("Question Part number invalid!")

    # 1st version
    # state = (x, y)
    # 2nd version
    state = (x, y, dx, dy, distance)

    if state not in seen_cost_by_state:
        state_queues_by_cost.setdefault(new_cost, []).append(state)
        seen_cost_by_state[state] = new_cost

if __name__ == "__main__":
    parser = argparse.ArgumentParser("AAC-2023-Day17")
    parser.add_argument("file", help="path to the txt file")
    args = parser.parse_args()
    input_list = read_list(args.file)
    input_grid = parse_list(input_list)
    print(input_grid)

    # width(x) and height(y) and their ending states
    y = len(input_grid)
    x = len(input_grid[0])

    end_x = x - 1
    end_y = y - 1

    # initialize data structures (also add comments about what they do)
    # 排隊中待處理的states, 依照cost是多少分類
    # initialization: state_queues_by_cost.setdefault(new_cost, []).append(state)
    # .setdefault method is a dict method, looks useful: https://www.w3schools.com/python/ref_dictionary_setdefault.asp
    state_queues_by_cost = {}
    # 已知的state(去過的格子)，記錄其cost / "我知道這格要多少cost"的dict. Record the cost for each seen state.
    seen_cost_by_state = {}
    
    
    # initialize
    move_and_add_state(cost=0, x=0, y=0, dx=1, dy=0, distance=1, part=1)
    move_and_add_state(cost=0, x=0, y=0, dx=0, dy=1, distance=1, part=1)

    # while True:
    for i in range(10000):
        print(i)
        # start with the lowest cost
        current_cost = min(state_queues_by_cost.keys())

        # pop in a dict pops the key/value and returns the value
        next_states = state_queues_by_cost.pop(current_cost)

        for state in next_states:
            # 1st version initialize
            # (x, y) = state
            # 2nd version initialize
            (x, y, dx, dy, distance) = state

            # part one
            # 2nd version: turn left, turn right
            move_and_add_state(cost=current_cost, x=x, y=y, dx=dy, dy=-dx, distance=1, part=1)
            move_and_add_state(cost=current_cost, x=x, y=y, dx=-dy, dy=dx, distance=1, part=1)

            # add option to go straight if distance < 3
            if distance < 3:
                move_and_add_state(cost=current_cost, x=x, y=y, dx=dx, dy=dy, distance=distance+1, part=1)

            # part two, remove comments to run
            # distance < 4 / 4~10 / > 10
            # if distance < 4:
            #     move_and_add_state(cost=current_cost, x=x, y=y, dx=dx, dy=dy, distance=distance+1, part=2)
            # elif distance < 10:
            #     move_and_add_state(cost=current_cost, x=x, y=y, dx=dy, dy=-dx, distance=1, part=2)
            #     move_and_add_state(cost=current_cost, x=x, y=y, dx=-dy, dy=dx, distance=1, part=2)
            #     move_and_add_state(cost=current_cost, x=x, y=y, dx=dx, dy=dy, distance=distance+1, part=2)
            # else:
            #     move_and_add_state(cost=current_cost, x=x, y=y, dx=dy, dy=-dx, distance=1, part=2)
            #     move_and_add_state(cost=current_cost, x=x, y=y, dx=-dy, dy=dx, distance=1, part=2)
