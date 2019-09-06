def dfs(temp, i, j, visited, matrix):
    visited[i][j] = True
    temp.append(matrix[i][j])
    l = len(matrix)

    adj = []    
    
    if i > 0 and j > 0 and matrix[i-1][j-1] == 1:
        adj.append((i-1, j-1))
    if i > 0 and matrix[i-1][j] == 1:
        adj.append((i-1, j))
    if i > 0 and j < l-1 and matrix[i-1][j+1] == 1:
        adj.append((i-1, j+1))
    if j > 0 and matrix[i][j-1] == 1:
        adj.append((i, j-1))
    if j < l-1 and matrix[i][j+1] == 1:
        adj.append((i, j+1))
    if i < i-1 and j > 0 and matrix[i+1][j-1] == 1:
        adj.append((i+1, j-1))
    if i < l-1 and matrix[i+1][j] == 1:
        adj.append((i+1, j))
    if i < l-1 and j < l-1 and matrix[i+1][j+1] == 1:
        adj.append((i+1, j+1))
    
    for elem in adj:
        if visited[elem[0]][elem[1]] == False:
            temp = dfs(temp, elem[0], elem[1], visited, matrix)
    
    return temp

def connectedCells(matrix):
    cc = []
    l = len(matrix)

    for i in range(l):
        for j in range(l):
            if matrix[i][j] == 1 and visited[i][j] == False:
                temp = []
                cc.append(dfs(temp, i, j, visited, matrix))
    
    maxlen  = 0
    for elem in cc:
        maxlen = max(maxlen, len(elem))

    return maxlen



matrix = [[0 for x in range(3)] for y in range(3)]
visited = [[False for x in range(3)] for y in range(3)]

matrix[0][0] = 1
matrix[0][1] = 1
matrix[1][0] = 1
matrix[2][2] = 1

print(connectedCells(matrix))