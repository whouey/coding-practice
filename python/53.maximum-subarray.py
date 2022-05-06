#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        local_max = global_max = nums[0]

        for i in range(1, len(nums)):
            
            if nums[i] > nums[i] + local_max:
                local_max = nums[i]
            else:
                local_max += nums[i]

            if local_max > global_max:
                global_max = local_max 

        return global_max

# @lc code=end

