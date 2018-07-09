import sqlite3

class SQLRunner:
    def __init__(self):
        self.connection = sqlite3.connect(':memory:')
        self.cursor = self.connection.cursor()

    def execute_create_file(self):
        file = open("./create.sql", 'r')
        sql = file.read()
        table = self.cursor.execute(sql)
        file.close()
        return table

    def execute_alter_file(self):
        file = open("./create.sql", 'r')
        sql = file.read()
        table = self.cursor.execute(sql)

        alter_file = open("./alter.sql", 'r')
        sql = alter_file.read()
        altered_table = self.cursor.execute(sql)
        file.close()
        alter_file.close()
        return altered_table

    def execute_insert_file(self):
        file = open("./insert.sql", 'r')
        sql = file.read()
        table_values = self.cursor.execute(sql)
        file.close()
        return table_values

    def execute_update_file(self):
        file = open("./update.sql", 'r')
        sql = file.read()
        updated = self.cursor.execute(sql)
        file.close()
        return updated

    def execute_delete_file(self):
        file = open("./delete.sql", 'r')
        sql = file.read()
        deletion = self.cursor.execute(sql)
        file.close()
        return deletion
