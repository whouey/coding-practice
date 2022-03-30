#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""

        length = len(s)
        i = 0

        while i < length:
            left = i
            right = i

            while right+1 < length and s[right+1] == s[left]:
                right += 1
                i += 1
            
            while left >= 0 and right < length:

                if s[left] == s[right]:
                    longest = s[left:right+1]
                else:
                    break
                
                left -= 1
                right += 1
            
            answer = longest if len(longest) > len(answer) else answer

            i += 1

        return answer
# @lc code=end

