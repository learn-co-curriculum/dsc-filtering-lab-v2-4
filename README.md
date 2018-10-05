
# Selecting Data - Lab

## Introduction 

NASA wants to go to Mars! Before they build their rocket, NASA needs to track information about all of the planets in the Solar System. Use SQL to help NASA create, alter, and insert data into a database that stores all of this important information. Then practice querying the database with various `SELECT` statements. We will select different columns, and employ other SQL clauses like `WHERE` to return the data we would like.

![solar_system](https://bilingualcarloscano.files.wordpress.com/2010/05/venus.jpg)

## Objectives
You will be able to:
* Retrieve all the information from a table
* Retrieve a subset of records from a table using a `WHERE` clause
* Retrieve a subset of columns from a table

## Instructions

### Part 1: Table setup

#### Create a table

In the `create.sql` file, use the `CREATE TABLE` command to create a table called `planets`.  

**Remember:** your create table statement should be formatted like the following:

```sql
CREATE TABLE table_name (
   # column_names and data types here
);
```

NASA is interested in comparing each planet across several characteristics.  They want to know each planet's name,  color, number of moons, and mass (relative to earth).  Your columns should be the following types:

|column | type  |
|-------|-------|
|id     |integer|
|name   |text   |
|color  |text   |
|num_of_moons  |integer|
|mass   | real  |

> **Notes:** Make sure to set the `id` column as the table's primary key.

#### Alter the table

NASA notices that several of the planets have rings around them.  However, we do not have a column to keep track of this information.  In the `alter.sql` file, use the `ALTER TABLE` statement to add a column called `rings` with a data type of `boolean` to the `planets` table.

### Part 2: Add and remove data

#### Add data to the table

In the `insert.sql` file, input data for the nine planets that constitute the Solar System using the `INSERT INTO` command.  The relevant information is provided in the table below:

|name   |color |num_of_moons|mass|rings|
|-------|-------|-------|-------|-------|
|Mercury|gray   |0      |0.55   |no     |
|Venus  |yellow |0      |0.82   |no     |
|Earth  |blue   |1      |1.00   |no     |
|Mars   |red    |2      |0.11   |no     |
|Jupiter|orange |53     |317.90 |no     |
|Saturn |hazel  |62     |95.19  |yes    |
|Uranus |light blue|27  |14.54  |yes    |
|Neptune|dark blue|14   |17.15  |yes    |
|Pluto  |brown  |5      |0.003  |no     |

Refer to the [SQLite3 documentation](https://www.sqlite.org/datatype3.html) to remember how to express boolean values in SQLite3.

#### Update table data

NASA has confirmed that Jupiter has another 15 moons!  Write an `UPDATE` command in `update.sql` so that Jupiter has 68 moons instead of 53.

> **Hint**: you probably need to use a `WHERE` statement to accomplish this task.

#### Remove data from the table

Wait just a moment!  NASA decided that Pluto is no longer a planet.  In the `delete.sql` file, remove Pluto from the table using the `DELETE FROM` command.

## Onto Selecting Data

We will be querying data from the `planets` table we just created. We can see it again below. No need to query the table we just created for the following set of tests. This `planets` table is created in the `create.sql` file and already seeded with data from the `seed.sql` file. The table's data and structure is provided below:

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

Write your `SELECT` SQL queries inside the `sql_selects.py` file. To get the tests in `test/index_test.py` to pass, add the correct SQL query to the empty string returned in each function. See the example below.

```python
def select_example_func():
    return '''SQL SELECT STATEMENT GOES HERE'''
```

* `select_all_columns_and_rows` should return all of the data featured in the `planets` table

* `select_name_and_color_of_all_planets` should return the name and color of each planet

* `select_all_planets_with_mass_greater_than_one` should return all columns for each planet whose mass is greater than 1.00


* `select_name_and_mass_of_planets_with_mass_less_than_equal_to_one` should return the name and mass of each planet whose mass is greater than or equal to 1.00

* `select_name_and_color_of_planets_with_more_than_10_moons` should return the name and color of each planets that has more than 10 moons

* `select_all_planets_with_moons_and_mass_less_than_one` should return the planet that has at least one moon and a mass less than 1.00

* `select_name_and_color_of_all_blue_planets` should return the name and color of planets that have a color of blue, light blue, or dark blue

## Summary

Congratulations! NASA is one step closer to embarking upon its mission to Mars. In this lab, we created a table to track all the planets in the solar system, altered the table to include another column, inserted values to populate the table, and we deleted data from the table. Then we practiced writing select statements that query a single table to get specific information. We also used other clauses and specified column names to cherry pick the data we wanted to retrieve. 
