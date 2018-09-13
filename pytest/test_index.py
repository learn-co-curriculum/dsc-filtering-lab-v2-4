import pytest
from sql_runner import SQLRunner

def test_create_table():
    sql_runner = SQLRunner()
    table = sql_runner.execute_create_file()
    planets = table.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchone()[0]
    results = table.execute("PRAGMA table_info('%s')" % planets).fetchall()
    columns = []
    for el in results:
        cleaned_col = (el[1], el[2])
        columns.append(cleaned_col)
    # id
    assert columns[0][0] == 'id', 'id not set to Primary Key'
    assert columns[0][1].upper() == 'INTEGER', 'id not set to Primary Key'
    # name
    assert columns[1][0] == 'name', 'name not set to TEXT'
    assert columns[1][1].upper() == 'TEXT', 'name not set to TEXT'
    # color
    assert columns[2][0] == 'color', 'color not set to TEXT'
    assert columns[2][1].upper() == 'TEXT', 'color not set to TEXT'
    # num_of_moons
    assert columns[3][0] == 'num_of_moons', 'num_of_moons not set to INTEGER'
    assert columns[3][1].upper() == 'INTEGER', 'num_of_moons not set to INTEGER'
    # mass
    assert columns[4][0] == 'mass', 'mass not set to REAL'
    assert columns[4][1].upper() == 'REAL', 'mass not set to REAL'

def test_alter_table():
    sql_runner = SQLRunner()
    altered_table = sql_runner.execute_alter_file()
    planets = altered_table.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchone()[0]
    results = altered_table.execute("PRAGMA table_info('%s')" % planets).fetchall()

    assert results[-1][1] == 'rings', 'rings not set to BOOLEAN'
    assert results[-1][2] == 'BOOLEAN', 'rings not set to BOOLEAN'

def test_insert_into():
    sql_runner = SQLRunner()
    table = sql_runner.execute_alter_file()
    table_values = sql_runner.execute_insert_file()
    test = table_values.execute("SELECT * FROM planets").fetchall()

    assert len(test) == 9

def test_update_jupiter():
    sql_runner = SQLRunner()
    table = sql_runner.execute_alter_file()
    table_values = sql_runner.execute_insert_file()
    update = sql_runner.execute_update_file()
    result = 68

    assert table_values.execute("SELECT num_of_moons FROM planets WHERE name = 'Jupiter';").fetchone()[0] == result

def test_delete_from():
    sql_runner = SQLRunner()
    table = sql_runner.execute_alter_file()
    table_values = sql_runner.execute_insert_file()
    deletion = sql_runner.execute_delete_file()
    test_delete = deletion.execute("SELECT * FROM planets").fetchall()

    assert len(test_delete) == 8, "Delete Pluto!"
