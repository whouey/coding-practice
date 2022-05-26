#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        
        b = str(bin(n))[2:]
        return b.count('1') == 1
# @lc code=end

