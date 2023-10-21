# Write your MySQL query statement below
WITH ct as (
    select distinct product_id,
           sum(unit) as unit
    from Orders
    where order_date >='2020-02-01' and order_date <='2020-02-29'
    group by product_id
)

select p.product_name, o.unit
from ct as o
LEFT JOIN Products as p
on o.product_id = p.product_id
where o.unit >= 100