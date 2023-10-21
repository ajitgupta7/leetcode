WITH
salary AS (
    SELECT
        account_id,
        income,
        CASE
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income >= 20000 AND income <= 50000 THEN 'Average Salary'
            ELSE 'High Salary'
        END AS category
    FROM
        Accounts
),

all_categories AS (
    SELECT 'Low Salary' AS category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary'
),

category_counts AS (
    SELECT
        category,
        COUNT(account_id) AS accounts_count
    FROM
        salary
    GROUP BY
        category
)

SELECT
    ac.category,
    IFNULL(cc.accounts_count, 0) AS accounts_count
FROM
    all_categories ac
LEFT JOIN
    category_counts cc ON ac.category = cc.category;