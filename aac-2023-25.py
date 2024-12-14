import argparse
import pprint
import random
import math

def read_list(filepath):
    with open(filepath, "r") as fp:
        return fp.read().splitlines()
    
def create_graph(input_list):
    result = {}
    for line in input_list:
        from_node = line.split(":")[0]
        to_nodes = line.split(":")[1].split(" ")[1:]
        # print(from_node, to_nodes)
        for to_node in to_nodes:
            if from_node not in result:
                result[from_node] = [to_node]
            else:
                result[from_node].append(to_node)

            if to_node not in result:
                result[to_node] = [from_node]
            else:
                result[to_node].append(from_node)
    # pprint.pprint(result)
    return result


# https://www.geeksforgeeks.org/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/
def BFS_SP(graph, start, goal):
    explored = []
     
    # Queue for traversing the 
    # graph in the BFS
    queue = [[start]]
     
    # If the desired node is 
    # reached
    if start == goal:
        print("Same Node")
        return None
     
    # Loop to traverse the graph 
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
         
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]
             
            # Loop to iterate over the 
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                 
                # Condition to check if the 
                # neighbour node is the goal
                if neighbour == goal:
                    # print("Shortest path = ", *new_path)
                    return new_path
            explored.append(node)
 
    # Condition when the nodes 
    # are not connected
    print("So sorry, but a connecting"\
                "path doesn't exist :(")
    return None


if __name__ == "__main__":
    print("Starting script for aac-2023-25")
    parser = argparse.ArgumentParser(description="C")
    parser.add_argument("file", help="path to .txt")
    args = parser.parse_args()
    input_list = read_list(args.file)

    unfixed_graph = create_graph(input_list)

    unfixed_graph_keys_list = list(unfixed_graph.keys())

    monte_carlo_dict = {}

    for i in range(300):
        # print(i)
        from_node, to_node = random.sample(unfixed_graph_keys_list, 2)
        # print(from_node,to_node)
        bfs_result = BFS_SP(unfixed_graph, from_node, to_node)
        # print(bfs_result)
        
        for i in range(len(bfs_result)-1):
            if (bfs_result[i], bfs_result[i+1]) in monte_carlo_dict:
                monte_carlo_dict[(bfs_result[i], bfs_result[i+1])] += 1
            else:
                monte_carlo_dict[(bfs_result[i], bfs_result[i+1])] = 1

            if (bfs_result[i+1], bfs_result[i]) in monte_carlo_dict:
                monte_carlo_dict[(bfs_result[i+1], bfs_result[i])] += 1
            else:
                monte_carlo_dict[(bfs_result[i+1], bfs_result[i])] = 1
    
    # pprint.pprint(monte_carlo_dict)
    sorted_monte_carlo_dict = sorted(monte_carlo_dict.items(), key=lambda item: item[1], reverse=True)
    pprint.pprint(sorted_monte_carlo_dict[:10])

    fixed_graph = unfixed_graph.copy()

    # remove extra edges from graph
    for i in range(6):
        fixed_graph[sorted_monte_carlo_dict[i][0][0]].remove(sorted_monte_carlo_dict[i][0][1])
    
    # try a set number of times, take the highest two values and multiply them
    result_set = set()
    for tries in range(10):
        start_node = random.choice(unfixed_graph_keys_list)
        node_set = set()
        node_set.add(start_node)
        queue = []
        checked = []
        queue.append(start_node)
        checked.append(start_node)
        while queue:
            next_node = queue.pop(0)
            for node in fixed_graph[next_node]:
                node_set.add(node)

                if node not in checked:
                    checked.append(node)
                    queue.append(node)
        print(len(node_set))
        result_set.add(len(node_set))

    print("Part one:", math.prod(result_set))
    