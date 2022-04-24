#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

from typing import List

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l, r, target = 0, len(nums)-1, len(nums)-k
        
        while l < r:
            mid = self.quickSelect(nums, l, r)
            if mid == target:
                return nums[mid]
            elif mid < target:
                l = mid + 1
            else:
                r = mid - 1
            
        return nums[l]
    
    def quickSelect(self, nums, l, r):
        i, j = l+1, r
        
        while True:
            while i < r and nums[i] <= nums[l]:
                i += 1
            while l < j and nums[j] >= nums[l]:
                j -= 1
            
            if i >= j:
                break
                
            nums[i], nums[j] = nums[j], nums[i]
            
        nums[l], nums[j] = nums[j], nums[l]
        
        return j
        
# @lc code=end

