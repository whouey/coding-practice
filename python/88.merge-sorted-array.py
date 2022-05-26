#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cur1, cur2, cur = m-1, n-1, m+n-1

        while cur >= 0 and cur2 >= 0:
            if cur1 >= 0 and nums1[cur1] > nums2[cur2]:
                nums1[cur] = nums1[cur1]
                cur-=1
                cur1-=1
            else:
                nums1[cur] = nums2[cur2]
                cur-=1
                cur2-=1

# @lc code=end

