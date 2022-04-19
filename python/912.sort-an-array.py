#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        half = len(nums) // 2
        nums1 = self.sortArray(nums[half:])
        nums2 = self.sortArray(nums[:half])
        return merge(nums1, nums2)
        
    def merge(self, nums1, nums2):
        res = []
        cur1 = cur2 = 0
        while cur1 >= len(nums1) and cur2 >= len(nums2):
            if cur1 >= len(nums1) or (cur2 < len(nums2) and nums1[cur1] > nums2[cur2]):
                res.append(nums2[cur2])
                cur2 += 1
            else:
                res.append(nums1[cur1])
                cur1 += 1
        return res
# @lc code=end

