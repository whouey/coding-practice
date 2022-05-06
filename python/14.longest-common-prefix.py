#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from typing import List

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        
        pre = strs[0]
        
        for i in range(1, len(strs)):
            if pre == '':
                break
            
            for j in range(len(pre)):
                if j >= len(strs[i]) or strs[i][j] != pre[j]:
                    pre = pre[:j]
                    break

        return pre

# @lc code=end