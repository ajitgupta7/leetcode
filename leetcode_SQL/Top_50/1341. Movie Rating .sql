WITH movie_rating as (
    select m.movie_id,
            AVG(rating) as avg_rating,
            title
    from MovieRating as m
    LEFT JOIN Movies as c
    ON m.movie_id = c.movie_id
    where created_at BETWEEN '2020-02-01' AND '2020-02-28'
    group by movie_id
    order by avg_rating desc, title asc
    LIMIT 1),

user_rating as (
    select u.user_id, u.name,
          count(m.user_id) as rate_count
    from Users as u
    LEFT JOIN Movierating as m
    ON u.user_id = m.user_id
    group by m.user_id
    order by rate_count desc, name asc
    limit 1
)

select name as 'results'
from user_rating

UNION ALL

select title
from movie_rating