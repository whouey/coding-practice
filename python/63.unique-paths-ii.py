#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        path = [[0 for _ in range(n)] for _ in range(m)]
        path[0][0] = 1

        for i in range(1, m):
            if not obstacleGrid[i][0]:
                path[i][0] = path[i-1][0]
        
        for j in range(1, n):
            if not obstacleGrid[0][j]:
                path[0][j] = path[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]:
                    path[i][j] = path[i-1][j] + path[i][j-1]

        return path[-1][-1]

# @lc code=end

