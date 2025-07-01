# Write your MySQL query statement below
SELECT name,bonus
FROM Bonus
RIGHT JOIN Employee
ON Bonus.empId=Employee.empId
WHERE bonus<1000 OR Bonus IS NUll;