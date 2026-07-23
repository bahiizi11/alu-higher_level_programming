# python-object_relational_mapping

This project covers connecting Python to a MySQL database two ways:
directly with the low-level `MySQLdb` driver, and through the
`SQLAlchemy` ORM. It also covers SQL injection: how string-formatted
queries are vulnerable to it, and how parameterized queries and ORM
filters prevent it.

## Learning Objectives

- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python class to a MySQL table
- How to use SQLAlchemy sessions to query, insert, update, delete
- Why and how to avoid SQL injections

## Files

| File | Description |
|------|-------------|
| `0-select_states.py` | List all states (MySQLdb) |
| `1-filter_states.py` | List states starting with N (MySQLdb) |
| `2-my_filter_states.py` | Filter states by input, unsafe (MySQLdb) |
| `3-my_safe_filter_states.py` | Filter states by input, injection-safe |
| `4-cities_by_state.py` | List all cities with their state (JOIN) |
| `5-filter_cities.py` | List cities of a given state, injection-safe |
| `model_state.py` | SQLAlchemy `State` model |
| `7-model_state_fetch_all.py` | List all states (SQLAlchemy) |
| `8-model_state_fetch_first.py` | Print the first state (SQLAlchemy) |
| `9-model_state_filter_a.py` | States containing "a" (SQLAlchemy) |
| `10-model_state_my_get.py` | Get a state by name, injection-safe |
| `11-model_state_insert.py` | Insert a new state (SQLAlchemy) |
| `12-model_state_update_id_2.py` | Update a state's name (SQLAlchemy) |
| `13-model_state_delete_a.py` | Delete states containing "a" |
| `model_city.py` | SQLAlchemy `City` model (FK to `State`) |
| `14-model_city_fetch_by_state.py` | List cities grouped by state |

## Author

bahiizi11
