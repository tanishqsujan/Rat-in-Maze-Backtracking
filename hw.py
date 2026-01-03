def countpath(maze, i, j, m, n):
    if i == m - 1 and j == n - 1:
        return 1
    
    if i >= m or j >= n or maze[i][j] == 0:
        return 0
    
    rightpath = countpath(maze, i, j + 1, m, n)
    
    downpath = countpath(maze, i + 1, j, m, n)
    
    return rightpath + downpath

maze = [[1, 1, 0, 0],
        [1, 1, 1, 1],
        [0, 1, 0, 1],
        [1, 1, 1, 1]]

m = len(maze)
n = len(maze[0])

print("Number of ways: ", countpath(maze, 0, 0, m, n))