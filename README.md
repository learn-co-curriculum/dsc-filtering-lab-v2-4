# Filtering Data with SQL - Lab

## Introduction 

NASA wants to go to Mars! Before they build their rocket, NASA needs to track information about all of the planets in the Solar System. In this lab, you'll practice querying the database with various `SELECT` statements. This will include selecting different columns and implementing other SQL clauses like `WHERE` to return the data desired.

<img src="https://raw.githubusercontent.com/learn-co-curriculum/dsc-filtering-lab-v2-4/master/images/planets.png" alt="image of solar system" width="600">

## Objectives

You will practice the following:

* Retrieve a subset of records from a table using a `WHERE` clause
* Filter results using conditional operators such as `BETWEEN`, `IS NULL`, and `LIKE`
* Apply an aggregate function to the result of a filtered query

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

## SQL Queries

Write SQL queries for each of the statements below using the same pandas wrapping syntax from the previous lesson.

### 1. Select just the `name` and `color` of each planet


```python
# Your code here
```

### 2. Select all columns for each planet whose `num_of_moons` is 0


```python
# Your code here
```

### 3. Select the `name` and `mass` of each planet whose `name` has exactly 7 letters


```python
# Your code here
```

### 4. Select all columns for each planet whose `mass` is greater than 1.00


```python
# Your code here
```

### 5. Select the `name` and `mass` of each planet whose `mass` is less than or equal to 1.00


```python
# Your code here
```

### 6. Select the `name` and `mass` of each planet whose `mass` is between 0 and 50


```python
# Your code here
```

### 7. Select all columns for planets that have at least one moon and a `mass` less than 1.00

***Hint:*** You can use `AND` to chain together two conditions in SQL, similar to `and` in Python


```python
# Your code here
```

### 8. Select the `name` and `color` of planets that have a `color` containing the string "blue"


```python
# Your code here
```

### 9. Select the count of planets that don't have rings as `planets_without_rings`

Note: even though the schema states that `rings` is a `BOOLEAN` and the example table shows values `TRUE` and `FALSE`, SQLite does not actually support booleans natively. From the [documentation](https://www.sqlite.org/datatype3.html#boolean_datatype):

> SQLite does not have a separate Boolean storage class. Instead, Boolean values are stored as integers 0 (false) and 1 (true).


```python
# Your code here
```

### 10. Select the name of all planets, along with a value `has_rings` that returns "Yes" if the planet does have rings, and "No" if it does not


```python
# Your code here
```

## Summary

Congratulations! NASA is one step closer to embarking upon its mission to Mars. In this lab, You practiced writing `SELECT` statements that query a single table to get specific information. You also used other clauses and specified column names to cherry-pick the data we wanted to retrieve. 
