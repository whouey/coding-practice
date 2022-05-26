#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#
from typing import List

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child, cookie = 0, 0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        
        return child
        
# @lc code=end

