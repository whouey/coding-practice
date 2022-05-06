#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        s1, s2 = 1, 2

        for _ in range(n-2):
            s1, s2 = s2, s1 + s2

        return s2

# @lc code=end


# from functools import cache

# class Solution:
#     @cache
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n

#         return self.climbStairs(n-1) + self.climbStairs(n-2)