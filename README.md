
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

## Connecting to the DataBase

To get started import pandas and sqlite3. Then, connect to the database titled `planets.db`. 

Don't forget to instantiate a cursor so that you can later execute your queries.


```python
# Your code here
```

## Selecting Data

Here's an overview of the planet's table you'll be querying.

|name   |color |num_of_moons|mass|rings|
|-------|-------|-------|-------|-------|
|Mercury|gray   |0      |0.55   |no     |
|Venus  |yellow |0      |0.82   |no     |
|Earth  |blue   |1      |1.00   |no     |
|Mars   |red    |2      |0.11   |no     |
|Jupiter|orange |67     |317.90 |no     |
|Saturn |hazel  |62     |95.19  |yes    |
|Uranus |light blue|27  |14.54  |yes    |
|Neptune|dark blue|14   |17.15  |yes    |

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


```python
# Your code here
```

## Summary

Congratulations! NASA is one step closer to embarking upon its mission to Mars. In this lab, You practiced writing `SELECT` statements that query a single table to get specific information. You also used other clauses and specified column names to cherry-pick the data we wanted to retrieve. 
