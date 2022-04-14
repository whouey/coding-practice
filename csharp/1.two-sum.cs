/*
 * @lc app=leetcode id=1 lang=csharp
 *
 * [1] Two Sum
 */
 
Console.WriteLine($"[{String.Join(", ", new Solution().TwoSum(new int[] {2,7,15,19}, 9))}]");

// @lc code=start
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        for(int i = 0; i < nums.Length; i++) {
            int diff = target - nums[i];
            for(int j = i+1; j < nums.Length; j++) {
                if(nums[j] == diff)
                    return new[] { i, j };
            }
        }
        return null;
    }
}
// @lc code=end

