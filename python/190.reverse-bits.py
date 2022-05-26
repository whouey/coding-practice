#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(str(bin(n))[2:].rjust(32, '0')[::-1], 2)
# @lc code=end

