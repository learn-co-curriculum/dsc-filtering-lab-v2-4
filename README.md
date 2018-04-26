
# SQL Solar System Lab

NASA wants to go to Mars!  Before they build their rocket, NASA needs to track information about all of the planets in the Solar System.  Use SQL to help NASA build a database that stores all of this important information.

![solar_system](https://bilingualcarloscano.files.wordpress.com/2010/05/venus.jpg)

## Objectives

1. Use the `CREATE TABLE` command to create a new table with various data types
2. Use the `INSERT INTO` command to insert data (i.e. rows) into a database table
3. Use the `ALTER TABLE` command to add a column to an existing table
3. Use the `DELETE FROM` command to remove data (i.e. rows) from a database table

#### Part 1: Creating a table

In the `create.sql` file, use the `CREATE TABLE` command to create a table called `planets`.  Remember, your statement should look like the following:

> ```sql
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

Make sure to set the `id` column as the table's primary key.

#### Part 2: Inserting values

In the `insert.sql` file, input data for the first five planets closest to the sun using the `INSERT INTO` command.  The relevant information is provided in the table below:

|name   |color  |num_of_moons|mass   |
|-------|-------|-------|-------|
|Mercury|gray   |0      |0.55   |
|Venus  |yellow |0      |0.82   |
|Earth  |blue   |1      |1.00   |
|Mars   |red    |2      |0.11   |
|Jupiter|orange |67     |317.90 |

#### Part 3: Altering a table

NASA notices that the next planet, Saturn, has rings around it!  However, we do not have a column to keep track of this information.  In the `alter.sql` file, use the `ALTER TABLE` statement to add a column called `rings` with a data type of `boolean` to the `planets` table.

Now, add the data for the remaining planets, including the boolean representing whether each planet has rings.  Refer to the [SQLite3 documentation](https://www.sqlite.org/datatype3.html) to remember how to express booleans in SQLite3.

|name   |color  |num_of_moons  |mass   |rings  |
|-------|-------|-------|-------|-------|
|Saturn |hazel  |62     |95.19  |yes    |
|Uranus |light blue|27  |14.54  |yes    |
|Neptune|dark blue|14    |17.15  |yes    |
|Pluto  |brown  |5      |0.003  |no     |

#### Part 4: Deleting rows from a table

Wait just a moment!  NASA decided that Pluto is no longer a planet.  Remove Pluto from the table using the `DELETE FROM` command.

> **Hint**: you probably need to use a `WHERE` statement to accomplish this task.

## Summary

Congratulations!  NASA is one step closer to embarking upon its mission to Mars.  In this lab, we practiced using the basic CRUD (Create, Read, Update, Delete) actions in SQL.  We created a table to track all the planets in the solar system, we inserted values to populate this table, we altered the table to include another column, and we deleted data from the table.
