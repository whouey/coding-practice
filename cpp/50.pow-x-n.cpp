/*
 * @lc app=leetcode id=50 lang=cpp
 *
 * [50] Pow(x, n)
 */


// @lc code=start
class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0 || x == 1)
            return 1;
            
        if (n < 0)
            return _myPow(1/x, -n);

        return _myPow(x, n);
    }
private:
    double _myPow(double x, int n, double prod = 1) {
        return n == 0 ? prod : _myPow(x, n-1, x*prod);
    }
};
// @lc code=end
