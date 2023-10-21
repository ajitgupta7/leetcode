# Write your MySQL query statement below
select c.customer_id
from (select distinct customer_id,
      count(distinct product_key) as cnt
      from Customer
      group by customer_id) as c
where c.cnt = (select count(product_key) from Product)