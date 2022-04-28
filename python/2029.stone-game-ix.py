#
# @lc app=leetcode id=2029 lang=python3
#
# [2029] Stone Game IX
#
from typing import List

# @lc code=start
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        outcome = False
        
        trimmed = [x % 3 for x in stones]
        counts = { k:trimmed.count(k) for k in [x for x in range(3)] }
        total = 0

        total_count = len(stones)
        while total_count > 0:
            if total == 0: # first step
                if counts[0] % 2 == 0:
                    if counts[1] < counts[2]:
                        if counts[1] > 0:
                            counts[1] -= 1
                            total = (total + 1) % 3
                        else:
                            return outcome
                    else:
                        if counts[2] > 0:
                            counts[2] -= 1
                            total = (total + 2) % 3
                        else:
                            return outcome
                else:
                    if counts[1] > counts[2]:
                        if counts[1] > 0:
                            counts[1] -= 1
                            total = (total + 1) % 3
                        else:
                            return outcome
                    else:
                        if counts[2] > 0:
                            counts[2] -= 1
                            total = (total + 2) % 3
                        else:
                            return outcome
            elif total == 1:
                if counts[1] > 0:
                    counts[1] -= 1
                    total = (total + 1) % 3
                elif counts[0] > 0:
                    counts[0] -= 1
                else:
                    return outcome
            else:
                if counts[2] > 0:
                    counts[2] -= 1
                    total = (total + 2) % 3
                elif counts[0] > 0:
                    counts[0] -= 1
                else:
                    return outcome

            outcome = not outcome
            total_count -= 1
        
        return False

# @lc code=end

print(Solution().stoneGameIX([1,2,2,2,1,2]))