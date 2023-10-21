# Write your MySQL query statement below
DELETE p1
from Person as p1
JOIN
Person as p2
where p1.email = p2.email and p1.id > p2.id