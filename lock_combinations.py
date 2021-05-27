import numpy as np

graph = np.array([
    [0,1,2,1,1,1,2,1,2],
    [1,0,1,1,1,1,1,2,1],
    [2,1,0,1,1,1,2,1,2],
    [1,1,1,0,1,2,1,1,1],
    [1,1,1,1,0,1,1,1,1],
    [1,1,1,2,1,0,1,1,1],
    [2,1,2,1,1,1,0,1,2],
    [1,2,1,1,1,1,1,0,1],
    [2,1,2,1,1,1,2,1,0],
])

points = 'ABCDEFGHI'

overlap_condition = {
    (0,2) : 1,
    (0,6) : 3,
    (0,8) : 4,
    (1,7) : 4,
    (2,6) : 4,
    (2,8) : 5,
    (3,5) : 4,
    (6,8) : 7
}

class Node:
    def __init__(self, info):
        self.leaves = []
        self.info = info

def fill(node, d, max_depth, path, count):
    if d == max_depth:
        return count + 1
    for i in range(9):
        if i != node.info and i not in path:
            if(graph[node.info][i] == 1):
                node.leaves.append(Node(i))
                count = fill(node.leaves[-1], d+1, max_depth, path + [i], count)
            else:
                if node.info > i:
                    selector = (i, node.info)
                else:
                    selector = (node.info, i)
                if overlap_condition[selector] in path:
                    node.leaves.append(Node(i))
                    count = fill(node.leaves[-1], d+1, max_depth, path + [i], count)
    return count
                
    
def rprint(node, d):
    space = " "*d
    print(space, points[node.info])
    for leaf in node.leaves:
        rprint(leaf, d+1)

def countPatternsFrom(firstPoint, length):
    point = points.index(firstPoint)
    root = Node(point)
    print(fill(root, 0, length - 1, [point], 0))
    #rprint(root, 0)