#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''

        i = len(a) - 1
        j = len(b) - 1
        carry = False

        while i >= 0 or j >= 0 or carry:
            x = a[i]=='1' if i >= 0 else False
            y = b[j]=='1' if j >= 0 else False

            sum = x + y + carry
            carry = sum > 1
            res += '0' if sum == 0 or sum == 2 else '1' 

            i -= 1
            j -= 1

        return res[::-1]

# @lc code=end

# class Solution:
#     def addBinary(self, a: 'str', b: 'str') -> 'str':
#         return bin(int(a, 2) + int(b, 2))[2:]