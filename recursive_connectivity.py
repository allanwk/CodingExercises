def explore(pos, came_from, grid, width, explored):
    explored.append(pos)
    if grid[pos-1] == ' ' and came_from != 'left' and pos-3 not in explored:
        explored = explore(pos-3, 'right', grid, width, explored)
    if grid[pos+2] == ' ' and came_from != 'right' and pos+3 not in explored:
        explored = explore(pos+3, 'left', grid, width, explored)
    if grid[pos-width] == ' ' and came_from != 'top' and pos-(width*2) not in explored:
        explored = explore(pos-(width*2), 'bottom', grid, width, explored)
    if grid[pos+width] == ' ' and came_from != 'bottom' and pos+(width*2) not in explored:
        explored = explore(pos+(width*2), 'top', grid, width, explored)
    return explored


def components(grid):
    subgraphs = []
    visited = []
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
                if(i+1-width not in visited):
                    explored = explore(i+1-width, "", grid, width, [])
                    visited += explored
                    subgraphs.append(explored)
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