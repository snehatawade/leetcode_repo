# Write your MySQL query statement below
SELECT DISTINCT l1.num AS "ConsecutiveNums" 
FROM logs l1,logs l2,logs l3
WHERE l1.id = l2.id+1 AND l2.Id=l3.Id+1 AND l1.Num=l2.Num AND l2.Num=l3.Num;