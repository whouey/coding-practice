#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, cnt = nums[0], 1
        for i in range(1, len(nums)):
            if res == nums[i]:
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                res = nums[i]
                cnt = 1
        return res
# @lc code=end

