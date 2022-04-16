/*
 * @lc app=leetcode id=341 lang=csharp
 *
 * [341] Flatten Nested List Iterator
 */
 using System.Collections;
 using System.Collections.Generic;

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool IsInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     int GetInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     IList<NestedInteger> GetList();
 * }
 */

// @lc code=start
public class NestedIterator {

    private List<int> values = new List<int>();
    private int cur = 0;

    public NestedIterator(IList<NestedInteger> nestedList) {
        foreach(var nested in nestedList)
            values.AddRange(GetIntegers(nested));
    }

    private IEnumerable<int> GetIntegers(NestedInteger nested) {
        if(nested.IsInteger())
            yield return nested.GetInteger();

        foreach(var sublist in nested.GetList())
            foreach(int sub in GetIntegers(sublist))
                yield return sub;
    }

    public bool HasNext() {
        return cur < values.Count();
    }

    public int Next() {
        return values[cur++];
    }
}
// @lc code=end

/**
 * Your NestedIterator will be called like this:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.HasNext()) v[f()] = i.Next();
 */
