#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#

# @lc code=start
class StockSpanner:

    def __init__(self):
        self.stock = []
        self.span = []

    def next(self, price: int) -> int:
        res = 1
        i = len(self.stock)-1
        while i >= 0:
            if self.stock[i] <= price:
                res += self.span[i]
                i-=self.span[i]
            else:
                break

        self.stock.append(price)
        self.span.append(res)
        return res

# @lc code=end

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)