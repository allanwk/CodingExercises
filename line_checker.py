d_table = {
    '-':[0,1,0,1],
    '|':[1,0,1,0],
    '+':[1,1,1,1],
    'X':[1,1,1,1],
    ' ':[0,0,0,0]
}

paths = []

def explore(x, y, grid, explored, came_from, n_paths, n_deadends):
    if grid[y][x] == 'X':
        for pos in explored:
            if grid[pos[1]][pos[0]] == 'X':
                print("Found path", x, y, grid[y][x])
                n_paths += 1
                paths.append(explored + [(x,y)])
                return (n_paths, n_deadends)
    print(grid[y][x], x, y)
    disabled = ''
    if grid[y][x] == '+':
        if came_from == 'top':
            disabled = 'bottom'
        elif came_from == 'bottom':
            disabled = 'top'
        elif came_from == 'right':
            disabled = 'left'
        elif came_from == 'left':
            disabled = 'right'
    deadEnd = True
    if y-1 >= 0 and disabled != 'top':
        if d_table[grid[y][x]][0] == 1 and d_table[grid[y-1][x]][2] == 1 and (x,y-1) not in explored:
            n_paths, n_deadends = explore(x,y-1,grid,explored + [(x,y)],'bottom', n_paths, n_deadends)
            deadEnd = False
    if x+1 < len(grid[0]) and disabled != 'right':
        if d_table[grid[y][x]][1] == 1 and d_table[grid[y][x+1]][3] == 1 and (x+1,y) not in explored:
            n_paths, n_deadends = explore(x+1,y,grid,explored + [(x,y)],'left', n_paths, n_deadends)
            deadEnd = False
    if y+1 < len(grid) and disabled != 'bottom':
        if d_table[grid[y][x]][2] == 1 and d_table[grid[y+1][x]][0] == 1 and (x,y+1) not in explored:
            n_paths, n_deadends = explore(x,y+1,grid,explored + [(x,y)],'top', n_paths, n_deadends)
            deadEnd = False
    if x-1 >= 0 and disabled != 'left':
        if d_table[grid[y][x]][3] == 1 and d_table[grid[y][x-1]][1] == 1 and (x-1,y) not in explored:
            n_paths, n_deadends = explore(x-1,y,grid,explored + [(x,y)],'right', n_paths, n_deadends)
            deadEnd = False
    if deadEnd and grid[y][x] != 'X':
        n_deadends += 1
    return (n_paths, n_deadends)

def line(grid):
    paths.clear()
    xpositions = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "X":
                xpositions.append((x,y))

    n_paths1, n_deadends1 = explore(xpositions[0][0], xpositions[0][1], grid, [], None, 0, 0)
    n_paths2, n_deadends2 = explore(xpositions[1][0], xpositions[1][1], grid, [], None, 0, 0)
    print(n_paths1, n_paths2, n_deadends1, n_deadends2)
    
    #Find at least one direction where theres only one path,
    #no deadends and has explored all tiles
    
    #Get the union of all paths
    union = set()
    for p in paths:
        for pos in p:
            union.add(pos)
    
    if (n_paths1 == 1 and n_deadends1 == 0) or (n_paths2 == 1 and n_deadends2 == 0):
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] != ' ' and (x,y) not in union:
                    return False
        return True
    return False
    

grid = ["X-----+",  
        "      |",  
        "X-----+",  
        "      |",  
        "------+" ]
print(line(grid))