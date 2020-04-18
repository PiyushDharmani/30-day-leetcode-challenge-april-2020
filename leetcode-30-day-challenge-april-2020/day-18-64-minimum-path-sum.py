class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
# DP solution - modifying orignal array
        row = len(grid)
        col = len(grid[0])

        for i in range(1,col):
            grid[0][i] += grid[0][i-1]

        for j in range(1,row):
            grid[j][0] += grid[j-1][0]

        for i in range(1,row):
            for j in range(1,col):
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])

        print(grid)

        return grid[row-1][col-1]






#         Recursive solution - from 0,0 to destination - DFS
#         n = len(grid)-1
#         m = len(grid[0])-1

#         def minCostPath(grid, i, j):
#             if i==n and j==m:
#                 return grid[i][j]
#             elif i > n or j > m:
#                 return float('inf')
#             else:
#                 return grid[i][j] + min(minCostPath(grid, i+1, j),minCostPath(grid, i, j+1))
#         return minCostPath(grid, 0, 0)
