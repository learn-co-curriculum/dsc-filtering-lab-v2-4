# Selecting Data - Lab


## Introduction 

NASA wants to go to Mars! Before they build their rocket, NASA needs to track information about all of the planets in the Solar System. In this lab, you'll practice querying the database with various `SELECT` statements. This will include selecting different columns and implementing other SQL clauses like `WHERE` to return the data desired.

<img src="./images/planets.png" width="600">

## Objectives
You will be able to:
* Connect to a SQL database using Python
* Retrieve all information from a SQL table
* Retrieve a subset of records from a table using a `WHERE` clause
* Write SQL queries to filter and order results
* Retrieve a subset of columns from a table

## Connecting to the Database

To get started, import `sqlite3` as well as `pandas` for conveniently displaying results. Then, connect to the SQLite database located at `planets.db`. 


```python
# Your code here
```

## Database Schema

This database contains a single table, `planets`. This is the schema:

```
CREATE TABLE planets (
  id INTEGER PRIMARY KEY,
  name TEXT,
  color TEXT,
  num_of_moons INTEGER,
  mass REAL,
  rings BOOLEAN
);
```

The data looks something like this:

| id | name    | color      | num_of_moons | mass   | rings |
| -- | ------- | ---------- | ------------ | ------ | ----- |
| 1  | Mercury | gray       | 0            | 0.55   | FALSE |
| 2  | Venus   | yellow     | 0            | 0.82   | FALSE |
| 3  | Earth   | blue       | 1            | 1.00   | FALSE |
| 4  | Mars    | red        | 2            | 0.11   | FALSE |
| 5  | Jupiter | orange     | 67           | 317.90 | FALSE |
| 6  | Saturn  | hazel      | 62           | 95.19  | TRUE  |
| 7  | Uranus  | light blue | 27           | 14.54  | TRUE  |
| 8  | Neptune | dark blue  | 14           | 17.15  | TRUE  |

Write SQL queries for each of the statements below using the same pandas wrapping syntax from the previous lesson.

## Select just the name and color of each planet


```python
# Your code here
```

## Select all columns for each planet whose mass is greater than 1.00



```python
# Your code here
```

## Select the name and mass of each planet whose mass is less than or equal to 1.00


```python
# Your code here
```

## Select the name and color of each planet that has more than 10 moons


```python
# Your code here
```

## Select the planet that has at least one moon and a mass less than 1.00


```python
# Your code here
```

## Select the name and color of planets that have a color of blue, light blue, or dark blue


```python
# Your code here
```

## Select the name, color, and number of moons for the 4 largest planets that don't have rings and order them from largest to smallest

Note: even though the schema states that `rings` is a `BOOLEAN` and the example table shows values `TRUE` and `FALSE`, SQLite does not actually support booleans natively. From the [documentation](https://www.sqlite.org/datatype3.html#boolean_datatype):

> SQLite does not have a separate Boolean storage class. Instead, Boolean values are stored as integers 0 (false) and 1 (true).

Keep this in mind when you are filtering for "planets that don't have rings".


```python
# Your code here
```

## Summary

Congratulations! NASA is one step closer to embarking upon its mission to Mars. In this lab, You practiced writing `SELECT` statements that query a single table to get specific information. You also used other clauses and specified column names to cherry-pick the data we wanted to retrieve. 
