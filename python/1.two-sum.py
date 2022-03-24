#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

#%%
from typing import List

#%%
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        for idx, num in enumerate(nums):
            if num in hash:
                return [hash[num], idx]
            else:
                diff = target - num
                hash[diff] = idx
# @lc code=end

#%%
print(Solution().twoSum([2,7,15,19], 9))