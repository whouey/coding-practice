/*
 * @lc app=leetcode id=119 lang=csharp
 *
 * [119] Pascal's Triangle II
*/
using System.Collections;
using System.Collections.Generic;

System.Console.WriteLine(Helper.ToString(new Solution().GetRow(8)));

public static class Helper {
    public static string ToString(IList<int> list) 
        => $"[{string.Join(", ", list)}]"; 
}

// @lc code=start
public class Solution {
    public IList<int> GetRow(int rowIndex) {
        if (rowIndex == 0)
            return new[] {1};

        var last = GetRow(rowIndex - 1).ToList();
        last.Add(0);

        var cur = new List<int> {1};

        for(int i = 1; i < last.Count(); i++)
            cur.Add(last[i-1] + last[i]);
        
        return cur;
    }
}
// @lc code=end

