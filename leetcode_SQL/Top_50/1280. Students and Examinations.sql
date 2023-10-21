# Write your MySQL query statement below
select s.student_id,
       s.student_name,
       st.subject_name,
       COUNT(e.subject_name) as attended_exams
from Students as s
CROSS JOIN Subjects as st
LEFT JOIN Examinations as e
ON s.student_id = e.student_id
and st.subject_name = e.subject_name
group by s.student_id, s.student_name, st.subject_name
order by s.student_id, s.student_name