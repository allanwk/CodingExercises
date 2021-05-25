def connect(n1, n2 , subgraphs):
    n1hasSubgraph = False
    n2hasSubgraph = False
    n1Subgraph = 0
    n2Subgraph = 0
    for a in range(len(subgraphs)):
        for i in range(len(subgraphs[a])):
            if subgraphs[a][i] == n1:
                n1hasSubgraph = True
                n1Subgraph = a
            if subgraphs[a][i] == n2:
                n2hasSubgraph = True
                n2Subgraph = a
            if n1hasSubgraph and n2hasSubgraph:
                break
    if not n1hasSubgraph and not n2hasSubgraph:
        subgraphs.append([n1, n2])
    elif n1hasSubgraph and not n2hasSubgraph:
        subgraphs[n1Subgraph].append(n2)
    elif n2hasSubgraph and not n1hasSubgraph:
        subgraphs[n2Subgraph].append(n1)
    elif n1Subgraph != n2Subgraph:
        merged = subgraphs[n1Subgraph] + subgraphs[n2Subgraph]
        if n1Subgraph > n2Subgraph:
            subgraphs.pop(n1Subgraph)
            subgraphs.pop(n2Subgraph)
        else:
            subgraphs.pop(n2Subgraph)
            subgraphs.pop(n1Subgraph)
        subgraphs.append(merged)

def components(grid):
    subgraphs = []
    width = grid.index('|')
    onFirstLine = True
    counter = 0
    for i in range(len(grid)):
        if grid[i] == '|':
            onFirstLine = False
        if grid[i] == '+' and onFirstLine == False and i != len(grid)-1:
            if(grid[i+1] != '\n'):
                counter += 1
    adj = [[0 for i in range(counter)]for j in range(counter)]
    onFirstLine = True
    counter = 0
    for i in range(len(grid)):
        if grid[i] == '|':
            onFirstLine = False
        if grid[i] == '+' and onFirstLine == False and i != len(grid)-1:
            if(grid[i+1] != '\n'):
                counter += 1
                if(grid[i-width] == ' '):
                    connect(counter, counter - 1, subgraphs)
                if(grid[i+1] == ' '):
                    connect(counter, counter + (width//3), subgraphs)
                if(grid[i-width] == '|'and grid[i+1] == '-' and grid[i+1-(width*2)] == '-'):
                    subgraphs.append([counter])      
    comps = {}
    for subgraph in subgraphs:
        l = len(subgraph)
        if l not in comps:
            comps[l] = 0
        comps[l] += 1
    return sorted(list(comps.items()), reverse=True, key=lambda tup: tup[0])

print(components('''\
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|        |           |           |           |        |  |  |
+  +--+  +  +--+--+--+--+  +  +--+--+  +--+--+  +  +  +  +  +
|  |  |  |              |  |  |  |  |     |  |           |  |
+  +--+  +  +  +  +--+--+  +--+  +  +  +--+--+  +  +  +  +  +
|        |  |     |  |     |     |  |     |     |        |  |
+--+--+--+--+  +--+  +  +--+  +  +  +  +--+  +--+  +--+--+--+
|     |  |        |     |     |           |  |     |  |     |
+--+--+--+  +  +  +  +--+  +  +  +--+--+  +  +--+--+--+  +  +
|  |  |     |           |  |     |        |        |  |     |
+  +  +  +  +  +--+--+  +--+  +--+--+--+--+--+--+--+--+  +--+
|  |                    |           |              |        |
+--+--+--+  +  +--+--+--+--+  +  +--+--+--+  +--+--+  +  +  +
|        |        |  |     |              |  |  |     |  |  |
+--+--+--+  +  +--+  +  +--+--+--+  +--+  +--+  +  +--+  +--+
|        |     |  |  |           |        |     |  |  |     |
+--+--+--+--+--+  +--+  +--+  +  +--+--+--+  +  +  +  +  +--+
|           |        |        |  |        |     |  |  |     |
+  +  +--+--+--+  +--+  +  +  +  +  +  +  +--+  +--+  +--+  +
|     |  |  |                 |           |     |     |     |
+--+  +  +  +--+  +--+--+  +  +  +--+  +--+--+--+--+  +  +--+
|  |  |           |  |  |     |           |     |     |  |  |
+--+--+  +--+--+--+--+  +--+--+  +  +--+  +--+--+--+  +--+--+
|  |  |        |  |     |  |  |     |  |  |        |  |     |
+  +  +--+--+--+  +--+--+--+  +--+  +--+--+  +  +  +--+--+  +
|  |                 |  |  |     |  |     |        |     |  |
+  +  +  +  +  +--+  +  +  +--+  +  +  +--+  +--+--+  +  +--+
|  |  |  |        |     |  |  |  |        |        |        |
+  +  +--+--+  +  +--+  +  +  +--+  +  +--+  +--+--+--+  +  +
|  |           |  |  |  |  |  |  |                    |     |
+--+--+  +--+  +  +--+  +  +  +--+  +  +--+  +  +  +--+--+--+
|        |        |  |        |     |                 |  |  |
+  +  +--+  +--+--+--+  +  +  +  +--+--+--+  +--+--+--+--+  +
|     |  |  |        |  |  |  |  |  |        |  |     |  |  |
+  +--+  +  +--+--+  +--+--+--+  +  +  +--+  +  +  +--+  +  +
|  |                    |  |  |  |  |     |  |     |     |  |
+--+--+--+  +--+--+--+--+--+--+  +  +  +--+--+  +  +--+--+--+
|     |              |  |        |  |     |        |        |
+  +  +  +  +  +  +--+  +  +  +--+  +--+  +--+--+--+  +  +  +
|  |           |     |        |  |  |           |  |     |  |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+'''))