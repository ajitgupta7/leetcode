# Write your MySQL query statement below
select
    CASE WHEN mod(id, 2)=0 THEN id-1
        WHEN mod(id, 2) = 1 and id+1 not in (select id from Seat) THEN id
        ELSE id+1 END as id,
        student
FROM Seat
order by id