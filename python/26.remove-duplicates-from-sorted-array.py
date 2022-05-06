#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        for j in range(i+1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]


        return i+1
            
# @lc code=end

