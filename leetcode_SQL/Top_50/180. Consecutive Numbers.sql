# Write your MySQL query statement below
WITH conNums as (
            select
                num,
                lead(num, 1) over() num1,
                lead(num, 2) over() num2
            from
                logs
                )
select
    distinct num as ConsecutiveNums
from
    conNums
where
    num = num1 and
    num = num2