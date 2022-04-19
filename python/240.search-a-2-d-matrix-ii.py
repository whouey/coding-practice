#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0] == target
        
        y = len(matrix) // 2
        x = 0
        while(matrix[y][x] < target and x+1 < len(matrix[y])):
            x += 1
        
        if matrix[y][x] == target:
            return True
        elif matrix[y][x] < target:
            return self.searchMatrix([row[x:] for row in matrix[y:]], target) or \
                    self.searchMatrix([row[:x] for row in matrix[y:]], target) or \
                    self.searchMatrix([row[x:] for row in matrix[:y]], target)
        else:
            return self.searchMatrix([row[:x] for row in matrix[:y]], target) or \
                    self.searchMatrix([row[:x] for row in matrix[y:]], target) or \
                    self.searchMatrix([row[x:] for row in matrix[:y]], target)
# @lc code=end

