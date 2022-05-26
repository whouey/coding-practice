#
# @lc app=leetcode id=1688 lang=python3
#
# [1688] Count of Matches in Tournament
#

# @lc code=start
class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0

        while n > 1:
            res += n // 2
            n = n // 2 + n % 2
        
        return res
# @lc code=end

