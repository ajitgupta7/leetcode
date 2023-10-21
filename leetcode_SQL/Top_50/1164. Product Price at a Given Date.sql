-- CTE to get the latest price change for each product on or before '2019-08-16'
WITH LatestPrices AS (
    SELECT
        product_id,
        new_price,
        ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY change_date DESC) AS rn
    FROM
        Products
    WHERE
        change_date <= '2019-08-16'
)

-- Select prices for products with a price change on or before '2019-08-16'
SELECT
    product_id,
    new_price AS price
FROM
    LatestPrices
WHERE
    rn = 1

-- Use UNION to add products without a price change on or before '2019-08-16'
UNION

SELECT
    product_id,
    10 AS price
FROM
    Products
WHERE
    product_id NOT IN (SELECT product_id FROM LatestPrices)
GROUP BY
    product_id;