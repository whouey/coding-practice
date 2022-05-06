#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(m):
            grid[0][i] = 1
        for i in range(n):
            grid[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        return grid[n-1][m-1]

# @lc code=end

