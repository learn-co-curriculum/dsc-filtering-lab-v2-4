
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

**Note, in this lesson the workflow will be a little different that usual. Instead of *just* editing your Jupyter Notebook, you're also going to have to use a text editor to put some SQL statements into a number of separate text files.**

**We're doing that (a) because it makes it easier for us to be able to write and run automated tests to "check your work", and (b) because as you start working on more complex projects, you'll often find yourself working with not just a Jupyter Notebook, but also some text files. For example, when you start to write your own re-usable code for cleaning up data you might well decide to create some Python files that you can access from and share between different Notebooks. **

### Part 1: Table setup

#### Create a table

Start by opening up the create.sql file in this directory in a text editor (not Jupyter Notebook). Write the necessary SQL in there to create a table using the `CREATE TABLE` command. Call the table `planets`. Save the file.

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

Now, create a sqlite database (lets call it planets.db), connect to it, and run the SQL from the create.sql file by reading it in and then executing it. 

> *Open up the hints.md file in this directory and look at hint # 1 if you need some help getting the database initialized and hint # 2 if you need some help figuring out how to read in the contents of the file *




```python
# Create the SQL database and connect to it

# Read in the contents of the create.sql file

# Execute that SQL against your database

```

#### Alter the table

NASA notices that several of the planets have rings around them.  However, we do not have a column to keep track of this information.  Open up alter.sql in a text editor, and write and save your SQL to use the `ALTER TABLE` statement to add a column called `rings` with a data type of `boolean` to the `planets` table. Write the code below to read in and execute that SQL against your database.


```python
# Your code for reading and executing alter.sql
```

### Part 2: Add and remove data

#### Add data to the table

Populate the empty `insert.sql` file in this directory with data for the nine planets that constitute the Solar System using the `INSERT INTO` command.  The relevant information is provided in the table below:

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

Then execute the contents of that file against the sqlite database using the cell below


```python
# Your code to read in the SQL from insert.sql and execute it
```

#### Update table data

NASA has confirmed that Jupiter has another 15 moons! In the empty update.sql file, write an `UPDATE` command so that Jupiter has 68 moons instead of 53.

> **Hint**: you probably need to use a `WHERE` statement to accomplish this task.


```python
# Your code to read in the SQL from update.sql and execute it
```

#### Remove data from the table

Wait just a moment!  NASA decided that Pluto is no longer a planet.  In the empty delete.sql file in this directory, remove Pluto from the table using the `DELETE FROM` command.


```python
# Your code to read in the SQL from delete.sql and execute it
```

## Onto Selecting Data

We will be querying data from the `planets` table we just created. We can see it again below:

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


* `select_name_and_mass_of_planets_with_mass_less_than_equal_to_one` should return the name and mass of each planet whose mass is less than or equal to 1.00

* `select_name_and_color_of_planets_with_more_than_10_moons` should return the name and color of each planets that has more than 10 moons

* `select_all_planets_with_moons_and_mass_less_than_one` should return the planet that has at least one moon and a mass less than 1.00

* `select_name_and_color_of_all_blue_planets` should return the name and color of planets that have a color of blue, light blue, or dark blue

## Summary

Congratulations! NASA is one step closer to embarking upon its mission to Mars. In this lab, we created a table to track all the planets in the solar system, altered the table to include another column, inserted values to populate the table, and we deleted data from the table. Then we practiced writing select statements that query a single table to get specific information. We also used other clauses and specified column names to cherry pick the data we wanted to retrieve. 
