#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        kids = len(ratings)
        candies = [1] * kids

        for i in range(kids-1):
            if ratings[i] < ratings[i+1]:
                candies[i+1] = candies[i] + 1
        
        for i in range(kids-1, 0, -1):
            if ratings[i-1] > ratings[i] and candies[i-1] <= candies[i]:
                candies[i-1] = candies[i] + 1
        
        return sum(candies)

# @lc code=end

