# SQL_more_queries

This project builds on `SQL_introduction`, covering MySQL user
management (creating users, granting privileges), table constraints
(`NOT NULL`, `DEFAULT`, `UNIQUE`, `AUTO_INCREMENT`, `PRIMARY KEY`,
`FOREIGN KEY`), and multi-table queries using subqueries and `JOIN`
(`INNER JOIN` and `LEFT JOIN`).

## Learning Objectives

- How to create a new MySQL user
- How to manage privileges for a user
- What's a `FOREIGN KEY`
- What's a subquery
- How to `JOIN` tables
- How to use `GROUP BY` and `COUNT` with joins

## Files

| File | Description |
|------|-------------|
| `0-privileges.sql` | Lists privileges of `user_0d_1` and `user_0d_2` |
| `1-create_user.sql` | Creates `user_0d_1` with all privileges |
| `2-create_read_user.sql` | Creates `hbtn_0d_2` and read-only `user_0d_2` |
| `3-force_name.sql` | Table `force_name` with `NOT NULL` name |
| `4-never_empty.sql` | Table `id_not_null` with a default id |
| `5-unique_id.sql` | Table `unique_id` with a unique default id |
| `6-states.sql` | Database `hbtn_0d_usa` and table `states` |
| `7-cities.sql` | Table `cities` with a foreign key to `states` |
| `8-cities_of_california_subquery.sql` | California cities via subquery |
| `9-cities_by_state_join.sql` | Cities with their state via `JOIN` |
| `10-genre_id_by_show.sql` | Shows with at least one genre |
| `11-genre_id_all_shows.sql` | All shows, `NULL` if no genre |
| `12-no_genre.sql` | Shows without a genre |
| `13-count_shows_by_genre.sql` | Genre counts, sorted descending |
| `14-my_genres.sql` | All genres of Dexter |
| `15-comedy_only.sql` | All Comedy shows |
| `16-shows_by_genre.sql` | All shows with their genres |

## Author

bahiizi11
