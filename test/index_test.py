import unittest, pdb
from sql_runner import SQLRunner
import sys
sys.path.insert(0, '..')


class TestSQLBasicOperations(unittest.TestCase):
    def test_create_table(self):
        sql_runner = SQLRunner()
        table = sql_runner.execute_create_file()
        planets = table.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchone()[0]
        results = table.execute("PRAGMA table_info('%s')" % planets).fetchall()
        columns = []
        for el in results:
            cleaned_col = (el[1], el[2])
            columns.append(cleaned_col)
        # id
        self.assertEqual(columns[0][0], 'id', 'id not set to Primary Key')
        self.assertEqual(columns[0][1], 'INTEGER', 'id not set to Primary Key')
        # name
        self.assertEqual(columns[1][0], 'name', 'name not set to TEXT')
        self.assertEqual(columns[1][1], 'TEXT', 'name not set to TEXT')
        # color
        self.assertEqual(columns[2][0], 'color', 'color not set to TEXT')
        self.assertEqual(columns[2][1], 'TEXT', 'color not set to TEXT')
        # num_of_moons
        self.assertEqual(columns[3][0], 'num_of_moons', 'num_of_moons not set to INTEGER')
        self.assertEqual(columns[3][1], 'INTEGER', 'num_of_moons not set to INTEGER')
        # mass
        self.assertEqual(columns[4][0], 'mass', 'mass not set to REAL')
        self.assertEqual(columns[4][1], 'REAL', 'mass not set to REAL')

        table.close()

    def test_alter_table(self):
        sql_runner = SQLRunner()
        altered_table = sql_runner.execute_alter_file()

        planets = altered_table.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchone()[0]
        results = altered_table.execute("PRAGMA table_info('%s')" % planets).fetchall()
        self.assertEqual(results[-1][1], 'rings', 'rings not set to BOOLEAN')
        self.assertEqual(results[-1][2], 'BOOLEAN', 'rings not set to BOOLEAN')

        altered_table.close()

    def test_insert_into(self):
        sql_runner = SQLRunner()
        table = sql_runner.execute_alter_file()
        table_values = sql_runner.execute_insert_file()
        test = table_values.execute("SELECT * FROM planets").fetchall()

        self.assertEqual(len(test), 9)
        table_values.close()

    def test_delete_from(self):
        sql_runner = SQLRunner()
        table = sql_runner.execute_alter_file()
        table_values = sql_runner.execute_insert_file()
        deletion = sql_runner.execute_delete_file()
        test_delete = deletion.execute("SELECT * FROM planets").fetchall()

        self.assertEqual(len(test_delete), 8, "Delete Pluto!")
