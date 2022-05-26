#
# @lc app=leetcode id=1779 lang=python3
#
# [1779] Find Nearest Point That Has the Same X or Y Coordinate
#

# @lc code=start
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index, min_dist = -1, float('inf')

        for i, (px, py) in enumerate(points):
            dx, dy = px - x, py - y
            if dx * dy == 0:
                dist = abs(dx + dy)
                if dist < min_dist:
                    index = i
                    min_dist = dist

        return index
# @lc code=end

