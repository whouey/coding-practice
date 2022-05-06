#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
from functools import reduce
from operator import xor

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)
# @lc code=end

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         return reduce(lambda acc, x: acc^x, nums)