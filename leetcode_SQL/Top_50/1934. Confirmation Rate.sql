# Write your MySQL query statement below
select s.user_id,
        round(ifnull(avg(action = 'confirmed'), 0), 2) as confirmation_rate
from Signups as s
LEFT JOIN Confirmations as c
ON s.user_id = c.user_id
group by s.user_id