# Write your MySQL query statement below
WITH combine as (
    select requester_id as id from RequestAccepted

    UNION ALL

    select accepter_id as id from RequestAccepted
)

select id, count(id) as num
from combine
group by id
order by num desc
limit 1