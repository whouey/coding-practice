#
# @lc app=leetcode id=1802 lang=python3
#
# [1802] Maximum Value at a Given Index in a Bounded Array
#

# @lc code=start
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # where nums[index] -> max
        # => all other nums -> min
        # => nums[index] be the peak of graph
        l, r = 0, maxSum-n
        while l<r:
            mid = (l+r+1)//2
            if self.getSum(mid, n, index) <= maxSum-n:
                l = mid
            else:
                r = mid-1

        return l+1

    def getSum(self, value, n, index):
        if value - index > 0:
            leftSum = (value + (value - index)) * (index+1) / 2
        else:
            leftSum = (value + 1) * value / 2

        if value - (n-index-1) > 0:
            rightSum = (value + (value - (n-index-1))) * ((n-index-1)+1) / 2
        else:
            rightSum = (value + 1) * value / 2

        return leftSum + rightSum - value

# @lc code=end

print(Solution().maxValue(3,2,18))