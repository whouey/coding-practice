#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
from typing import List

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_volume = 0
        i, j = 0, len(height)-1

        while i<j:

            if height[i] < height[j]:
                volume = (j-i) * height[i]
                i += 1
            else:
                volume = (j-i) * height[j]
                j -= 1
            
            if volume > max_volume:
                max_volume = volume
        
        return max_volume
# @lc code=end

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))