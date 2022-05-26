#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.width, self.height = len(grid), len(grid[0])
        max_area = 0

        for i in range(self.width):
            for j in range(self.height):
                    area = self._islandArea(grid, i, j)
                    if area > max_area:
                        max_area = area

        return max_area

    def _islandArea(self, grid, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height and grid[x][y]):
            return 0

        grid[x][y] = 0
        area = 1
        for (dx, dy) in self.directions:
            area += self._islandArea(grid, x+dx, y+dy)

        return area
  
# @lc code=end

# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#         width, height = len(grid), len(grid[0])
#         max_area = 0

#         for i in range(width):
#             for j in range(height):
#                 if grid[i][j]:
#                     grid[i][j] = 0
#                     area = 1
#                     exploration = [(i+dx, j+dy) for (dx, dy) in directions]

#                     while(exploration):
#                         x, y = exploration.pop()

#                         if 0 <= x < width and 0 <= y < height and grid[x][y]:
#                             grid[x][y] = 0
#                             area += 1
#                             exploration.extend([(x+dx, y+dy) for (dx, dy) in directions])

#                     if area > max_area:
#                         max_area = area

#         return max_area