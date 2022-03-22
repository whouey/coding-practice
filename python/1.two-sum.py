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
        for idx, num in enumerate(nums):
            diff = target-num
            for i in range(idx+1, len(nums)):
                if nums[i]==diff:
                    return [idx, i]
# @lc code=end

#%%
print(Solution().twoSum([2,7,15,19], 9))