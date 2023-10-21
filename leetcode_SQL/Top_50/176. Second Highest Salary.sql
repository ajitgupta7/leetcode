SELECT MAX(salary) AS SecondHighestSalary
FROM (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 2
) AS Subquery
WHERE salary NOT IN (
    SELECT MAX(salary) FROM Employee
)