# Write your MySQL query statement below
select round(100 * SUM(CASE WHEN i_or_s = 'i' THEN 1 ELSE 0 END)/count(i_or_s), 2) as immediate_percentage
FROM (select customer_id,
             min(order_date) as first_order_date,
             CASE
                WHEN min(customer_pref_delivery_date) = min(order_date) THEN 'i'
                ELSE 's'
                END as i_or_s
from Delivery
group by customer_id) o