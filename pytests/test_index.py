import pytest
from sql_runner import SQLRunner
from sql_runner_selects import SQLRunnerSelects
from sql_selects import *

sql_runner_select = SQLRunnerSelects()
table_select = sql_runner_select.execute_create_file()
table_select = sql_runner_select.execute_seed_file()


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


def test_select_all_columns_and_rows():
    result = [(1, 'Mercury', 'gray', 0, 0.55, 0.0), (2, 'Venus', 'yellow', 0, 0.82, 0.0), (3, 'Earth', 'blue', 1, 1.0, 0.0), (4, 'Mars', 'red', 2, 0.11, 0.0), (5, 'Jupiter', 'orange', 67, 317.9, 0.0), (6, 'Saturn', 'hazel', 62, 95.19, 1.0), (7, 'Uranus', 'light blue', 27, 14.54, 1.0), (8, 'Neptune', 'dark blue', 14, 17.15, 1.0)]
    assert table_select.execute(select_all_columns_and_rows()).fetchall() == result

def test_select_name_and_color_of_all_planets():
    result = [('Mercury', 'gray'), ('Venus', 'yellow'), ('Earth', 'blue'), ('Mars', 'red'), ('Jupiter', 'orange'), ('Saturn', 'hazel'), ('Uranus', 'light blue'), ('Neptune', 'dark blue')]
    assert table_select.execute(select_name_and_color_of_all_planets()).fetchall() == result

def test_select_all_planets_with_mass_greater_than_one():
    result = [(5, 'Jupiter', 'orange', 67, 317.9, 0.0), (6, 'Saturn', 'hazel', 62, 95.19, 1.0), (7, 'Uranus', 'light blue', 27, 14.54, 1.0), (8, 'Neptune', 'dark blue', 14, 17.15, 1.0)]
    assert table_select.execute(select_all_planets_with_mass_greater_than_one()).fetchall() == result

def test_select_name_and_mass_of_planets_with_mass_less_than_equal_to_one():
    result = [('Mercury', 0.55), ('Venus', 0.82), ('Earth', 1.0), ('Mars', 0.11)]
    assert table_select.execute(select_name_and_mass_of_planets_with_mass_less_than_equal_to_one()).fetchall() == result

def test_select_name_and_color_of_planets_with_more_than_10_moons():
    result = [('Jupiter', 'orange'), ('Saturn', 'hazel'), ('Uranus', 'light blue'), ('Neptune', 'dark blue')]
    assert table_select.execute(select_name_and_color_of_planets_with_more_than_10_moons()).fetchall() == result

def test_select_all_planets_with_moons_and_mass_less_than_one():
    result = [(4, 'Mars', 'red', 2, 0.11, 0.0)]
    assert table_select.execute(select_all_planets_with_moons_and_mass_less_than_one()).fetchall() == result

def test_select_name_and_color_of_all_blue_planets():
    result = [('Earth', 'blue'), ('Uranus', 'light blue'), ('Neptune', 'dark blue')]
    assert table_select.execute(select_name_and_color_of_all_blue_planets()).fetchall() == result
