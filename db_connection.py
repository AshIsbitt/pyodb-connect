import pyodbc

# Setup variables that pass into connection

server = "localhost, 1433"
database = "Northwind"
UID = "SA"
PWD = "Passw0rd2018"

# https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Mac-OSX

conn = pyodbc.connect('DSN=MYMSSQL;UID='+ UID + ';PWD=' + PWD + ';DATABASE=' + database)
crsr = conn.cursor()
rows = crsr.execute("select * from orders").fetchall()
print(type(rows))
crsr.close()
conn.close()