import pyodbc


class MSDBconn:
    def __init__(self):
        self.database = "Northwind"
        self.UID = "SA"
        self.PWD = "Passw0rd2018"

        self.conn = pyodbc.connect('DSN=MYMSSQL;UID=' + self.UID +
                              ';PWD=' + self.PWD +
                              ';DATABASE=' + self.database)

        self.crsr = self.conn.cursor()

    def __sql_query(self, query):
        return self.crsr.execute(query)

