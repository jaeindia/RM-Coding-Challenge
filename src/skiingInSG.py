'''
Created on Oct 19, 2015

@author: Jayakumar
'''
#!/usr/bin/python

grid = [] # Map

firstLineFlag = True

with open('../Input/Map.txt', 'r') as f:
    for line in f:
        line = line.strip()
        
        if len(line) > 0 and not firstLineFlag:
            grid.append(map(int, line.split(' ')))
        
        firstLineFlag = False

row = len(grid)
col = len(grid[0])

print "row " + str(row) + "\n"
print "col " + str(col) + "\n"

lds = []  # Longest Decreasing Sequence

for i in range(row):
    lds.append([0 for x in grid[0]])

# Find the length of the longest decreasing sequence for each element in the Map 
def fillMaxPathLength(i, j):
    if lds[i][j] != 0:
        return lds[i][j]
    flag = False
    (up, down, left, right) = (0, 0, 0, 0)
    if (i < row - 1) and (grid[i][j] > grid[i + 1][j]):
        down = fillMaxPathLength(i + 1, j)
        flag = True
    if (j < col - 1) and (grid[i][j] > grid[i][j + 1]):
        right = fillMaxPathLength(i, j + 1)
        flag = True
    if (i > 0) and (grid[i][j] > grid[i - 1][j]):
        up = fillMaxPathLength(i - 1, j)
        flag = True
    if (j > 0) and (grid[i][j] > grid[i][j - 1]):
        left = fillMaxPathLength(i, j - 1)
        flag = True
    if not flag:
        return 0
    else:
        lds[i][j] = max(up, down, left, right) + 1
        return lds[i][j]

# Get the longest decreasing sequence
def getSequence(k, i, j):
    c = grid[i][j]
    
    if k == 0:
        path.append(c)
        return str(c)
    if (i < row - 1) and (lds[i][j] == lds[i + 1][j] + 1):
        path.append(c)
        return str(c) + ' ' + getSequence(k - 1, i + 1, j)
    if (j < col - 1) and (lds[i][j] == lds[i][j + 1] + 1):
        path.append(c)
        return str(c) + ' ' + getSequence(k - 1, i, j + 1)
    if (i > 0) and (lds[i][j] == lds[i - 1][j] + 1):
        path.append(c)
        return str(c) + ' ' + getSequence(k - 1, i - 1, j)
    if (j > 0) and (lds[i][j] == lds[i][j - 1] + 1):
        path.append(c)
        return str(c) + ' ' + getSequence(k - 1, i, j - 1)

# Main routine    
def solve():
    for i in range(row):
        for j in range(col):
            if lds[i][j] == 0:
                fillMaxPathLength(i, j)
                
    maxPathLength = 0
    for i in range(row):
        for j in range(col):
            if maxPathLength < lds[i][j]:
                maxPathLength = lds[i][j]
    
    global path  # Path Sequence Container
    path = []
                
    for i in range(row):
        for j in range(col):
            if lds[i][j] == maxPathLength:
                print "Longest Ski Run ....\n"
                print getSequence(maxPathLength, i, j) + "\n"
                print "Length " + str(len(path)) + "\n"
                print "Drop " + str(path[0]) + " - " + str(path[len(path) - 1]) + "\t" + str(path[0] - path[len(path) - 1]) + "\n"
                path = []
        
# Main call
solve()
