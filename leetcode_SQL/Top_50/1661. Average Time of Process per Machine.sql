# Write your MySQL query statement below
select m1.machine_id,
       ROUND(AVG(m2.timestamp - m1.timestamp), 3) as processing_time
from Activity as m1
JOIN Activity as m2
On m1.machine_id = m2.machine_id and
   m1.process_id = m2.process_id and
   m1.activity_type = 'start'    and
   m2.activity_type = 'end'

group by m1.machine_id