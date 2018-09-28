import sqlite3

class SQLRunnerSelects:
    def __init__(self):
        self.connection = sqlite3.connect(':memory:')
        self.cursor = self.connection.cursor()

    def execute_create_file(self):
        file = open("./create_select.sql", "r")
        sql = file.read()
        table = self.cursor.execute(sql)
        return table

    def execute_seed_file(self):
        file = open("./seed.sql", "r")
        sql = file.read()
        table = self.cursor.execute(sql)
        return table
