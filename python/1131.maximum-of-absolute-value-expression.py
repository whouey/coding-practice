#
# @lc app=leetcode id=1131 lang=python3
#
# [1131] Maximum of Absolute Value Expression
#
from typing import List

# @lc code=start
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        max_value = 0

        for x, y in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            distances = [x * arr1[i] + y * arr2[i] + i for i in range(len(arr1))]
            max_value = max(max_value, max(distances) - min(distances))

        return max_value
# @lc code=end

print(Solution().maxAbsValExpr([1,2,3,4], [-1,4,5,6]))
print(Solution().maxAbsValExpr([1,-2,-5,0,10], [0,-2,-1,-7,-4]))