# Write your MySQL query statement below
SELECT D.name as 'Department', E.name as 'Employee', E.salary as 'Salary'
FROM Employee E JOIN Department D ON E.departmentId = D.id
WHERE E.salary = (SELECT max(salary) FROM Employee WHERE departmentID = E.departmentID);