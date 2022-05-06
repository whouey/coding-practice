#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]

        add = 1
        for _ in range(n):
            for i in range(add):
                res.append(res[add-i-1] + add)
            add *= 2
        
        return res

# @lc code=end

