"""

link: https://leetcode.com/problems/combine-two-tables

problem: 数据查找

"""
SELECT p.FirstName, p.LastName, a.City, a.State 
FROM Person AS p 
LEFT JOIN Address AS a 
ON p.PersonId = a.PersonId
