#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        import re 
        match = re.search('^[\s]*([+-]{0,1}\d+).*$', s)
        res = int(match.group(1)) if match else 0

        max = 2**31 - 1
        min = -(2**31)

        if res > max:
            return max
        elif res < min:
            return min
        else:
            return res

# @lc code=end

#%%
input = "+-12"
print(Solution().myAtoi(input))

# %%
