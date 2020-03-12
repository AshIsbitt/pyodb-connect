import pyodbc

# Setup variables that pass into connection
server = "localhost, 1433"
database = "Northwind"
UID = "SA"
PWD = "Passw0rd2018"

# Follow this to the letter to set up PYODBC
# https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Mac-OSX

conn = pyodbc.connect('DSN=MYMSSQL;UID='+ UID + ';PWD=' + PWD + ';DATABASE=' + database)
# The cursor will maintain the state
crsr = conn.cursor()

# Run SQL commands with .execute()
crsr.execute("SELECT * FROM CUSTOMERS")

# This gets the headers of the db
print(crsr.description)

# Fetchall is dangerous because it can pull a LOT of data and this can
# stall or crash a server. Instead, use a while loop and a fetchone

# row = crsr.fetchall()
# for item in row:
#     print(item.ContactName, item.Fax)

while True:
    record = crsr.fetchone()
    if record is None:
        break
    print(record.ContactName)

rows = crsr.execute("SELECT * FROM Products")

while True:
    record = rows.fetchone()
    if record is None:
        break
    else:
        print(record.UnitPrice * 200)


crsr.close()
conn.close()