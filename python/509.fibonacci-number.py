#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

#%%
# @lc code=start

class Solution:
    memory = {0:0, 1:1}
    def _fib_cache(func):
        def wrap(self, *args):
            if args[0] not in self.memory:
                self.memory[args[0]] = func(self, args[0])
            return self.memory[args[0]]
        return wrap

    @_fib_cache
    def fib(self, n: int) -> int:
        return self.fib(n-1) + self.fib(n-2)

# @lc code=end

#%%
print(Solution().fib(10))

#%%