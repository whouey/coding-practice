#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
from typing import List

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []

        nums.sort()

        res = set()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            d = set()
            for j in range(i+1, len(nums)):
                if nums[j] not in d:
                    d.add(-nums[i]-nums[j]) # add complement
                else:
                    res.add((nums[i], -nums[i]-nums[j], nums[j]))

        return list(res)
        
# @lc code=end

