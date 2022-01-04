# Filtering Data with SQL - Lab

## Introduction 

NASA wants to go to Mars! Before they build their rocket, NASA needs to track information about all of the planets in the Solar System. In this lab, you'll practice querying the database with various `SELECT` statements. This will include selecting different columns and implementing other SQL clauses like `WHERE` to return the data desired.

<img src="./images/planets.png" width="600">

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


```python
# __SOLUTION__
import pandas as pd
import sqlite3
conn = sqlite3.connect('planets.db')
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


```python
# __SOLUTION__ 
pd.read_sql("""
SELECT name, color
  FROM planets;
""", conn)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>color</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mercury</td>
      <td>gray</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Venus</td>
      <td>yellow</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Earth</td>
      <td>blue</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mars</td>
      <td>red</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Jupiter</td>
      <td>orange</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Saturn</td>
      <td>hazel</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Uranus</td>
      <td>light blue</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Neptune</td>
      <td>dark blue</td>
    </tr>
  </tbody>
</table>
</div>



### 2. Select all columns for each planet whose `num_of_moons` is 0


```python
# Your code here
```


```python
# __SOLUTION__ 
pd.read_sql("""
SELECT *
  FROM planets
 WHERE num_of_moons = 0;
""", conn)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>color</th>
      <th>num_of_moons</th>
      <th>mass</th>
      <th>rings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Mercury</td>
      <td>gray</td>
      <td>0</td>
      <td>0.55</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Venus</td>
      <td>yellow</td>
      <td>0</td>
      <td>0.82</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



### 3. Select the `name` and `mass` of each planet whose `name` has exactly 7 letters


```python
# Your code here
```


```python
# __SOLUTION__ 
pd.read_sql("""
SELECT name, mass
  FROM planets
 WHERE length(name) = 7;
""", conn)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>mass</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mercury</td>
      <td>0.55</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jupiter</td>
      <td>317.90</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Neptune</td>
      <td>17.15</td>
    </tr>
  </tbody>
</table>
</div>



### 4. Select all columns for each planet whose `mass` is greater than 1.00


```python
# Your code here
```


```python
# __SOLUTION__ 
pd.read_sql("""
SELECT *
  FROM planets
 WHERE mass > 1.00;
""", conn)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>color</th>
      <th>num_of_moons</th>
      <th>mass</th>
      <th>rings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>Jupiter</td>
      <td>orange</td>
      <td>68</td>
      <td>317.90</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>Saturn</td>
      <td>hazel</td>
      <td>62</td>
      <td>95.19</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>Uranus</td>
      <td>light blue</td>
      <td>27</td>
      <td>14.54</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8</td>
      <td>Neptune</td>
      <td>dark blue</td>
      <td>14</td>
      <td>17.15</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### 5. Select the `name` and `mass` of each planet whose `mass` is less than or equal to 1.00


```python
# Your code here
```


```python
# __SOLUTION__ 
pd.read_sql("""
SELECT name, mass
  FROM planets
 WHERE mass <= 1.00;
""", conn)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>mass</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mercury</td>
      <td>0.55</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Venus</td>
      <td>0.82</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Earth</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mars</td>
      <td>0.11</td>
    </tr>
  </tbody>
</table>
</div>



### 6. Select the `name` and `mass` of each planet whose `mass` is between 0 and 50


```python
# Your code here
```


```python
# __SOLUTION__ 

# Technically this would also work if you said
# 0 <= mass AND mass <= 50
# but using BETWEEN is simpler and more efficient

pd.read_sql("""
SELECT name, mass
  FROM planets
 WHERE mass BETWEEN 0 AND 50;
""", conn)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>mass</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mercury</td>
      <td>0.55</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Venus</td>
      <td>0.82</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Earth</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mars</td>
      <td>0.11</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Uranus</td>
      <td>14.54</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Neptune</td>
      <td>17.15</td>
    </tr>
  </tbody>
</table>
</div>



### 7. Select all columns for planets that have at least one moon and a `mass` less than 1.00

***Hint:*** You can use `AND` to chain together two conditions in SQL, similar to `and` in Python


```python
# Your code here
```


```python
# __SOLUTION__

# "at least one moon", i.e. "1 or more moons",
# i.e. num_of_moons >= 1

pd.read_sql("""
SELECT *
  FROM planets
 WHERE num_of_moons >= 1
   AND mass < 1.00;
""", conn)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>color</th>
      <th>num_of_moons</th>
      <th>mass</th>
      <th>rings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>Mars</td>
      <td>red</td>
      <td>2</td>
      <td>0.11</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



### 8. Select the `name` and `color` of planets that have a `color` containing the string "blue"


```python
# Your code here
```


```python
# __SOLUTION__ 

# For this particular dataset, we also could have done:
# WHERE color = 'blue'
#    OR color = 'light blue'
#    OR color = 'dark blue'
# but that would not be flexible if the underlying data ever changed

# Also, the string of "%blue" would work for this dataset
# since the available colors all end with "blue", but putting
# % on either side is a better match for the prompt

pd.read_sql("""
SELECT name, color
  FROM planets
 WHERE color LIKE "%blue%";
""", conn)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>color</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Earth</td>
      <td>blue</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Uranus</td>
      <td>light blue</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Neptune</td>
      <td>dark blue</td>
    </tr>
  </tbody>
</table>
</div>



### 9. Select all columns for planets that don't have rings

Note: even though the schema states that `rings` is a `BOOLEAN` and the example table shows values `TRUE` and `FALSE`, SQLite does not actually support booleans natively. From the [documentation](https://www.sqlite.org/datatype3.html#boolean_datatype):

> SQLite does not have a separate Boolean storage class. Instead, Boolean values are stored as integers 0 (false) and 1 (true).


```python
# Your code here
```


```python
# __SOLUTION__

# We could also say
# WHERE NOT rings

pd.read_sql("""
SELECT *
  FROM planets
 WHERE rings = 0;
""", conn)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>color</th>
      <th>num_of_moons</th>
      <th>mass</th>
      <th>rings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Mercury</td>
      <td>gray</td>
      <td>0</td>
      <td>0.55</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Venus</td>
      <td>yellow</td>
      <td>0</td>
      <td>0.82</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Earth</td>
      <td>blue</td>
      <td>1</td>
      <td>1.00</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Mars</td>
      <td>red</td>
      <td>2</td>
      <td>0.11</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Jupiter</td>
      <td>orange</td>
      <td>68</td>
      <td>317.90</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



### 10. Select the name of all planets, along with a value `has_rings` that returns "Yes" if the planet does have rings, and "No" if it does not


```python
# Your code here
```


```python
pd.read_sql("""
SELECT name,
       CASE rings
       WHEN 1 THEN "Yes"
       WHEN 0 THEN "No"
       END AS has_rings
  FROM planets;
""", conn)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>has_rings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mercury</td>
      <td>No</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Venus</td>
      <td>No</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Earth</td>
      <td>No</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mars</td>
      <td>No</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Jupiter</td>
      <td>No</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Saturn</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Uranus</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Neptune</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
</div>



## Summary

Congratulations! NASA is one step closer to embarking upon its mission to Mars. In this lab, You practiced writing `SELECT` statements that query a single table to get specific information. You also used other clauses and specified column names to cherry-pick the data we wanted to retrieve. 
