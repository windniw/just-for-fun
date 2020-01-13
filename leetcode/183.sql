"""

link: https://leetcode.com/problems/customers-who-never-order

problem: 数据查找

"""

SELECT 
    a.Name AS Customers 
FROM 
    Customers AS a 
WHERE 
    a.Id NOT IN (
        SELECT DISTINCT CustomerId FROM Orders
    );

---

SELECT 
    c.Name AS Customers
FROM 
    Customers AS c
LEFT JOIN 
    Orders o
ON 
    c.Id=o.CustomerId
where 
    o.CustomerId is null