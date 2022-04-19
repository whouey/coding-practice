--
-- @lc app=leetcode id=586 lang=mysql
--
-- [586] Customer Placing the Largest Number of Orders
--

-- @lc code=start
# Write your MySQL query statement below
select customer_number from (
    select Count(*) as count_order, customer_number 
    from Orders 
    group by customer_number 
    order by count_order desc 
    limit 1
) t
-- @lc code=end

