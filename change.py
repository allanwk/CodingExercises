class Node:
    def __init__(self, info):
        self.leaves = []
        self.info = info

def fill(node, d, coins, sum, wanted):
    sum += node.info
    if(sum >= wanted):
        if sum == wanted:
            solutions[0] += 1
        return
    for coin in coins:
        if coin >= node.info and sum + coin <= wanted:
            node.leaves.append(Node(coin))
            fill(node.leaves[-1], d+1, coins, sum, wanted)

solutions = [0]

def count_change(money, coins):
    solutions[0] = 0
    wanted = money
    coins.sort()
    root = Node(0)
    fill(root, 0, coins, 0, money)
    return solutions[0]

print(count_change(419, [2, 5, 10, 20, 50]))
