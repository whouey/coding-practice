#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
from typing import List

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        removed = 0
        previous_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if previous_end > intervals[i][0]:
                removed += 1
            else:
                previous_end = intervals[i][1]

        return removed
        
# @lc code=end

