
# SQL Solar System Lab

NASA wants to go to Mars!  Before they build their rocket, NASA needs to track information about all of the planets in the Solar System.  Use SQL to help NASA build a database that stores all of this important information.

![solar_system](https://bilingualcarloscano.files.wordpress.com/2010/05/venus.jpg)

## Objectives

1. Use the `CREATE TABLE` command to create a table with various data types
2. Use the `ALTER TABLE` command to add a column to an existing table
3. Use the `INSERT INTO` command to insert data (i.e. rows) into a database table
4. Use the `UPDATE` command to change the value of a cell in a database table
5. Use the `DELETE FROM` command to remove data (i.e. rows) from a database table

### Part 1: Table setup

#### Create a table

In the `create.sql` file, use the `CREATE TABLE` command to create a table called `planets`.  Remember, your statement should look like the following:

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

Make sure to set the `id` column as the table's primary key.

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

## Summary

Congratulations!  NASA is one step closer to embarking upon its mission to Mars.  In this lab, we created a table to track all the planets in the solar system, altered the table to include another column, inserted values to populate the table, and we deleted data from the table.
