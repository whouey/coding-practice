#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        start = 0
        end = 0

        length = len(s)
        hash = set()

        while end < length:

            if s[end] in hash:
                hash.remove(s[start])
                start += 1
            else:
                hash.add(s[end])
                end += 1

                l = end - start
                answer = l if l > answer else answer
                
        return answer
# @lc code=end

#%%
print(Solution().lengthOfLongestSubstring('pwwkew'))

#%%