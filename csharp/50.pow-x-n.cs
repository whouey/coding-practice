/*
 * @lc app=leetcode id=50 lang=csharp
 *
 * [50] Pow(x, n)
 */

 System.Console.WriteLine(new Solution().MyPow(2, -2147483648));

// @lc code=start
public class Solution {
    public double MyPow(double x, int n) {
        if (n == 0 || x == 1) {
            return 1;
        }
        else if (n > 0) {
            if (n == 1)
                return x;

            return (n%2 == 0 ? 1 : x) * MyPow(x*x, n/2);
        }
        else {
            if (n == -1)
                return 1/x;

            return (n%2 == 0 ? 1 : 1/x) * MyPow(x*x, n/2);
        }
    } 
}
// @lc code=end

